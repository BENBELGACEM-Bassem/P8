#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module to unitest users application views"""

from django.test import TestCase
from django.urls import reverse

from users.models import User


class TestSignUpView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/users/signup')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)


class TestConnectView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/users/login')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)


class TestQuitView(TestCase):

    def setUp(self):
        # Create a user
        test_user = User.objects.create_user(
            username='testuser1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        test_user.save()

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(
            username='testuser1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        response = self.client.get('/users/logout')
        # Check that we got a redirect to the home page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, ('/'))

    def test_view_url_accessible_by_name(self):
        login = self.client.login(
            username='testuser1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('users:logout'))
        # Check that we got a redirect to the home page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, ('/'))

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))


class TestAccountView(TestCase):

    def setUp(self):
        # Create a user
        test_user = User.objects.create_user(
            username='testuser2',
            first_name='test',
            password='1X<ISRUkw+tuK')
        test_user.save()

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(
            username='testuser2',
            first_name='test',
            password='1X<ISRUkw+tuK')
        response = self.client.get('/users/account')
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser2')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(
            username='testuser2',
            first_name='test',
            password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('users:account'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser2')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('users:account'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))
