#!/usr/bin/env python3
# coding=utf-8

testlist = ['Linux', 'Java', 'Python', 'DevOps', 'Go']

it = iter(testlist)
print("Loop Start...")
while True:
    try:
        course = next(it)
        print(course)
    except StopIteration :
        break

print("Loop End")