#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

people = [
    {'Country': 'Turkey', 'City':'Istanbul'},
    {'Country': 'German', 'City':'Berlin'},
    {'Country': 'UK', 'City':'London'},
] 

peopleOfJson = json.dumps(people, indent=4, sort_keys=True)

print(peopleOfJson)

"""
[
    {
        "City": "Istanbul",
        "Country": "Turkey"
    },
    {
        "City": "Berlin",
        "Country": "German"
    },
    {
        "City": "London",
        "Country": "UK"
    }
]

"""

values = json.loads(peopleOfJson)

print(values[0]["Country"]) # Turkey