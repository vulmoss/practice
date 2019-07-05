#!/usr/bin/env python
# coding=utf-8
import pickle
d = dict(name = 'Bob',age=20,score=88)
pickle.dumps(d)
f = open('dump.txt','ab')
pickle.dump(d,f)
f.close()

