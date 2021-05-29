#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    file = open("xyz.txt")
except IOError as e:
    print("Error message: {}".format(e))
