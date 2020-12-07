#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module creating product and category data base tables,based on django ORM"""

from django.db import models
from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _
from .managers import ProductManager


class Category(models.Model):
    """Class representing categories table fields"""

    class Meta:
        db_table = 'Category'

    category_name = models.CharField(
        max_length=255,
        unique=True,
        help_text='Category name')

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """Class representing products table fields"""

    class Meta:
        db_table = 'Product'

    barcode = models.CharField(
        max_length=200,
        unique=True,
        help_text='Product barcode')
    product_name = models.CharField(max_length=500)
    nutrition_grade = models.CharField(
        max_length=1, help_text='Nutritional score of the product')
    url = models.URLField(
        max_length=500,
        help_text='hyperlink to Openfoodfacts product page')
    product_image = models.URLField(
        max_length=500, help_text='hyperlink to Openfoodfacts product image')
    nutrition_image = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        help_text='hyperlink to Openfoodfacts nutrition data image')
    category = models.ManyToManyField(Category, related_name='products')

    objects = ProductManager()

    def __str__(self):
        return self.product_name


class ProductForm(ModelForm):
    """Define a form related to Product table"""
    class Meta:
        model = Product
        fields = ('product_name',)
        widgets = {'product_name': TextInput(attrs={
            'class': 'form-control border border-warning',
            'placeholder': 'Trouvez un aliment', })}

        labels = {'product_name': _(''), }
