#!/usr/bin/env python
# coding=utf-8
import pickle

f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print(d)

