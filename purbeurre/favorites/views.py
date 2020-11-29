#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Define views managing a given user favorite products"""

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Favorite


class FavoriteListView(ListView):
    """Define a list of given user favorite products"""

    template_name = 'favorites/list.html'
    context_object_name = 'favorites_list'

    def get_queryset(self):
        """Retrieve the query set from the data base"""
        current_user = self.request.user
        favorites = Favorite.objects.filter(user=current_user.id)
        if favorites.exists():
            self.paginate_by = 6
            return favorites
        return None


class SaveFavouriteView(CreateView):
    """Save a product in user favorite list"""

    model = Favorite
    template_name = 'products/results.html'
    fields = ['substituted', 'substitute', 'user']

    def get_success_url(self):
        """Redirect to the same page in case user saves a product"""
        product_name = self.kwargs['product_name']
        redirect_page = self.kwargs['redirect_page']
        redirect_url = reverse_lazy(
            'products:results', kwargs={
                'product_name': product_name})
        return f'{redirect_url}?page={redirect_page}'


class DeleteFavouriteView(DeleteView):
    """Delete a product from Favorite data base table"""

    model = Favorite
    template_name = 'favorites/list.html'

    def get_success_url(self):
        """Define redirect in case of deleting"""
        # Current page
        redirect_page = self.kwargs['redirect_page']
        # Number of products in this page
        product_count = self.kwargs['count']
        # Original favorite url
        redirect_url = reverse_lazy('favorites:list')
        # Url redirecting to the current page
        endpoint = f'{redirect_url}?page={redirect_page}'

        # Case of more than one product per page outside of page 1
        if product_count >= 2 and redirect_page > 1:
            return endpoint
        # Case of one product per page outside of page 1
        elif product_count < 2 and redirect_page > 1:
            return f'{redirect_url}?page=1'
        # Case of more than one product per page on page 1
        elif product_count >= 2 and redirect_page == 1:
            return f'{redirect_url}?page=1'
        # Case of one product on the page one
        elif product_count < 2 and redirect_page == 1:
            return f'{redirect_url}'
