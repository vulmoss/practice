#!/usr/bin/env python3
# coding=utf-8

import sys

output_dict = {}

def fenxi(str):
    for arg in sys.argv[1:]:
        str2 = arg.split(':')
        output_dict[str2[0]] = str2[1]
    return output_dict

def output(output_dict):
    for key in output_dict:
        print('ID :{}'.format(key), 'Name : {}'.format(output_dict[key]))


if __name__ == '__main__':
    m = fenxi(sys.argv)
    output(m)

