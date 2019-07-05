#!/usr/bin/env python
# coding=utf-8
a1 = 3
b1 = 5

def rational_plus(a1, b1, a2, b2):
    num = a1 * b2 + b1 * a2
    den = b1 * b2
    print num,den
    return num,den
a2 ,b2 = rational_plus(a1,b1,7,10)

if __name__ == '__main__':
    rational_plus

rational_plus
