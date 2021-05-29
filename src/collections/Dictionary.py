#!/usr/bin/env python
# -*- coding: utf-8 -*-

address = {
    "Country":"Turkey",
    "City": "Istanbul",
    "District":"Bahçelievler"
}

print(address)
print(type(address))
print("address dictionary length is {}".format(len(address))) # address dictionary length is 3

print("Your country is {}".format(address["Country"])) # Your country is Turkey
print("Your city is {}".format(address["City"])) # Your city is Istanbul
print("Your district is {}".format(address.get("District"))) # Your district is Bahçelievler

print()
print("Removing attribute in address".center(15,"*"))
print()

print(address)
del address["District"]
print(address)

"""
{'Country': 'Turkey', 'City': 'Istanbul', 'District': 'Bahçelievler'}
{'Country': 'Turkey', 'City': 'Istanbul'}
"""

print()
print("Clean".center(15,"*"))
print()

print(address)
address.clear()
print(address)

"""
{'Country': 'Turkey', 'City': 'Istanbul'}
{}
"""

address = {
    "Country":"Turkey",
    "City": "Istanbul",
    "District":"Bahçelievler"
}

print()
print("all".center(15,"*")) 
print()

print(all(address)) # True

print()
print("any".center(15,"*"))
print()

print(any(address)) # True
address.clear()
print(any(address)) # False

address = {
    "Country":"Turkey",
    "City": "Istanbul",
    "District":"Bahçelievler"
}

