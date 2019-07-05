#!/usr/bin/env python3
# coding=utf-8

import sys
from collections import namedtuple

IncomeTaxItem = namedtuple('IncomeTaxItem',['start_point','income_rate','num1'])
bx = {'ylbx':0.08,'yilbx':0.02,'sy':0.005,'gjj':0.06}
IncomeTaxGroup = [IncomeTaxItem(80000,0.45,13505),
                  IncomeTaxItem(55000,0.35,5505),
                  IncomeTaxItem(35000,0.3,2755),
                  IncomeTaxItem(9000,0.25,1005),
                  IncomeTaxItem(4500,0.2,555),
                  IncomeTaxItem(1500,0.1,105),
                  IncomeTaxItem(0,0.03,0)]
startZ = 3500

def calc(income):
    bxf = income * int(sum(bx.values()))
    real_income = income - bxf
    will_tax = real_income - startZ
    if startZ <= 0 :
        return '{:.2f}'.format(real_income)
    for item in IncomeTaxGroup:
        if will_tax > item.start_point:
            tax = will_tax * item.income_rate - item.num1
            return '{:.2f}'.format(real_income - tax)

output_dict = {}
def fenxi(str):
    for arg in sys.argv[1:]:
        str2 = arg.split(':')
        output_dict[str2[0]] = str2[1]
    return output_dict

def main():
    fenxi(sys.argv)
    for key,value in output_dict.items():
        output_dict[key] = calc(int(value))
        print('ID :{}'.format(key),'cala : {}'.format(value))

if __name__ == '__main__':
    main()

