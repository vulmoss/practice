#!/usr/bin/env python
# coding=utf-8

'''
#author 0xff
'''


from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))


for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
