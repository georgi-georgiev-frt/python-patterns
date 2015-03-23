#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Factory

class StaticFactory:
    TYPE_PRODUCT_A = 'a'
    TYPE_PRODUCT_B = 'b'

    @staticmethod
    def create(type):
        if type == StaticFactory.TYPE_PRODUCT_A:
            return ProductA()

        elif type == StaticFactory.TYPE_PRODUCT_B:
            return ProductB()

        else:
            raise ValueError('Invalid type {}'.format(type))


# Entities

class ProductInterface():  # Simple creation interface
    def get_type(self):
        raise NotImplemented


class ProductA(ProductInterface):
    def __init__(self):
        pass

    def get_type(self):
        return StaticFactory.TYPE_PRODUCT_A


class ProductB(ProductInterface):
    def __init__(self):
        pass

    def get_type(self):
        return StaticFactory.TYPE_PRODUCT_B

# Creating products
if __name__ == "__main__":
    product_a = StaticFactory.create(StaticFactory.TYPE_PRODUCT_A)
    print product_a.get_type()

    product_b = StaticFactory.create(StaticFactory.TYPE_PRODUCT_B)
    print product_b.get_type()