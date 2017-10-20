# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase


class InitialTest(TestCase):
    def setUp(self):
        self.value = 1 + 1

    def test_initial(self):
        self.assertEqual(1 + 1, self.value)
