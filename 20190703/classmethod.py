#!/usr/bin/env python3
# coding=utf-8

class A(object):
    bar = 1
    def func1(self):
        print('foo')
    @classmethod
    def func2(cls):
        print('func2')
        print(cls().bar)
        print(cls().func1())


A.func2()
