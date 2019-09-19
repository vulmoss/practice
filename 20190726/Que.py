#!/usr/bin/env python3
# coding=utf-8

from multiprocessing import Process,Queue

queue = Queue()

def f1(s):
    data = 'hello world'
    s.put(data)
    print('send the data is {}'.format(data))

def f2(r):
    data = r.get()
    print('recv the data is {}'.format(data))

def main():
    Process(target=f1,args=(queue,)).start()
    Process(target=f2,args=(queue,)).start()

if __name__ == '__main__':
    main()
