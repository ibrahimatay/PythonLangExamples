#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = 1
y = 3

if x < y:
    print('x ({}) is less than y ({})'.format(x, y))
elif y < x:
    print('y ({}) is not less than x ({})'.format(x, y))
else:
    print("x is equal to y")