#!/usr/bin/env python3
# coding=utf-8

class UserData:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'ID : {}, Nmae:{}'.format(self.id,self.name)

if __name__ == '__main__':
    user1 = UserData(101,'jack')
    user2 = UserData(102,'Louplus')
    print(user1)
    print(user2)
