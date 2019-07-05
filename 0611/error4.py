#!/usr/bin/env python
# coding=utf-8

try:
    foo()
except ValueError  as e:
    print('ValueError',e)
except UnicodeError as  e:
    print('UnicodeError',e)
