#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('results/<product_name>/', views.ResultView.as_view(), name='results'),
    path('details/<int:pk>/', views.ProductView.as_view(), name='details'),
]
