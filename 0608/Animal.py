#!/usr/bin/env python
# coding=utf-8

class Animal():
    def run(self):
        print('the Animal is running')

class Dog(Animal):
    def run(self):
        print('thd Dog is running')
    def eat(self):
        print('The dog eat meal')
class Cat(Animal):
    def run(self):
        print('the cat is running')
    def eat(self):
        print('the cat eat milk')

Animal().run()
