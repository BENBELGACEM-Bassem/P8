#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module creating models managers"""

from django.db import models


class ProductManager(models.Manager):
    def get_substitute_candidates(self, product):
        """Get a product substitute for a given product"""
        # Subcategories related to the product
        subcategories = product.category.all()
        # Remaining objects where to look for a candidate
        candidate_objects = self.model.objects.exclude(id=product.id)
        # Find similar_products candidates sharing number of subcategories
        similar_products = []
        for candidate in candidate_objects:
            subcat = candidate.category.all()
            similarity = len(subcategories.intersection(subcat))
            grade = candidate.nutrition_grade
            candidate_description = (candidate, similarity, grade)
            similar_products.append(candidate_description)
        # Sort similar_products from most to less similar
        sorted_by_similarity = sorted(
            similar_products,
            key=lambda tup: tup[1],
            reverse=True)
        # Leave only equal or better grade among similar_products
        healthier_candidate_objects = [
            similar_product[0] for similar_product in sorted_by_similarity if similar_product[2] < product.nutrition_grade]
        # Get a queryset from this list
        healthier_candidate_object_ids = [
            product.id for product in healthier_candidate_objects]
        healthier_candidate_queryset = self.model.objects.filter(
            id__in=healthier_candidate_object_ids)
        # Return a queryset
        return healthier_candidate_queryset
