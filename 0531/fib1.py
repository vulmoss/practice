#!/usr/bin/env python
# coding=utf-8
def fib(n):
    in n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


