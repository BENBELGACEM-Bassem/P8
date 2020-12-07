#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module creating users data base table based on django ORM"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Class representing users table fields"""

    class Meta:
        db_table = 'User'

    first_name = models.CharField(max_length=200)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
