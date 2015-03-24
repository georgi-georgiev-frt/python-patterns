#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Simple factory pattern


# Entities

class VehicleInterface:
    def drive_to(self):
        raise NotImplemented


class Car(VehicleInterface):
    def __init__(self):
        pass

    def drive_to(self):
        pass

    def __str__(self):
        return 'car'


class Motorcycle(VehicleInterface):
    def __init__(self):
        pass

    def drive_to(self):
        pass

    def __str__(self):
        return 'motorcycle'

# Factory


class VehicleFactory:
    TYPE_CAR = 'car'
    TYPE_MOTORCYCLE = 'motorcycle'

    def __init__(self):
        self._type_list = {
            self.TYPE_CAR: Car,
            self.TYPE_MOTORCYCLE: Motorcycle
        }

    def create(self, type):
        if type not in self._type_list:
            raise ValueError('Unsupported type {}'.format(type))
        else:
            return self._type_list[type]()

if __name__ == "__main__":
    factory = VehicleFactory()
    car = factory.create(VehicleFactory.TYPE_CAR)
    bike = factory.create(VehicleFactory.TYPE_MOTORCYCLE)

    print car, bike


### OUTPUT ###
# car motorcycle
