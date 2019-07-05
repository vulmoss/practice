#!/usr/bin/env python
# coding=utf-8
#__author__ = 'h0n9d!'

import sys

l = {}
income = sys.argv[1:]
for str1 in income:
    str2 = str1.split(':')
    for i in str2:
        l[str2[0]] = str2[1]
for key,value in l.items():
    print('ID:{}'.format(key),'NAME:{}'.format(value))
