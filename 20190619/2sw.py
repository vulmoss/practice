#!/usr/bin/env python
# coding=utf-8
#__author__ = 'h0n9d!'
'''
应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
纳税 = 应纳税所得额 × 税率 － 速算扣除数
'''
import sys

result1 = 0
gz = int(sys.argv[1])
if gz < 3500:
    print('you are so poor')
elif gz >=3500:
    ss = gz - 3500
    print('you need to 缴纳保护费')
    if 3500 <= gz < 5000:
        result1 = ss * 0.03
        print('feiyongis {} yuan'.format(result1))
    elif 5000 <= gz < 8000:
        result1 = ss  * 0.1 - 105
        print('feiyongis {} yuan'.format(result1))
    elif 8000 <= gz < 18000:
        result1 = ss  * 0.25 - 1005
        print('feiyongis {} yuan'.format(result1))
    else :
        result1 = ss  * 0.5
        print('feiyongis {} yuan'.format(result1))
        print('罚死你')
#Yns =
#Ns =
