# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Clients(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    iban = models.CharField(max_length=34)
    country = models.CharField(null=True, blank=True, max_length=10)
    createdTime = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,
                                  related_name='created_clients')
