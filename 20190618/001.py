#!/usr/bin/env python
# coding=utf-8
#__author__ ='h0n9d!'

filename = input('please input the file path: ')
print('\n',end="")
try:
    f = open(filename)
    print(f.read())
    f.close()
except FileNotFoundError as err:
    print("Error,{0}".format(err))

