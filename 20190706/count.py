#!/usr/bin/env python3
# coding=utf-8

class Count(object):
    def __init__(self,func):
        self.func = func
        self.count = 0
    def __call__(self,*args,**kwargs):
        self.count += 1
        return self.func(*args,**kwargs)

@Count
def num_count():
    pass

for i in range(200000):
    num_count()

print(num_count.count)

