#!/usr/bin/env python
# coding=utf-8
#__author__ = 'h0n9d!'

import sys

income = sys.argv[1:]
#print(income)
set1 = set(income)
for i in set1:
    print(i,end='  ')
