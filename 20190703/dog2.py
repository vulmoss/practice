#!/usr/bin/env python3
# coding=utf-8

class Animal(object):
    owner = 'ximin'
    __owner_age = 32
    def __init__(self,name):
        self._name = name
    @classmethod
    def get_owner(cls):
        return cls.owner
    @classmethod
    def set_owner(cls,name):
        cls.owner = name
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        print(self.get_name() + 'is making wang wang wang')

class Cat(Animal):
    def make_sound(self):
        print(self.get_name() + 'is making mew mew mew')


dog = Dog('wangcai')
cat = Cat('Kitty')
print('00000000000000000000')
animals = Animal('jj')
print(animals.owner)
print('111111111111111111111')
dog.make_sound()
cat.make_sound()
print('---------------------')
dog._name
print('**********************')

print(Animal.owner)
print(Cat.owner)
print('!!!!!!!!!!!!!!!!!!!!!!!!!!')
print(Animal.get_owner())


print('22222222222222222')
animals.set_owner('mm')
print(Animal.get_owner())
