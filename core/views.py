#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Define views managing serving home and legal notice pages"""

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from products.models import ProductForm


class HomeView(FormView):
	template_name = 'core/index.html'
	form_class = ProductForm

	def form_valid(self, form):
		# Retrieve form cleaned content and send it to the result view
		product_name = form.cleaned_data.get('product_name')
		self.success_url = reverse_lazy('products:results', kwargs={'product_name': product_name})
		return super().form_valid(form)


class LegalNoticeView(TemplateView):
	template_name = 'core/legal_notice.html'
	def get(self, request):
		return render(request, self.template_name)
