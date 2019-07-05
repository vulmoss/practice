#!/usr/bin/env python
# coding=utf-8
n = 2
for i in range(n):
    for j in range(n):
        x = 0.0
        for k in range(n):
            x = x + m1[i][k] * m2[k][j]
            m[i][j] = x
