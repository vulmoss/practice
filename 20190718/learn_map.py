#!/usr/bin/env python3
# coding=utf-8

pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]

def a(i):
    return i[0].lower()

print(list(map(a,pp)))


'''
map(a, b)
# a 是函数，用来处理 b 参数
# b 是可迭代对象

'''
