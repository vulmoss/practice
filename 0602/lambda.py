#!/usr/bin/env python
# coding=utf-8
print(map(lambda x : x * x,[1,2,3,4,5,6,7,8,9]))


"""
通过结果可以看出，匿名函数lambda x : x* x实际上就是

def f(x):
    return x * x
"""
