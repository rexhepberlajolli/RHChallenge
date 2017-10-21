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


class ClientListViewTest(LoginSetup):
    def setUp(self):
        super(ClientListViewTest, self).setUp()
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


class ClientDetailViewTest(LoginSetup):
    def setUp(self):
        super(ClientDetailViewTest, self).setUp()
        self.custom_client = Clients.objects.create(first_name='RH', last_name='CH', iban='IBAN')

    def test_get_client_details(self):
        response = self.client.get('/clients/{0}'.format(self.custom_client.pk), follow=True)
        client = response.context_data['client']
        self.assertEqual(
            client.first_name,
            self.custom_client.first_name,
            msg="Get client details failed, received client name {0} instead of {1}"
                .format(client.first_name, self.custom_client.first_name)
        )


class ClientUpdateViewTest(LoginSetup):
    changed_data = {
        'first_name': 'editedName',
        'last_name': 'editedLastname',
        'iban': 'XK051506001004471930'
    }

    def setUp(self):
        super(ClientUpdateViewTest, self).setUp()
        self.second_user = User.objects.create(username='testUser2', is_active=True, is_superuser=True)
        self.second_user.set_password('RHChallenge')
        self.second_user.save()
        self.first_c = Clients.objects.create(first_name='RH', last_name='CH', iban='IBAN', createdBy=self.user)
        self.second_c = Clients.objects.create(first_name='RH', last_name='CH', iban='IBAN', createdBy=self.second_user)

    def test_update_client(self):
        self.client.post('/clients/{0}/edit'.format(self.first_c.pk), data=self.changed_data)
        first_client = Clients.objects.first()
        self.assertEqual(
            first_client.first_name,
            self.changed_data.get('first_name'),
            msg="Update client details failed, received first name {0} instead of {1}"
                .format(first_client.first_name, self.changed_data.get('first_name'))
        )
        self.assertEqual(
            first_client.last_name,
            self.changed_data.get('last_name'),
            msg="Update client details failed, received last name {0} instead of {1}"
                .format(first_client.last_name, self.changed_data.get('last_name'))
        )
        self.assertEqual(
            first_client.iban,
            self.changed_data.get('iban'),
            msg="Update client details failed, received iban {0} instead of {1}"
                .format(first_client.iban, self.changed_data.get('iban'))
        )

    def test_update_forbidden_client(self):
        self.client.post('clients/{0}/edit'.format(self.second_c.pk), data=self.changed_data)
        second_client = Clients.objects.last()
        self.assertEqual(
            second_client.first_name,
            self.second_c.first_name,
            msg="Updating a forbidden user succeeded, received first name {0} instead of {1}"
                .format(second_client.first_name, self.second_c.first_name)
        )
        self.assertEqual(
            second_client.last_name,
            self.second_c.last_name,
            msg="Updating a forbidden user succeeded, received last name {0} instead of {1}"
                .format(second_client.last_name, self.second_c.last_name)
        )
        self.assertEqual(
            second_client.iban,
            self.second_c.iban,
            msg="Updating a forbidden user succeeded, received iban {0} instead of {1}"
                .format(second_client.iban, self.second_c.iban)
        )


class ClientDeleteViewTest(LoginSetup):
    def setUp(self):
        super(ClientDeleteViewTest, self).setUp()
        self.first_c = Clients.objects.create(first_name='RH', last_name='CH', iban='IBAN')

    def test_delete_client(self):
        self.first_c.createdBy = self.user
        self.first_c.save()
        self.client.post('/clients/{0}/delete'.format(self.first_c.pk))
        clients = Clients.objects.all()
        self.assertEqual(
            clients.count(),
            0,
            msg="Delete client failed, received {0} instead of {1} clients".format(clients.count(), 0)
        )

    def test_forbidden_delete_client(self):
        self.client.post('/clients/{0}/delete'.format(self.first_c.pk))
        clients = Clients.objects.all()
        self.assertEqual(
            clients.count(),
            1,
            msg="Delete forbidden client succeeded, received {0} instead of {1} clients".format(clients.count(), 1)
        )
