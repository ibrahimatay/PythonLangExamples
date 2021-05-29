#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = 1
y = 10

while x < y:
    print(x)
    x = x + 1

print("While is done.")
print()

"""
For loop with file read
"""
file = open("lines.txt")
for line in file.readlines():
    print(line, end="")

print()

"""
For loop with range
"""

for index in range(1,10):
    print(index)

print()

for index in range(1, 10, 2):
    print(index)