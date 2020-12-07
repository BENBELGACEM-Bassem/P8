#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module to unitest products manager method"""

from django.test import TestCase

from products.models import Product, Category


class TestProductManager(TestCase):
    @classmethod
    def setUp(self):
        # Create a categories
        test_category1 = Category.objects.create(
            category_name='test_category1')
        test_category2 = Category.objects.create(
            category_name='test_category2')
        test_category3 = Category.objects.create(
            category_name='test_category3')
        # Create 5 test_products
        self.to_be_substituted = Product.objects.create(
            barcode='000000',
            product_name='to_be_substituted',
            nutrition_grade='D',
            url='http://unhealthy.com',
            product_image='http://image.com',
            nutrition_image='http://ingredients.com'
        )
        self.candidate1 = Product.objects.create(
            barcode='000001',
            product_name='candidate1',
            nutrition_grade='C',
            url='http://candidate1.com',
            product_image='http://image.com',
            nutrition_image='http://ingredients.com'
        )
        self.candidate2 = Product.objects.create(
            barcode='000002',
            product_name='candidate2',
            nutrition_grade='A',
            url='http://candidate2.com',
            product_image='http://image.com',
            nutrition_image='http://ingredients.com'
        )
        self.candidate3 = Product.objects.create(
            barcode='000003',
            product_name='candidate3',
            nutrition_grade='B',
            url='http://candidate3.com',
            product_image='http://image.com',
            nutrition_image='http://ingredients.com'
        )
        self.candidate4 = Product.objects.create(
            barcode='000004',
            product_name='candidate4',
            nutrition_grade='E',
            url='http://candidate4.com',
            product_image='http://image.com',
            nutrition_image='http://ingredients.com'
        )
        # Link substituted to 3 categories
        self.to_be_substituted.category.add(test_category1)
        self.to_be_substituted.category.add(test_category2)
        self.to_be_substituted.category.add(test_category3)
        # Link candidates from most similar to less similar
        self.candidate1.category.add(test_category1)
        self.candidate1.category.add(test_category2)
        self.candidate1.category.add(test_category3)
        self.candidate2.category.add(test_category1)
        self.candidate2.category.add(test_category2)
        self.candidate3.category.add(test_category1)
        # Link candidate4 which is similar but not healthier
        self.candidate4.category.add(test_category1)
        self.candidate4.category.add(test_category2)
        self.candidate4.category.add(test_category3)

    def test_get_substitute_candidates(self):
        product = self.to_be_substituted
        run_result = Product.objects.get_substitute_candidates(product)
        result_list = [food for food in run_result]
        correct_response = [self.candidate1, self.candidate2, self.candidate3]
        self.assertEqual(result_list, correct_response)
