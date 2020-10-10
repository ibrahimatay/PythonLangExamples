Enum#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PEP 435 -- Adding an Enum type to the Python standard library
https://www.python.org/dev/peps/pep-0435/

Support for enumerations
https://docs.python.org/3.4/library/enum.html

ImportError: cannot import name 'IntEnum'
https://stackoverflow.com/questions/44666136/importerror-cannot-import-name-intenum

# sudo pip3 install -U enum34 # python3
# sudo pip2 install -U enum # python2
"""

from enum import Enum 

class Animal(Enum):
    Ant = 1
    Cat = 2
    Dog = 3

print(Animal.Ant) # <Animal.DOG: 1>

myAnimal = Animal.Ant

Numbers = Enum(ONE=1, TWO=2, THREE=3)
print(Numbers.ONE) 
print(Numbers.ONE == 1)
