#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

from django.contrib import admin

from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)
