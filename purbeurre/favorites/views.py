#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
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

class DeleteFavouriteView(DeleteView):
	model = Favorite
	template_name = 'favorites/list.html'
