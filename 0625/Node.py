#!/usr/bin/env python
# coding=utf-8
class Node(object):
    def __init__(self,initdata):
        self.data = initdata
        self.next =Node
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
class unOrderedList():
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == Node









tmp = Node(33)
myList = unOrderedList()
