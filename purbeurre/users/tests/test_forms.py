#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module to unitest users application form"""

from django.test import TestCase

from users.forms import UserForm


class TestUserForm(TestCase):

    def test_form_first_name_field_exists(self):
        form = UserForm()
        self.assertTrue(
            'first_name' in form.fields.keys())
