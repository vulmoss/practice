#!/usr/bin/env python3
# coding=utf-8

class Text(object):
    def __init__(self,data=0):
        self.data = data
    def __iter__(self):
        return self
    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data += 1
            return self.data


for i in Text():
    print(i)



使用 __iter__方法就可以让类成为一个可迭代对象，如果使用 for 循环遍历类对象还需要在类中定义__next__ 方法，在__next__
方法中可以定义取值的规则，当超出取值规则会抛出 StopIteration 异常从而退出当前循环。
