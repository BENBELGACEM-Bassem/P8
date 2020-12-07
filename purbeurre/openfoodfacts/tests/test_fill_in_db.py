#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module to test loading the database"""

from django.test import TestCase
from django.core.management import call_command

from products.models import Product


class TestCommand(TestCase):

    def test_load_sufficient_product_number_per_category(self):
        # Size is number of products per category
        # Categories is the list of chosen categories
        opts = {'size': 50, 'categories': ["Fromages"]}
        call_command('fill_in_db', **opts)
        number_products_loaded = Product.objects.all().count()
        # Test number for fromages category
        assert (number_products_loaded >= 50)

    def test_load_sufficient_product_number_in_db(self):
        # Size is number of products per category
        # Default number of categories is 5
        opts = {'size': 20}
        call_command('fill_in_db', **opts)
        number_products_loaded = Product.objects.all().count()
        # Test the whole number is 5*20
        assert (number_products_loaded >= 100)
