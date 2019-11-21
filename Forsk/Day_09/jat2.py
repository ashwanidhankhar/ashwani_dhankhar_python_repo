# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:44:15 2019

@author: BSDU ADMIN
"""

n=int(input("enter number"))
a=0
b=1
i=1
while i<n:
    c=a+b
    b=a
    a=c
    i=i+1
    print(c)
    