# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:33:09 2019

@author: BSDU ADMIN
"""

#n=int(input("Enter the number"))
#def sum(n):
#    if n==0:
#        return 0
#    else:
#        return(n+sum(n-1))
#if n<0:
#    print("Number is negative, sum is not exit.")
#else:
#    print("Sum of number is",n+sum(n-1))
#    

n=int(input("a"))
def sum(n) :
    if n==0:
        return 0
    else:
        return(n-sum(n-1))
if n<0:
    print("number is positive, sum is not exit.")
else:
    print("sum of number is",n-sum(n-1))      