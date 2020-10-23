#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module creating product and category data base tables,  based on django ORM"""

from django.db import models
from .managers import ProductManager, CategoryManager


class Category(models.Model):
    """Class representing categories table fields"""

    class Meta:
        db_table = 'Category'

    category_name = models.CharField(
        max_length=200,
        unique=True,
        help_text='Category name')

    objects = CategoryManager()

    def __str__(self):
        return self.category_name

    @classmethod
    def field_names(cls):
        return [f.name for f in cls._meta.get_fields()]


class Product(models.Model):
    """Class representing products table fields"""

    class Meta:
        db_table = 'Product'

    barcode = models.CharField(
        max_length=200,
        unique=True,
        help_text='Product barcode')
    product_name = models.CharField(max_length=200, help_text='Product name')
    nutrition_grade = models.CharField(
        max_length=1, help_text='Nutritional score of the product')
    url = models.URLField(help_text='hyperlink to Openfoodfacts product page')
    product_image = models.URLField(
        help_text='hyperlink to Openfoodfacts product image')
    nutrition_image = models.URLField(
        null=True,
        blank=True,
        help_text='hyperlink to Openfoodfacts nutrition data image')
    category = models.ManyToManyField(Category, related_name='categories')

    objects = ProductManager()

    def __str__(self):
        return self.product_name

    @classmethod
    def field_names(cls):
        return [f.name for f in cls._meta.get_fields()]
