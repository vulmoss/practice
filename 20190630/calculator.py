#!/usr/bin/env python3
# coding=utf-8

import sys

'''
个税计算公式：
应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
纳税 = 应纳税所得额 × 税率 － 速算扣除数
'''
output_dict = {}
def fenxi(str):
    for arg in sys.argv[1:]:
        str2 = arg.split(':')
        output_dict[str2[0]] = str2[1]
    return output_dict
def naShui(gz):
    re_gz = gz - gz * 0.165 -3500
    if re_gz <=1500:
        result = re_gz * 0.03
    elif 1500 < re_gz <= 4500:
        result = re_gz * 0.1 - 105
    elif 4500 < re_gz <= 9000:
        result = re_gz * 0.2 - 555
    elif 9000 < re_gz <= 35000:
        result = re_gz * 0.25 - 1005
    elif 35000 < re_gz <=55000:
        result = re_gz * 0.3 - 2755
    elif 55000 < re_gz <= 80000:
        result = re_gz * 0.35 - 5505
    else :
        result = re_gz * 0.45 - 13505
    return result
def output(output_dict):
    for key,value in output_dict.items():
        print(key,value)

if __name__ == '__main__':
    m = sys.argv
    fenxi(m)
    for key,value in output_dict.items():
        output_dict[key] = naShui(int(value))
    output(output_dict)
