# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:13:29 2019

@author: BSDU ADMIN
"""

n=int(input("enter the number"))
def sum(n):
     if n==0:
         return 0
     else:
         return(n+sum(n-1))
print(n+sum(n-1))

# =============================================================================
n=int(input("enter the number"))
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(n*fact(n-1))

n=int(input("enter the number"))
def fs(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(fs(n-1)+fs(n-2))
for i in range(n):
    print(fs(i))