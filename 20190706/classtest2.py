#!/usr/bin/env python3
# coding=utf-8

class NewUser(object):
    def __init__(self,id,name):
        self.id = id
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value) >3:
            self._name = value
        else:
            self._name = 'ERROR'
if __name__ == '__main__':
    user1 = NewUser(101, 'Jack')
    user1.name = 'Lou'
    user1.name = 'Jackie'
    user2 = NewUser(102, 'Louplus')
    print(user1.name)
    print(user2.name)
