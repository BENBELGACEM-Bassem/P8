#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Define urls wiring templates to favorites app views"""

from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'favorites'

urlpatterns = [
    path(
        'list',
        login_required(
            views.FavoriteListView.as_view()),
        name='list'),
    path(
        'save/<product_name>/<redirect_page>/',
        login_required(
            views.SaveFavouriteView.as_view()),
        name='save'),
    path(
        'delete/<int:pk>/<int:redirect_page>/<int:count>/',
        login_required(
            views.DeleteFavouriteView.as_view()),
        name='delete'),
]
