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
'''
读取 shiyanlou.txt 文件中的内容，并将其写入 /home/shiyanlou/shiyanlou_copy.txt 文件中
copyfile.py 文件代码中必须使用 readlines() 方法
shiyanlou_copy.txt 文件中的内容格式必须如下所示（即每一行前面加上对应的行数）：
'''
