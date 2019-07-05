#!/usr/bin/env python3
# coding=utf-8

class Animals(object):
    def __init__(self):
        self.__age = 100
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if isinstance(value,int):
            self.__age = value
        else:
            raise ValueError
    @age.deleter
    def age(self):
        print('delete age')
        del self.__age

cat = Animals()
print(cat.age)
print('set the value with age')
cat.age = 50
print(cat.age)

print('deleting operation')
del cat.age
print(cat.age)



'''
@property 装饰器可以将一个方法变成一个属性来使用，通过 @property 装饰器可以获得和修改对象的某一个属性。

使用 @property 装饰器的方法如下：

只有 @property 表示只读
同时有 @property 和 @*.setter 表示可读可写
同时有 @property、@*.setter、和 @*.deleter 表示可读可写可删除
@property 必须定义在 @*.setter 的前面
类必须继承 object 父类，否则 @property 不会生效

这样我们就能以访问属性的方式获取和修改 age 属性了。

从这个简单的例子中我们可以发现 age 由一个函数转变为一个属性，并且通过增加一个
setter 函数的方式来支持 age 的设置。通过 property 和 setter ，可以有效地实现
get_age（获取对象的属性） 和 set_age（设置对象的属性）这两个操作，而不需要直接将
内部的 __age 属性暴露出来，同时可以在 setter 函数中对设置的参数进行检查，避免了
直接对 __age 内部属性进行赋值的潜在风险。
'''
