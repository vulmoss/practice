#!/usr/bin/env python3
# coding=utf-8

def char_count(str1):
    countdict = {} #定义一个字典
    for str2 in str1: #每一个字符
        c = countdict.get(str1) #字符是key，c是value ，第一个是None
        if c is None:  #如果是第一个的话
            countdict[str2] = 1 #c这个value定义为1
        else:
            countdict[str2] += 1 #不是nonde的 value加1
        print('ID is {}'.format(countdict.key()),'count is : {}'.countdict.value())

if __name__ == '__main__':
    s = input('please input char:')
    char_count(s)
