# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:44:31 2019

@author: ashwa
"""

"""

Code Challenge
  Name: 
    Simpsons Phone Book
  Filename: 
    simpsons.py
  Problem Statement:
    There are some people with the surname Neu. 
    We are looking for a Neu, but we don't know the first name, 
    we just know that it starts with a J. 
    Let's write a Python script, which finds all the lines of the phone book, 
    which contain a person with the described surname and a first name starting with J. 
 Hint: 
     Use Regular Expressions 
     re.search(r"J.*Neu",line)  
 Solution:
     Jack Neu 555-7666
     Jeb Neu 555-5543
     Jennifer Neu 555-3652
"""
import re
with open("simpsons_phone_book.txt") as phone:
    file=phone.read()

x=re.compile(r"[J][\w]+[\s]*Neu.+")

x.findall(file)