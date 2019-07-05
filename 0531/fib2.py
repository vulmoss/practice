#!/usr/bin/env python
# coding=utf-8
def fib(n):
    f1 = f2 = 1
    for k in range(1,n):
        f1, f2 = f2 ,f2 + f1
        return f2
