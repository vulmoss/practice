#!/usr/bin/env python3
# coding=utf-8

from multiprocessing import Process
import time
def io_task():
    time.sleep(1)

def main():
    start_time = time.time()
    print('the time is {}'.format(start_time))
    '''
    for i in range(5):
        io_task()
    '''
    process_list = []
    for i in range(5):
        process_list.append(Process(target=io_task))
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()
    end_time = time.time()
    print('the time is {:.2f}'.format(end_time-start_time))

if __name__ == '__main__':
    main()

