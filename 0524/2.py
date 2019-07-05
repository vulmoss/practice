#!/usr/bin/env python
# coding=utf-8

def fn(x,y):
    return x * 10 + y
print reduce(fn,[1,2,3,4,5,6])


def char2num(s):
    return {'0':0,'1':1}[s]
print reduce(fn,max(char2num,'123456'))

