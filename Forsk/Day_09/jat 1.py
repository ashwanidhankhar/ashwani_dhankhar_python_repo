# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:29:31 2019

@author: BSDU ADMIN
"""


    num = int(input("enter a number: "))
    if num < 0:
    print("enter a positive number")
else:
    sum = 0
    while(num > 0):
     sum = num + sum
     num = num - 1
     print("The sum is", sum)
     