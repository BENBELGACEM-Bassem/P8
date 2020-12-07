#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Define views managing serving substitutes for a given product"""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from favorites.models import Favorite


class ResultView(ListView):
    """Define a list of substitute candidates for a given one"""

    template_name = 'products/results.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        """Retrieve the query set from the data base using manager method"""
        if Product.objects.filter(
                product_name__icontains=self.kwargs['product_name']).exists():
            self.product = Product.objects.filter(
                product_name__icontains=self.kwargs['product_name'])[0]
            candidates = Product.objects.get_substitute_candidates(
                self.product)
            if candidates.exists():
                self.paginate_by = 6
                return candidates
            return None
        else:
            self.product = None
            return None

    def user_favorites(self):
        """Define a favorites for the login user"""
        status = []
        current_user = self.request.user
        if self.get_queryset():
            for candidate in self.get_queryset():
                if Favorite.objects.filter(
                        user=current_user.id,
                        substitute=candidate.id).exists():
                    status.append(candidate)
            return status
        return status

    def get_context_data(self, **kwargs):
        """Create context parameter"""
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the product to be substituted to the context
        context['substituted'] = self.product
        # Add user favorite list to the context
        context['user_favorites'] = self.user_favorites()
        return context


class ProductView(DetailView):
    """Define details view for a specific product"""

    template_name = 'products/details.html'
    model = Product
    context_object_name = 'product'
