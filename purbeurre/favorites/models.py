#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module creating favorite products data base table based on django ORM"""

from django.db import models
from products.models import Product
from django.conf import settings
from .managers import FavoriteManager

class Favorite(models.Model):
    """Class representing favorite prodcuts table fields"""

    class Meta:
        db_table = 'Favorite'
        unique_together = ['substituted', 'substitute']

    substituted = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='substituties',
        help_text='Product to be substituted')

    substitute = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='+',
        help_text='Substitute product')

    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='favorites',
        help_text='User who saves a substitute product')

    objects = FavoriteManager()

    def __str__(self):
        return self.substitute
