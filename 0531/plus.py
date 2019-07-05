#!/usr/bin/env python
# coding=utf-8
r1 = (3,5)
r2 = (7,10)

def rational_plus(r1,r2):
    num = r1[0]*r2[1] + r2[0]*r1[1]
    den = r1[1]*r2[1]
    return num, den
r3 = rational_plus(r1,r2)
print r3
