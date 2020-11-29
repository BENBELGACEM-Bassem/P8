#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Define forms for users app"""

from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput


class UserForm(UserCreationForm):
    """"Inherit User fields to define ones for signup form"""

    class Meta(UserCreationForm.Meta):
        model = User
    # Adding ur customized first_name field
        fields = UserCreationForm.Meta.fields + ('first_name',)
    # Defining components for the frontend
        widgets = {
            'username': EmailInput(attrs={
                'placeholder': 'Entrer votre email'}),
            'first_name': TextInput(attrs={
                'placeholder': 'Entrer votre prénom'}),
        }
