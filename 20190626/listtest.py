#!/usr/bin/env python
# coding=utf-8
#__author__ = 'h0n9d!'

import sys

c = sys.argv[1:]
m = []
n = []
for i in c:
    if len(i) <=3 :
        m.append(i)
    elif len(i) > 3 :
        n.append(i)

k = len(m)
for l in m:
    k -= 1
    if k == 0:
        print('\n')
    print(l,end=' ')

for h in n:
    print(h,end='  ')
