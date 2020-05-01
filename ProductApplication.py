"""
This models a Product Catalog module or application
"""
import os
from Tags import get_random_tags
from Entity import AttributedEntity

NUM_PRODUCTS = int(os.environ.get('NUM_PRODUCTS', 1000))

"""
A very simplified representation of a Product
"""
class Product(AttributedEntity):
    pass

products = []
for i in range(0, NUM_PRODUCTS):
    tags = get_random_tags()
    products.append(Product(tags))

def get_products():
    return products
