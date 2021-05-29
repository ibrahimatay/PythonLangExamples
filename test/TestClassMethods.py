#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class TestClassMethods(unittest.TestCase):
  
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()