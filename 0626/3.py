#!/usr/bin/env python
# coding=utf-8
import re
from datetime import datetime,timezone,timedelta
def to_timestamp(dt_str,tz_str):
    cday = dateime.strptime(dt_str,'%Y-%m-%d %H:%M:%S') #将str转换成dateime
    tz_info = re.match(r'^UTC([+|-]\d?\d):00$',tz_str) #正则匹配 UTC + 或者 -
    tz_utc_local = timezone(timedelta(hours=int(tz_info.group(1))) #
    cday = cday.replace(tzinfo=tz_utc_local)
    return cday.timestamp()
