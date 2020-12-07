#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module creating product and category data base tables,based on django ORM"""

from django.core.management.base import BaseCommand, CommandError
from products.models import Product, Category
from openfoodfacts.apifetcher.configuration import ApiOff as api
from openfoodfacts.apifetcher import dbbuilder


class Command(BaseCommand):
    help = 'Fill in an existing data base with data from Open Food Facts Api'

    def add_arguments(self, parser):
        """Define arguments for the command to be run"""
        parser.add_argument(
            '--size',
            type=int,
            help='Number of products per category')
        parser.add_argument(
            '--categories',
            nargs='*',
            help='Catgory names to be used')

    def handle(self, *args, **options):
        try:
            Category.objects.all().delete()
            Product.objects.all().delete()
            if options['categories']:
                api.category_list = options['categories']
            if options['size']:
                api.minimum_category_size = options['size']
            dbbuilder.build()
            self.stdout.write(self.style.SUCCESS(
                'Data base successfully populated'))
        except Product.DoesNotExist:
            raise CommandError('Product table has to be created first')
        except Category.DoesNotExist:
            raise CommandError('Category table has to be created first')

