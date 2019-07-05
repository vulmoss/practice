#!/usr/bin/env python
# coding=utf-8
import json
d = dict(name = 'Bob',age=200,score=0)
m= json.dumps(d)
print(m)

L = json.loads(m)
print('----------------')
print(L)
