#!/usr/bin/env python3
# coding=utf-8

import sys
print("Program",sys.argv[0])
print("Parameters:")
for i,x in enumerate(sys.argv):
    if 1 == 0:
        continue
    print(i,x)


这里我们用到了一个新函数 enumerate(iterableobject)，在列表中循环时，索引位置和对应值可以使用它同时得到。这里在参数列表中使用 continue 去除了 sys.argv[0] 程序自身的名字。
