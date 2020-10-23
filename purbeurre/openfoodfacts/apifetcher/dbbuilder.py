"""This module is responsible for building the user database"""

from .offcleaner import ProductCleaner as pcl
from products.models import Product, Category


class ProductBuilder:
    """This class manages product data insertion into a given database"""

    def __init__(self):
        """Initialise product table instance"""
        self.headers = Product.field_names()

    def insert_product_data(self, product_rows):
        """Insert product data into an already created product table"""
        for row in product_rows:
            data_product = dict(
                zip(self.headers, row))
            Product.objects.create(**data_product)


class CategoryBuilder:
    """This class manages product data insertion into a given database"""

    def __init__(self):
        """Initialise category table instance"""
        self.headers = Category.field_names()

    def insert_category_data(self, product_categories_dict):
        """Insert category data into an already created category table"""
        # Loop through list of barcodes given from the cleaner module
        for barcode in product_categories_dict.keys():
            # Get the product object associated with this barcode
            product = Product.objects.get(barcode=barcode)
            # Get the list of categories associated to this barcode
            categories_per_product_list = product_categories_dict[barcode]
            for category_name in categories_per_product_list:
                # Create and add a category object to product in one step
                data_category = dict(zip(self.headers, category_name))
                product.categories.create(**data_category)


def build():
    """Build the content of the data base"""
    pc = pcl.extract_data()
    product_rows = pc[0]
    product_categories_dict = pc[1]

    ProductBuilder().insert_product_data(product_rows)
    CategoryBuilder().insert_category_data(product_categories_dict)

if __name__ == "__main__":
    build()
