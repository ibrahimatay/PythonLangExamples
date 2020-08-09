#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Case 1
# print ("First Module's name: {}".format(__name__))

def main():
    # pass
    # Case 2
    # print ("First Module's name: {}".format(__name__))
    # Case 3
    # print(sys.argv)
    # python first_module.py test aaa bb
    # ['first_module.py', 'test', 'aaa', 'bb']
    if sys.argv[1] == "Hello":
        print("Welcome")
    else:
        print("access denied")


if __name__ == "__main__":
    main()

