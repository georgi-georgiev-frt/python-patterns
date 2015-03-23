#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect


# Entities

class ProductInterface():  # Simple creation interface
    def get_type(self):
        raise NotImplemented


class ProductA(ProductInterface):
    def __init__(self):
        pass

    def get_type(self):
        return 'This is Product A'


class ProductB(ProductInterface):
    def __init__(self):
        pass

    def get_type(self):
        return 'This is Product B'


# Factory

class StaticFactory:
    TYPE_PRODUCT_A = ProductA
    TYPE_PRODUCT_B = ProductB

    @staticmethod
    def create(product):
        if inspect.isclass(product):
            return product()
        else:
            raise ValueError('Invalid product {}'.format(product))

# Creating products
if __name__ == "__main__":
    product_a = StaticFactory.create(StaticFactory.TYPE_PRODUCT_A)
    print product_a.get_type()

    product_b = StaticFactory.create(StaticFactory.TYPE_PRODUCT_B)
    print product_b.get_type()

### OUTPUT ###
# This is Product A
# This is Product B
