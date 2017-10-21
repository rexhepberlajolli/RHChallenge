# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Clients


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


class LoginSetup(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testUser', is_active=True, is_superuser=True)
        self.user.set_password('RHChallenge')
        self.user.save()
        self.client.force_login(self.user)


class ClientsViewTest(LoginSetup):
    def setUp(self):
        super(ClientsViewTest, self).setUp()
        self.custom_client = Clients.objects.create(first_name='RH', last_name='CH', iban='IBAN')

    def test_client_create(self):
        data = {'first_name': 'Rexhep', 'last_name': 'Berlajolli', 'iban': 'XK051506001004471930'}
        self.client.post('/add', data=data)
        clients_count = Clients.objects.count()
        self.assertEqual(
            clients_count,
            2,
            msg="Create client failed, received {0} clients instead of 2".format(clients_count)
        )

    def test_client_create_validation(self):
        data = {'first_name': 'Invalid', 'last_name': 'Data', 'iban': 'INVALID_IBAN'}
        self.client.post('/add', data=data)
        clients_count = Clients.objects.count()
        self.assertEqual(
            clients_count,
            1,
            msg="Insertion of invalid data succeeded, received {0} clients instead of 1".format(clients_count)
        )

    def test_get_clients(self):
        response = self.client.get('/')
        clients = response.context_data['clients']
        self.assertEqual(
            list(clients),
            list(Clients.objects.all()),
            msg="Get clients failed, received clients {0} instead of {1}".format(clients, [self.custom_client])
        )
