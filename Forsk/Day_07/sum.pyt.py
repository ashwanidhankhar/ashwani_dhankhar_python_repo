# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:34:36 2019

@author: BSDU ADMIN
"""

def recur_sum(n):
    """function to return the sum
    of natural numbers using recursion"""
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)
    
    # change this value for a different result
    #num = 16
    
    # uncomment to take input from the user 
    num = int(input("enter a number:"))
    
    if num < 0:
        print("enter a positive number")
    else:
        print("the sum is",recur_sum(num))
        
        
        
        