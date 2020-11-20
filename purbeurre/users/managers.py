#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
	
	 def create_user(self, email, date_of_birth, password=None):
	        """
	        Creates and saves a User with the given email, date of
	        birth and password.
	        """
	        if not email:
	            raise ValueError('Users must have an email address')

	        user = self.model(
	            email=self.normalize_email(email),
	            date_of_birth=date_of_birth,
	        )

	        user.set_password(password)
	        user.save(using=self._db)
	        return user
