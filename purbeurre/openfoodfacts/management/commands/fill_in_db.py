#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module creating product and category data base tables,  based on django ORM"""

from django.core.management.base import BaseCommand, CommandError
from products.models import Product, Category
from openfoodfacts.apifetcher.configuration import ApiOff as api
from openfoodfacts.apifetcher import dbbuilder


class Command(BaseCommand):
    help = 'Fill in an existing data base with data from Open Food Facts Api'

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         '--category_list',
    #         type=list,
    #         help='Catgory names to be used')
    #     parser.add_argument(
    #         '--category_size',
    #         type=int,
    #         help='Number of products per category')

    def handle(self, *args, **options):
        try:
            Category.objects.all().delete()
            Product.objects.all().delete()
            # api.category_list = options['category_list']
            # api.category_size = options['category_size']
            dbbuilder.build()
            self.stdout.write(self.style.SUCCESS(
                'Data base successfully populated'))
        except Product.DoesNotExist:
            raise CommandError('Product table has to be created first')
        except Category.DoesNotExist:
            raise CommandError('Category table has to be created first')
