#!/usr/bin/env python3
# coding=utf-8

import os, time, random
from multiprocessing import Pool

def task(name):
    print('task {} begin running,the process id is :{}'.format(name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task {} end , taken time is {:.2f}s'.format(name,(end - start)))

def main():
    print('current is main process,process id is {}'.format(os.getpid()))
    print('--------------------------------------------')
    p = Pool()
    for i in range(1,7):
        p.apply_async(task,args = (i,))
    p.close()
    print('starting run child process')
    p.join()
    print('----------------------------------------------')
    print('all child process finish,current is main process,process id {}'.format(os.getpid()))

if __name__ == '__main__':
    main()
