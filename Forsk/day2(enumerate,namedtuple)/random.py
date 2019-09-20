# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:36:07 2019

@author: ashwa
"""

import random
list1=[]
i=0
for x in range(100):
    i=random.randint(1,14)
    if i in list1:
        continue
    elif len(list1)==14:
        break        
    else:
        list1.append(i)


random.uniform(1.1,10.1)