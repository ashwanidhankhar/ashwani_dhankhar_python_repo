# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:26:52 2019

@author: BSDU ADMIN
"""
n=int(input("enter the number"))
def fs(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fs(n-1+fs(n-2))
for i in range(n):
    print(i)