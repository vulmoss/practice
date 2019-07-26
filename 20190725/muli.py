#!/usr/bin/env python3
# coding=utf-8

import os
from multiprocessing import Process

def hello(name):
    print('child process:{}'.format(os.getpid()))
    print('Hello ' + name)

def main():
    print('parent process:{}'.format(os.getpid()))
    p = Process(target=hello,args = ('shiyanlou', ))
    print('child process start')
    p.start()
    p.join()  # go on the main
    print('child process stop')
    print('parent process:{}'.format(os.getpid()))

if __name__ == '__main__':
    main()

