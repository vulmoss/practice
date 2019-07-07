#!/usr/bin/env python3
# coding=utf-8

import sys

def copy_file(src,dst):
    with open(src,'r') as s:
        with open(dst,'w') as d:
            d.write(s.read())

def main():
    if len(sys.argv) == 3:
        copy_file(sys.argv[1],sys.argv[2])
    else:
        print("parameter error")
        print("please input src and dst")
        sys.exit(-1)
    sys.exit()

if __name__ == '__main__':
    main()
