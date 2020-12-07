#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module to unitest products application views"""

from django.test import TestCase
from django.urls import reverse

from products.models import Product, Category


class TestResultView(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 10 products for pagination tests
        number_of_products = 10
        # Create a category
        test_category = Category.objects.create(category_name='test_category')
        # Create a test_product
        test_product = Product.objects.create(
            barcode='000001',
            product_name='unhealthy',
            nutrition_grade='E',
            url='http://unhealthy.com',
            product_image='http://image.com',
            nutrition_image='http://ingredients.com'
        )
        # Link the product to the test_category
        test_product.category.add(test_category)
        # Create 10 candidates
        for product_id in range(number_of_products):
            test_product = Product.objects.create(
                barcode=f'barcode_{product_id}',
                product_name=f'product_name_{product_id}',
                nutrition_grade='B',
                url=f'url_{product_id}',
                product_image=f'product_image_{product_id}',
                nutrition_image=f'nutrition_image_{product_id}'
            )
            # Link products to the test_category
            test_product.category.add(test_category)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/results/unhealthy/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse(
                'products:results', kwargs={
                    'product_name': 'unhealthy'}))
        self.assertEqual(response.status_code, 200)


class TestProductView(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a category
        test_category = Category.objects.create(category_name='test_category')
        # Create a test_product product
        test_product = Product.objects.create(
            barcode='000002',
            product_name='healthy',
            nutrition_grade='A',
            url='http://healthy.com',
            product_image='http://image_healthy.com',
            nutrition_image='http://ingredients_healthy.com'
        )
        # Link the product to the test_category
        test_product.category.add(test_category)

    def setUp(self):
        test_product = Product.objects.get(barcode='000002')
        self.test_product_id = test_product.id

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(
            f'/products/details/{self.test_product_id}/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse(
                'products:details', kwargs={
                    'pk': self.test_product_id}))
        self.assertEqual(response.status_code, 200)
