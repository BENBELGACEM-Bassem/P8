#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from favorites.models import Favorite


class ResultView(ListView):
	template_name = 'products/results.html'
	context_object_name = 'product_list'


	def get_queryset(self):
		# Retrieve product to be substituted
		if Product.objects.filter(product_name__icontains=self.kwargs['product_name']).exists():
			self.product = Product.objects.filter(product_name__icontains=self.kwargs['product_name'])[0]
			candidates = Product.objects.get_substitute_candidates(self.product)
			if candidates.exists():
				self.paginate_by = 6
				return candidates
			return None
		else:
			self.product = None
			return None


	def user_favorites(self):
		status = []
		current_user = self.request.user
		if self.get_queryset():
			for candidate in self.get_queryset():
				if Favorite.objects.filter(user=current_user.id, substitute=candidate.id).exists():
					status.append(candidate)
			return status
		return status

	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super().get_context_data(**kwargs)
	    # Add in the product to be substituted to the context
	    context['substituted'] = self.product
	    context['user_favorites'] = self.user_favorites()
	    return context


class ProductView(DetailView):
	template_name = 'products/details.html'
	model = Product
	context_object_name = 'product'
