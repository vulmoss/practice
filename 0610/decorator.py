#!/usr/bin/env python
# coding=utf-8
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log1(test):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (test, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def now():
    print('2018-06-10')
f = now
f()
#print(f.__name__)

print('___________________________________________')


@log1('excute')
def now():
    print('today')
