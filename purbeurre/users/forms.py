#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name',)
        widgets = {
        'username': EmailInput(attrs={
            'placeholder': 'Entrer votre email'}),
        'first_name': TextInput(attrs={
            'placeholder': 'Entrer votre prénom' }),
            }