#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person:

    # private
    __firtName = None
    __lastName = None
    __email = None

    def __init__(self, firtName, lastName, email):
        self.__firtName = firtName
        self.__lastName = lastName
        self.__email = email
    
    @property
    def fullName(self):
        return "{} {}".format(self.__firtName, self.__lastName)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return "{} {} {}".format(self.__firtName, self.__lastName, self.__email)

class Application:
    def __init__(self):
        pass

    # public
    def Main(self):
        person = Person("İbrahim", "ATAY", "contact@ibrahimatay.com")
        print(person)
        print(person.fullName)

if __name__ == "__main__": 
    app = Application()
    app.Main()