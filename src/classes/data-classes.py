#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python 3.7 

PEP 557 -- Data Classes
https://www.python.org/dev/peps/pep-0557/

dataclasses — Data Classes
https://docs.python.org/3/library/dataclasses.html

Socure code
https://github.com/python/mypy/blob/master/mypy/plugins/dataclasses.py

Raymond Hettinger - Dataclasses: The code generator to end all code generators - PyCon 2018
https://www.youtube.com/watch?v=T-TwcmT6Rcw
"""

from dataclasses import dataclass
from typing import List

@dataclass(init=True, repr=True, eq=True)
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name =''
    unit_price = 0.0
    quantity_on_hand = 0

    def get_total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

@dataclass
class Inventories:
    items = List[InventoryItem]

item01 = InventoryItem("Book", 12.5, 5)
item02 = InventoryItem("Notebook", 7.6, 2)
item03 = InventoryItem("Paper", 2.5, 10)

items = [
    item01,
    item02,
    item03
]

InventoryCollections01 = Inventories([items])

for item in InventoryCollections01.items:
    print(item)

InventoryCollections02 = Inventories([])

InventoryCollections02.items.append(item01)
InventoryCollections02.items.append(item02)
InventoryCollections02.items.append(item03)

for item in InventoryCollections02.items:
    print(item)