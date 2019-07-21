#!/usr/bin/env python3
# coding=utf-8


class Test():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        self.a += 1
        if self.a > self.b:
            raise StopIteration
        return self.a

test = Test(0,100)

print(next(test))
print('--------------')
print(next(test))
