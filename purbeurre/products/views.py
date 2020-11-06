from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product


class ResultView(ListView):
	template_name = 'products/results.html'
	def get_queryset(self):
		pass
