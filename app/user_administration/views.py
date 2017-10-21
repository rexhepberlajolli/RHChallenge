# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
import logging
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Clients
from .forms import ClientsForm
import json
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http.response import HttpResponseNotAllowed, HttpResponseForbidden


logger = logging.getLogger(__name__)


class LoginPage(TemplateView):
    template_name = 'user_administration/login.html'


@method_decorator(login_required, name='dispatch')
class ClientCreateView(CreateView):
    model = Clients
    form_class = ClientsForm
    success_url = reverse_lazy('UserAdministration:ClientListView')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.createdBy = self.request.user
        obj.save()
        messages.add_message(self.request, messages.SUCCESS, "Client Created Successfully")
        return super(ClientCreateView, self).form_valid(form)

    def form_invalid(self, form):
        errors = json.loads(form.errors.as_json())
        for error in errors:
            for message in errors[error]:
                messages.add_message(self.request, messages.ERROR, message['message'])
        return redirect(self.success_url)


@method_decorator(login_required, name='dispatch')
class ClientListView(ListView):
    model = Clients
    template_name = 'user_administration/clients.html'
    context_object_name = 'clients'
    paginate_by = 10
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        context['create_form'] = ClientsForm()
        return context


@method_decorator(login_required, name='dispatch')
class ClientDetailView(DetailView):
    model = Clients
    template_name = 'user_administration/client_detail.html'
    context_object_name = 'client'


@method_decorator(login_required, name='dispatch')
class ClientUpdateView(UpdateView):
    model = Clients
    form_class = ClientsForm
    context_object_name = 'client'
    template_name = 'user_administration/client_update.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        if obj.createdBy == self.request.user:
            messages.add_message(self.request, messages.SUCCESS, "Client Data Updated Successfully")
        else:
            messages.add_message(self.request, messages.ERROR, "You Can Not Update This Client's Data")
            return self.form_invalid(form)
        return super(ClientUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        errors = json.loads(form.errors.as_json())
        for error in errors:
            for message in errors[error]:
                messages.add_message(self.request, messages.ERROR, message['message'])
        return super(ClientUpdateView, self).form_invalid(form)

    def get_success_url(self, **kwargs):
        pk = self.kwargs['pk']
        return reverse_lazy('UserAdministration:ClientUpdateView', kwargs={'pk': pk})


class ClientDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('UserAdministration:ClientListView')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.createdBy != self.request.user:
            messages.add_message(self.request, messages.ERROR, "You do not have access to remove this client")
            return redirect(reverse_lazy('UserAdministration:ClientDetailView', kwargs={'pk': obj.pk}))
        messages.add_message(self.request, messages.SUCCESS, "Client Removed Successfully")
        return super(ClientDeleteView, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed("GET")

