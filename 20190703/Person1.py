#!/usr/bin/env python3
# coding=utf-8

class A:
    def test(self):
        print('-----testA------')
class B:
    def test(self):
        print('------testB---------')



class Person(A,B):
    pass

person = Person()
person.test()
print(Person.mro())
