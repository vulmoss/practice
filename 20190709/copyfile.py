#!/usr/bin/env python3
# coding=utf-8

src = 'shiyanlou.txt'
target = 'shiyanlou_copy.txt'
def copyfile(src,target):
    with open(src,'r') as r:
        with open(target,'w') as w:
            count = 0
            for line in r.readlines():
                count += 1
                a = '{} {}'.format(count,line)
                w.write(a)
def main():
    copyfile(src,target)

if __name__ == '__main__':
    main()

