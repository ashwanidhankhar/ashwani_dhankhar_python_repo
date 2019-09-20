# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:49:04 2019

@author: ashwa
"""

"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""

#input number to calculate foactorial for the following
num=int(input("Enter the number   :"))
num1=num
fact=1

#Loop for the pattern of factorial 
while True:
    fact=fact*num
    num=num-1
    if num <= 1:
        break
#printing the output
print("The factorial of {} is {}".format(num1,fact))




#using library

import math

#using library function to find factorial for the following
fact1=math.factorial(num1)

print(fact1)