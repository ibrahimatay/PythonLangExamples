#!/usr/bin/env python
# -*- coding: utf-8 -*-

numbers = []
numbers = [2,3,5,7,11,13]

print(numbers)

print("number varible type is {}".format(type(numbers)))
print("number list item count is {}".format(len(numbers)))


everyTypes = [23,4,1923, "Turkey"]
print(everyTypes)

print("everyTypes varible type is {}".format(type(everyTypes)))
print("1 index item length is {} in everyTypes list".format(len(everyTypes[3]))) # Turkey word length is 6 in everyTypes list

print()
print("".center(15,"*"))
print()

newList = everyTypes + numbers
print(newList)

for item in newList:
    print(item)

print()
print("".center(15,"*"))
print()

for item in range(5):
    print(item)


print()
print("".center(15,"*"))
print()

index  = 0
while index < 10:
    print(index)
    index = index + 1

print()
print("List Append".center(15,"*"))
print()


numbers.append(17)
numbers.append(19)
numbers.append(23)
numbers.append(29)
numbers.append(31)

print(numbers)

print()
print("List Insert".center(15,"*"))
print()

print(numbers)
numbers.insert(2,14)
print(numbers)

print()
print("List Index".center(15,"*"))
print()

print(numbers.index(31))

print()
print("List Remove".center(15,"*"))
print()

print(numbers)
numbers.remove(23)
print(numbers)

print()
print("List Sort".center(15,"*"))
print()

print(numbers)
numbers.sort()
print(numbers)

print()
print("List Reverse".center(15,"*"))
print()

print(numbers)
numbers.reverse()
print(numbers)
