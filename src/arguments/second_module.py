#!/usr/bin/env python
# -*- coding: utf-8 -*-

import first_module

print ("Second Module's name: {}".format(__name__))

"""
Case 1
First Module's name: first_module
Second Module's name: __main__

Case 2
Second Module's name: __main__
"""