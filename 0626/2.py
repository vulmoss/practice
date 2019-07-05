#!/usr/bin/env python
# coding=utf-8
from datetime import datetime

t = 1429417200.0
print(datetime.fromtimestamp(t))


cday = datetime.strptime('2018-06-26 19:07:00','%Y-%m-%d %H:%M:%S')
print(cday)
