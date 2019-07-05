#!/usr/bin/env python
# coding=utf-8

def foo(s):
    print(10/int(s))
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error',e)
    finally:
        print('finally...')

if __name__ == '__main()__':
    foo(0)
