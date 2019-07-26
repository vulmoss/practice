#!/usr/bin/env python3
# coding=utf-8

import time
def io_task():
    time.sleep(1)

def main():
    start_time = time.time()
    print('the time is {}'.format(start_time))
    for i in range(5):
        io_task()
    end_time = time.time()
    print('the time is {:.2f}'.format(end_time-start_time))

if __name__ == '__main__':
    main()

