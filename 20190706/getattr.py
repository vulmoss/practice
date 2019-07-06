#!/usr/bin/env python3
# coding=utf-8

class Animals(object):
    def __init__(self,name,gerder):
        self.name = name
        self.gerder = gerder
    def __getattribute__(self,attr):
        print('use the __getattribute__,get the {}'.format(attr))
        if attr in ('name','gerder'):
            return object.__getattribute__(self,attr)
        else:
            print('use the getattr')
            return object.__getattr__(self,attr)
    def __getattr__(self,attr):
        print('start to use getattr')
        if attr == 'age':
            return 100
        else :
            return '__getattr__ dont found '
dog = Animals('wangcai','male')
print(dog.name)
print('-----------1-------')
print(dog.gerder)
print('------------2---')
print(dog.age)
print('-------------3-----')
print(dog.address)


在 Python 类中，当访问实例对象属性的时候，其实默认会调用 __getattribute__ 方法，如果没有该属性就会报 AttributeError 错误，
这个时候可以考虑使用 __getattr__ 方法进行自定义。两者的区别主要如下：

区别	__getattribute__(self,attr)	__getattr__
调用时间	调用实例对象属性时触发(无论属性是否存在)	获取不存在的实例对象属性时触发
参数	self,attr(实例对象属性)	self,attr(实例对象属性)
返回值	必须有	必须有
作用	控制访问权限	访问不存在属性时进行自定义
需要注意的是： __getattribute__ 方法会比 __getattr__ 方法优先调用，如果调用__getattribute__ 方法有返回值就不会再调用 __getattr__ 方法了。
