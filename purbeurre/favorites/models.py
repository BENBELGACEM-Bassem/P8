#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module creating favorite products data base table based on django ORM"""

from django.db import models
from products.models import Product
from django.conf import settings


class Favorite(models.Model):
    """Class representing favorite prodcuts table fields"""

    class Meta:
        db_table = 'Favorite'

    substituted = models.ForeignKey(
        Product,
        on_delete=models.CASCADE)

    substitute = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='+')

    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='favorites')
