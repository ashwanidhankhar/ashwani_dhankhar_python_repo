# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 03:56:50 2019

@author: ashwa
"""

#First
a=0
b=1


for i in range(14):
    c=a+b
    a=b
    b=c
    print(c)
    
    
 #Second   

arr=[1,2,3,4,5,6,7]
x=2

if x in arr:
    print(True," It is present a t index number ",arr.index(x))
else:
    print(False)


#third

try:
    from googlesearch import search
except ImportError:
    print("No module named google found")
    
#to search
    
query= "Bhartiya Skill Development University"

for i in search(query,tld="co,in"):
    print(i)