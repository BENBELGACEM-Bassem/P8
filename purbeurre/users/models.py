#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module creating users data base table based on django ORM"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    """Class representing users table fields"""

    class Meta:
        db_table = 'User'

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
