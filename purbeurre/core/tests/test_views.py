#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module to unitest core application views"""

from django.test import TestCase
from django.urls import reverse


class TestHomeView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)


    class TestLegalNoticeView(TestCase):

        def test_view_url_exists_at_desired_location(self):
            response = self.client.get('/legal/')
            self.assertEqual(response.status_code, 200)

        def test_view_url_accessible_by_name(self):
            response = self.client.get(reverse('core:legal_notice'))
            self.assertEqual(response.status_code, 200)
