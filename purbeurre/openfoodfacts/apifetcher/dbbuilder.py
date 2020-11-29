#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""This module is responsible for building the user database"""

from .offcleaner import ProductCleaner as pcl
from products.models import Product, Category


class ProductBuilder:
    """This class manages product data insertion into a given database"""

    def __init__(self):
        """Initialise product table instance"""
        self.headers = [
            'barcode',
            'product_name',
            'nutrition_grade',
            'url',
            'product_image',
            'nutrition_image']

    def insert_product_data(self, product_rows):
        """Insert product data into an already created product table"""
        for row in product_rows:
            data_product = dict(
                zip(self.headers, row))
            Product.objects.update_or_create(**data_product)


class CategoryBuilder:
    """This class manages product data insertion into a given database"""

    def __init__(self):
        """Initialise category table instance"""
        self.headers = 'category_name'

    def insert_category_data(self, product_categories_dict):
        """Insert category data into an already created category table"""
        # Loop through list of barcodes given from the cleaner module
        for barcode in product_categories_dict.keys():
            # Get the product object associated with this barcode
            product = Product.objects.get(barcode=barcode)
            # Get the list of categories associated to this barcode
            categories_per_product_list = product_categories_dict[barcode]
            for category_name in categories_per_product_list:
                # Define new catgory field values
                data_category = {self.headers: category_name}
                # Create the new category object
                Category.objects.update_or_create(**data_category)
                # Get the new category object
                new_cat = Category.objects.get(category_name=category_name)
                # Associate the new category to the product
                product.category.add(new_cat)


def build():
    """Build the content of the data base"""
    # Call needed inputs from cleaner module
    pc = pcl.extract_data()
    product_rows = pc[0]
    product_categories_dict = pc[1]
    # Call building functions
    ProductBuilder().insert_product_data(product_rows)
    CategoryBuilder().insert_category_data(product_categories_dict)


if __name__ == "__main__":
    build()
