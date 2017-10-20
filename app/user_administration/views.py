# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.views.generic import View
import logging

logger = logging.getLogger(__name__)


class HomePage(View):
    def get(self, request):
        logger.info("Home Page")
        return HttpResponse("Home Page")
