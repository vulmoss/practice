#!/usr/bin/env python
# coding=utf-8
def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    return r
def bar():
    r = foo()
    if r == (-1):
        print('Error')
    else:
        pass





try :
    print('try')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('error....')
print('END')
