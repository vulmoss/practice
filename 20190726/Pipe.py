#!/usr/bin/env python3
# coding=utf-8

from multiprocessing import Pipe,Process

conn1 ,conn2 = Pipe()

def send():
    data = 'hello world'
    conn1.send(data)
    print('Send data is {}'.format(data))

def recv():
    data = conn2.recv()
    print('recv data is {}'.format(data))
def main():
    Process(target=recv).start()
    Process(target=send).start()

if __name__ == '__main__':
    main()
