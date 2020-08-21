#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Basket:
    def __init__(self, price, productCount):
        self.price = price
        self.productCount = productCount
    
    def getTotalAmount(self):
        return self.price * self.productCount


if __name__ == "__main__":
    basket = Basket(18.20, 10)
    print(basket.getTotalAmount())