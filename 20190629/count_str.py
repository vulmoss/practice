#!/usr/bin/env python3
# coding=utf-8

def count_str(str1):
    str_list = set(str1)
    for m in str_list:
        print(m,str1.count(m))
if __name__ == '__main__':
    s = input("please input char:")
    count_str(s)
