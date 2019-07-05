#!/usr/bin/env python
# coding=utf-8



def log(func):
    def wrapper(*arg,**kw):
        print('call %s():' % func.__name__)
        return func(*arg,**kw)
    return wrapper


@log
def now():
    print('2018-06-02')



f = now
f()
