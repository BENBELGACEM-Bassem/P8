#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm


class SignUpView(SuccessMessageMixin, FormView):
	template_name = 'users/signup.html'
	form_class = UserForm
	success_url = reverse_lazy('users:login')

	def form_valid(self, form):
		form.save()
		first_name = form.cleaned_data.get('first_name')
		self.success_message = f"Bravo {first_name} ! votre compte est crée avec succés."
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super().get_context_data(**kwargs)
	    # Change the context form name
	    context['signup_form'] = context.pop('form')
	    return context


class ConnectView(SuccessMessageMixin, LoginView):

	template_name = 'users/login.html'
	success_url = reverse_lazy('core:home')

	def form_valid(self, form):
		self.success_message = "Vous êtes bien connectés à votre compte PurBeurre !"
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super().get_context_data(**kwargs)
	    # Change the context form name
	    context['login_form'] = context.pop('form')
	    return context

class QuitView(SuccessMessageMixin, LogoutView):

	template_name = 'core/index.html'
	success_url = reverse_lazy('core:home')
	success_message = "Vous êtes bien deconnectés ! A bientôt."

class AccountView(TemplateView):
	template_name = 'users/account.html'
