#!/usr/bin/env python
# coding=utf-8
import threading

local_school = threading.local()

def process_student(name):
    std = Student(name)
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)

global_dict = {}

def std_thread(name):
    std = Student(name)
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2

def process_student():
    std = local_school.stduent
    print('Hello, %s (in %s)' % (std,threading.current_thread().name))
def process_thread(name):
    local_school.stduent = name
    process_student()

t1 = threading.Thread(target = process_thread,args=('Alice',), name='Thead-1')
t1.start()
t1.join()
