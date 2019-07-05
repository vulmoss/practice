#!/usr/bin/env python3
# coding=utf-8


import sys
from collections import namedtuple #定义元组


IncomeTaxQuickLookupItem = namedtuple(
    'IncomeTaxQuickLookupItem',
    ['start_point', 'tax_rate', 'quick_subtractor']
) #namedtuple是一个函数，定义tuple

INCOME_TAX_START_POINT = 3500 #起征点

INCOME_TAX_QUICK_LOOKUP_TABLE = [
    IncomeTaxQuickLookupItem(80000, 0.45, 13505),
    IncomeTaxQuickLookupItem(55000, 0.35, 5505),
    IncomeTaxQuickLookupItem(35000, 0.30, 2755),
    IncomeTaxQuickLookupItem(9000, 0.25, 1005),
    IncomeTaxQuickLookupItem(4500, 0.2, 555),
    IncomeTaxQuickLookupItem(1500, 0.1, 105),
    IncomeTaxQuickLookupItem(0, 0.03, 0)
] #一个列表，列表的顺序不能错，稍后使用的时候是从头开始计算的

SOCIAL_INSURANCE_MONEY_RATE = {
    'endowment_insurance': 0.08,
    'medical_insurance': 0.02,
    'unemployment_insurance': 0.005,
    'employment_injury_insurance': 0,
    'maternity_insurance': 0,
    'public_accumulation_funds': 0.06
}
#好处是如果加入了其他的利率什么的，可以直接添加进字典中

def calc_income_tax_and_remain(income):
    social_insurance_money = income * sum(SOCIAL_INSURANCE_MONEY_RATE.values())
    real_income = income - social_insurance_money
    taxable_part = real_income - INCOME_TAX_START_POINT
    if taxable_part <= 0: #不够起征点
        return '0.00', '{:.2f}'.format(real_income)
    for item in INCOME_TAX_QUICK_LOOKUP_TABLE: #从头开始不断循环列表中的元组
        if taxable_part > item.start_point: #namedtuple中定义的属性
            tax = taxable_part * item.tax_rate - item.quick_subtractor
            return '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)


def main():
    for item in sys.argv[1:]:
        employee_id, income_string = item.split(':')
        try:
            income = int(income_string)
        except ValueError:
            print('Parameter Error')
            continue
        _, remain = calc_income_tax_and_remain(income)
        print('{}:{}'.format(employee_id, remain))


if __name__ == '__main__':
    main()
