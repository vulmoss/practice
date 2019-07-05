#!/usr/bin/env python3
# coding=utf-8

class A:
    def __init__(self,name):
        self.name = 'xiaoming'
    def testA(self):
        print('TEsta---------------------')
class B:
    def __init__(self,age):
        self.age = 9
    def testB(self):
        print('TEstB-----------')

class Person(A,B):
    def __init__(self,name,age):
        A.__init__(self,name)
        B.__init__(self,age)
    def testP(self):
        print('-----------testPersion--')

person = Person('linilin',12)
print(person.name)
print(person.age)
person.testA()
person.testB()
person.testP()
