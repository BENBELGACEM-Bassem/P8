#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Favorite


class FavoriteListView(ListView):
	template_name = 'favorites/list.html'
	context_object_name = 'favorites_list'

	def get_queryset(self):
		# Retrieve favorites list
		try:
			favorites = Favorite.objects.all()
			if favorites.exists():
				self.paginate_by = 6
				return favorites
		except:
			return None


class SaveFavouriteView(CreateView):
	model = Favorite
	template_name = 'products/results.html'
	fields = ['substituted', 'substitute', 'user']

	def get_success_url(self):
		product_name = self.kwargs['product_name']
		redirect_page = self.kwargs['redirect_page']
		redirect_url = reverse_lazy('products:results', kwargs={'product_name': product_name})
		return f'{redirect_url}?page={redirect_page}'



class DeleteFavouriteView(DeleteView):
	model = Favorite
	template_name = 'favorites/list.html'
