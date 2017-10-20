# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase


class LoginRequiredTest(TestCase):
    def test_login_required(self):
        response = self.client.get('/')
        self.assertEqual(
            response.status_code,
            302,
            msg="Login Required Validation Failed, Received code {0} instead of 302".format(response.status_code)
        )
        self.assertEqual(
            response.url,
            '/login?next=/',
            msg="Login Required Redirection Failed, Received url {0} instead of /login?next=/".format(response.url)
        )
