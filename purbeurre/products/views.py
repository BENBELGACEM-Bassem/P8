from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product


class ResultView(ListView):
	template_name = 'products/results.html'
	context_object_name = 'product_list'
	

	def get_queryset(self):
		# Retrieve product to be substituted
		try:
			self.product = Product.objects.filter(product_name__icontains=self.kwargs['product_name'])[0]
			candidates = Product.objects.get_substitute_candidates(self.product)
			if candidates:
				self.paginate_by = 6
				return candidates
		except:
			return None

	def get_context_data(self, **kwargs):
		try:
		    # Call the base implementation first to get a context
		    context = super().get_context_data(**kwargs)
		    # Add in the product to be substituted to the context
		    context['product_to_substitute'] = self.product
		    return context
		except:
			return None


class ProductView(DetailView):
	template_name = 'products/details.html'
	model = Product
	context_object_name = 'product'
