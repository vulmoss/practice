#!/usr/bin/env python
# coding=utf-8
#author 0xff
import random

number = random.randint(1,100)
guess = 0
while guess < 5:
    game = raw_input('plesase input the you guess the num:')
    guess += 1
    if not game.isdigit():
        print "please input the interger"
    elif int(game) <0 or int(game) >100:
        print "please input the number between 1 and 100"
    else:
        if number ==int(game):
            print "confguration you are right"
            break
        elif number > int(game):
            print "the number is', number ,'you are samll"
        elif number < int(game):
            print "the number is', number,'you are bigger"
        else:
            print "I dnot kown "
