#!/usr/bin/env python
# coding=utf-8
a=input()
if int(a)<0:
    a=a[1:]
    b=-int(a[::-1])
else:
    b=int(a[::-1])


print(b)
