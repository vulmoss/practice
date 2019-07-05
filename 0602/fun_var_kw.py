#!/usr/bin/env python
# coding=utf-8
def fun_var_kw(farg, **kw):
    print("args:",farg)
    for key in kw:
        print("another keyword arg: %s" %kw[key])

fun_var_kw(1,"two",3)
