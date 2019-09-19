#!/usr/bin/env python3
# coding=utf-8


import time
from multiprocessing import Process,  Value

def func(val):
    for i in range(100):
        time.sleep(0.01)
        val.value += 1

if __name__ == '__main__':
    val = Value('i',0)
    procs = [Process(target=func, args = (val)) for i in range(1)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print(val.value)







'''
 # 多进程无法使用全局变量，multiprocessing 提供的 Value 是一个代理器，可以实现在多进程中共享这个变量
    # val 是一个 Value 对象，它是全局变量，数据类型为 int，初始值为 0
# 创建 10 个任务，备用
  # 启动 10 个子进程来运行 procs 中的任务，对 Value 对象进行 +1 操作
# join 方法使主进程挂起，直至所有子进程运行完毕
'''#
