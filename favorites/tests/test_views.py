#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module to unitest favorites application views"""

from django.test import TestCase
from django.urls import reverse

from users.models import User
from products.models import Product, Category
from favorites.models import Favorite


class TestFavoriteListView(TestCase):

    def setUp(self):
        # Create 2 users
        self.test_user1 = User.objects.create_user(
            username='user1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        self.test_user2 = User.objects.create_user(
            username='user2',
            first_name='test',
            password='1X<ISRUkw+tuK')
        self.test_user1.save()
        self.test_user2.save()
        # Create a category
        test_cat = Category.objects.create(category_name='test_cat')
        # Create 3 test_products
        self.test_product1 = Product.objects.create(
            barcode='000010',
            product_name='substituted',
            nutrition_grade='A',
            url='http://substituted.com',
            product_image='http://image.com',
            nutrition_image='http://ingredients.com'
        )
        self.test_product2 = Product.objects.create(
            barcode='000020',
            product_name='substitute1',
            nutrition_grade='A',
            url='http://substitute1.com',
            product_image='http://image.com',
            nutrition_image='http://ingredients.com'
        )
        self.test_product3 = Product.objects.create(
            barcode='000030',
            product_name='substitute2',
            nutrition_grade='A',
            url='http://substitute2.com',
            product_image='http://image.com',
            nutrition_image='http://ingredients.com'
        )
        # Link the product to the test_cat
        self.test_product1.category.add(test_cat)
        self.test_product2.category.add(test_cat)
        self.test_product3.category.add(test_cat)
        # Link test_product2 to user1 favorites
        self.favorite1 = Favorite.objects.create(
            substituted=self.test_product1,
            substitute=self.test_product2)
        self.favorite1.user.add(self.test_user1)
        # Link test_product3 to user2 favorites
        self.favorite2 = Favorite.objects.create(
            substituted=self.test_product1,
            substitute=self.test_product3)
        self.favorite2.user.add(self.test_user2)

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(
            username='user1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        response = self.client.get('/favorites/list')
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'user1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(
            username='user1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('favorites:list'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'user1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('favorites:list'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_show_only_current_user_list(self):
        login = self.client.login(
            username='user1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('favorites:list'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'user1')
        # Check we only have current user favorite product
        self.assertContains(response, self.test_product2.product_name)
        self.assertNotContains(response, self.test_product3.product_name)


class SaveFavouriteView(TestCase):

    def setUp(self):
        # Create a user
        test_user = User.objects.create_user(
            username='user1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        test_user.save()

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(
            username='user1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        response = self.client.get('/users/account')
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'user1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(
            username='user1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('users:account'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'user1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('users:account'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))


class TestDeleteFavouriteView(TestCase):

    def setUp(self):
        # Create a user
        test_user = User.objects.create_user(
            username='user1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        test_user.save()

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(
            username='user1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        response = self.client.get('/users/account')
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'user1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(
            username='user1',
            first_name='test',
            password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('users:account'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'user1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('users:account'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))
