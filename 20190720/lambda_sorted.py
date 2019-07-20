#!/usr/bin/env python3
# coding=utf-8

pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]

s = sorted(list(map(lambda i:i[0].upper(),pp)),reverse=True)
print(s)



'''
将前面几个高阶函数中作为参数的函数，用 lambda 实现
使用 lambda 和 map 获取 pp 列表中球员的名字的全大写列表并使用 sorted 函数进行降序排序（一行代码实现）
>>> pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]
期望得到如下结果：

['STEPHEN CURRY', 'LEBORN JAMES', 'KEVIN DURANT', 'JAMES HARDEN', 'ANTHONY DAVIS']
'''
