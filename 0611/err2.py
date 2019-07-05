#!/usr/bin/env python
# coding=utf-8
try:
    print('try....')
    r = 10 / int('a')
    print('result.....')
except ValueError as e:
    print('ValueError')
except ZeroDivisionError as e:
    print('ZeroDivisionError')
finally:
    print('finally...')
print('END')
