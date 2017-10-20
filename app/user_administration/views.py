# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, View
import logging
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import HttpResponse

logger = logging.getLogger(__name__)


class LoginPage(TemplateView):
    template_name = 'user_administration/login.html'


@method_decorator(login_required, name='dispatch')
class HomePage(View):
    def get(self, request):
        return HttpResponse("Home Page")
