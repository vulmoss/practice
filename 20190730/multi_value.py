#!/usr/bin/env python3
# coding=utf-8

import time
from multiprocessing import Process, Value,Lock


def func(val,lock):
    for i in range(50):
        time.sleep(0.1)
        with lock:
            val.value += 1

if __name__ == '__main__':
    v = Value('i',0)
    lock = Lock()
    procs = [Process(target=func, args=(v,lock)) for i in range(10)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print(v.value)


'''每次进行加 1 操作时候，为 i 加一把锁，也就是说当前的进程在操作 i 时，其它进程
不能操作它。multiprocessing 模块的 Lock 类封装的锁操作，使用 acquire() 方法获取
锁，release() 方法释放锁.
# with lock 语句是对下面语句的简写：
        lock.acquire()
        val.value += 1
        lock.release()
        # 为 val 变量加锁，结果就是任何时刻只有一个进程可以获得 lock 锁
        # 自然 val 的值就不会同时被多个进程改变


'''
