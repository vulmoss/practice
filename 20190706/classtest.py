#!/usr/bin/env python3
# coding=utf-8

class Animals(object):
    def __init__(self):
        self.__age = 100
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if isinstance(value,int):
            self.__age = value
        else:
            raise ValueError
    @age.deleter
    def age(self):
        print('delete age')
        del self.__age

cat = Animals()
print(cat.age)
print('set the value with age')
cat.age = 50
print(cat.age)

print('deleting operation')
del cat.age
print(cat.age)
