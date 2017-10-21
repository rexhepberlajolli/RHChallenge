# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, CreateView, ListView, DetailView
import logging
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Clients
from .forms import ClientsForm
import json
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect


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
