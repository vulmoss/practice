#!/usr/bin/env python
# coding=utf-8
class Screen(object):
    @property
    def widht(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be an integer')
        elif value < 0:
            raise ValueError('must be than 0')
        else:
            self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not isinstance(value, int):
            raise ValueError('height is must be integer')
        elif value < 0:
            raise ValueError('must be than 0')
        else:
            self._height = value
    @property
    def resolution(self):


