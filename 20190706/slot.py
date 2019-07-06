#!/usr/bin/env python3
# coding=utf-8

由于 Python 是动态语言，因此定义一个实例对象后可以绑定任意的属性，如果需要限制绑定属性类别，可以使用 __slots__ 变量
，可以绑定的属性值以元组的形式赋予给它。需要注意的是：__slots__中定义的属性只在定义的类中有效，在被继承的子类中是无效的，如果想要在子类中限制属性则需要重新定义。

class Animals(object):
    __slots__ = ('name','age')
