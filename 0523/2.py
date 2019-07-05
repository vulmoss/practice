#!/usr/bin/env python
# coding=utf-8
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 2
    print 'step 3'
    yield 6

o = odd()
print o.next()
