# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
import factory.django

from django.test import TestCase
from app.models import Review


# Create your tests here.

class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        django_get_or_create = (
                'user',
                #'datetime',
                #'description',
                'text',
                'place',
                )

        user = 'user1'
        text = 'nice place'
        place = 'McDonalds'

class ReviewTest(TestCase):
    def test_create_product(self):
        product = ProductFactory()
        all_products = Product.objects.all()
        self.assertEqual(len(all_products), 1)
        pr = all_product[0]
        self.assertEqual(pr,product)

        self.assertEqual(pr.name, 'NERF blaster')
        self.asserEqual(pr.description, 'Toy gun')
        self.assertEqual(pr.price, 100)
        self.assertEqual(self.store, 'BR')
        self.assertEqual(self.stock, 50)


'''

