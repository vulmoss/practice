#!/usr/bin/env python3
# coding=utf-8

import threading

def hello(name):
    print('current child thread:{}'.format(threading.get_ident()))
    print('Hello ' + name)
def main():
    print('current is main thread ID :{}'.format(threading.get_ident()))
    print('-------------------')
    t = threading.Thread(target=hello,args=('shiyanlou',))
    t.start()
    t.join()
    print('--------------------------')
    print('current is main thread ID:{}'.format(threading.get_ident()))

if __name__ == '__main__':
    main()
