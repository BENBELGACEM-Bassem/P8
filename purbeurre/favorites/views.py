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
		current_user = self.request.user
		favorites = Favorite.objects.filter(user=current_user.id)
		if favorites.exists():
			self.paginate_by = 6
			return favorites
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

	def get_success_url(self):
		redirect_page = self.kwargs['redirect_page']
		product_count = self.kwargs['count']
		redirect_url = reverse_lazy('favorites:list')
		endpoint = f'{redirect_url}?page={redirect_page}'

		if product_count >= 2 and redirect_page > 1:
			return endpoint

		elif product_count < 2 and redirect_page > 1:
			return f'{redirect_url}?page=1'

		elif product_count >= 2 and redirect_page == 1:
			return f'{redirect_url}?page=1'

		elif product_count < 2 and redirect_page == 1:
			return f'{redirect_url}'