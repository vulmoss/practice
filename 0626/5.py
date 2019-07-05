#!/usr/bin/env python
# coding=utf-8
from PIL import Image

im = Image.open('test.jpg')
w, h = im.size

print('Original image size : %sx%s' % (w,h))

im.thumbnail((w//2,h//2))

im.thumbnail((w//3,h//3))

im.save('thumbnaol3.jpg','jpeg')
