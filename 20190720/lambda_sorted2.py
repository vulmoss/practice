#!/usr/bin/env python3
# coding=utf-8


#!/usr/bin/env python3

list1 = [('Shi',100), ('Yan', 75), ('Lou', 200), ('Plus', 80)]

sortedlist = sorted(list1, key=lambda i:i[1])

print(sortedlist)


'''

列表 list1 为一个二元组的列表，我们需要使用每个二元组的第二个元素进行比较排序，从小到大排列。

sorted 为内置的排序函数，其中需要将列表作为参数传递给 sorted，key 参数表示指定排序的关键字，可以理解为告诉 sorted 函数该怎么排序。在这段代码中，我们需要用到 Lambda 表达式来处理，即提取每个二元组中的第二个元素来进行排序。

使用 Lambda 表达式修复上面程序的 TODO 部分，然后执行 python3 /home/shiyanlou/lambdatest.py，输出的结果应该是：

[('Yan', 75), ('Plus', 80), ('Shi', 100), ('Lou', 200)]
'''
