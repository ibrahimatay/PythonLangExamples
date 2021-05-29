#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class TestClassMethods(unittest.TestCase):
    def test_upper(self):
        name = 'foo'
        nameToUpper = name.upper()
        self.assertEqual(nameToUpper, 'FOO')

if __name__ == '__main__':
    unittest.main()