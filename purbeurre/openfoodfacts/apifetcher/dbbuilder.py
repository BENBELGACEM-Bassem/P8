"""This module is responsible for building the user database"""

from .offcleaner import ProductCleaner as pcl
from .configuration import ApiOff as api
from ...products.models import Product, category



class ProductBuilder:
    """This class manages product data insertion into a given database"""

    def __init__(self):
        """Initialise product table instance"""
        self.headers = Product.fields

    def insert_product_data(self, product_rows):
        """Insert product data into an already created product table"""
        for row in product_rows:
            data_product = dict(
                zip(self.headers, row))
            Product.objects.create(**data_product)


class CategoryBuilder:
    """This class manages product data insertion into a given database"""

    def insert_category_data(self, categories):
        """Insert category data into an already created category table"""

        # Loop through list of barcodes given from the cleaner module
        for barcode in categories.keys():
            # Get the product object associated with this barcode
            product = Product.objects.get(barcode=barcode)
            # Get the list of categories associated to this barcode
            product_category_list = categories[barcode]
            for category_name in product_category_list:
                # Create and add a category object to product in one step
                product.category.create(category_name=category_name)

def build():
    """Build the content of the data base"""
    pc = pcl.extract_data()
    product_rows = pc[0]
    categories = pc[1]

    ProductBuilder().insert_product_data(product_rows)
    CategoryBuilder().insert_category_data(categories)

if __name__ == "__main__":
    build()
