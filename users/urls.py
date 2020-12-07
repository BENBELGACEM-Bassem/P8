#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Define urls wiring templates to users app views"""

from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'users'

urlpatterns = [

    path('login', views.ConnectView.as_view(), name='login'),

    path('logout', login_required(views.QuitView.as_view()), name='logout'),

    path('signup', views.SignUpView.as_view(), name='signup'),

    path('account', login_required(views.AccountView.as_view()), name='account'),

]
