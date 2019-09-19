#!/usr/bin/env python3
# coding=utf-8

import threading

def hello(name):
    print('current is child thread,thread id is {}'.format(threading.get_ident()))
    print('Hello ' + name)

def main():
    print('current is main threading ,thread id is {}'.format(threading.get_ident()))
    print('----=====================----------------')
    t = threading.Thread(target=hello,args=('world',))
    t.start()
    t.join()
    print('------------------------------')
    print('current is main thread,thread id is {}'.format(threading.get_ident()))

if __name__ == '__main__':
    main()
