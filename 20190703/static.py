#!/usr/bin/env python3
# coding=utf-8

class Animals(object):
    owner = 'jack'
    def __init__(self,name):
        self._name = name
    @staticmethod
    def order_animals_food():
        print('fucking')
        print('OK')
print(Animals.order_animals_food())
