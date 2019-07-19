#!/usr/bin/env python3
# coding=utf-8

from math import pi
def f(a):
    return lambda: a**2*pi

if __name__ == '__main__':
    print(f(2))
    print(f(2)())
