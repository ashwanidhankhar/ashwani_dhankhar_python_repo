# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 01:27:59 2019

@author: ashwani

"""
################## 8*8  ######################33
import numpy as np 

import matplotlib.pyplot as plt


matrix=np.array([0,1]*32)
matrix=matrix.reshape(8,8)

for a in [1,3,5,7]:
    for i in [0,2,4,6]:
        matrix[a][i]=1
    for j in [1,3,5,7]:
        matrix[a][j]=0




       
plt.imshow(matrix, cmap = 'gray')
#####################################################




############# 64*64  #################


import matplotlib.pyplot as plt

import numpy as np


layout=np.array([0,1]*2048)
new=layout.reshape(64,64)

for row in [range(0,8),range(16,24),range(32,40),range(48,56)]:
    for column in [range(8,16),range(24,32),range(40,48),range(56,64)]:
        for a in row:
            for i in [range(0,8),range(16,24),range(32,40),range(48,56)]:
                for r in i:
                    new[a][r]=0
            for m in column:
                new[a][m]=1
        for a in column:
            for i in row:
                new[a][i]=1
            for m in [range(8,16),range(24,32),range(40,48),range(56,64)]:
                for e in m:
                    new[a][e]=0
                    
plt.imshow(new, cmap = 'gray')

"""

for z in [range(0,8),range(16,24),range(32,40),range(48,56)]:
    for q in [range(8,16),range(24,32),range(40,48),range(56,64)]:
        for a in z:
            for e in q:
                for i in [range(0,8),range(16,24),range(32,40),range(48,56)]:
                    new[a][i]=0
                for i in [range(8,16),range(24,32),range(40,48),range(56,64)]:
                    new[a][i]=1    
                for i in [range(0,8),range(16,24),range(32,40),range(48,56)]:
                    new[e][i]=1
                for i in [range(8,16),range(24,32),range(40,48),range(56,64)]:
                    new[e][i]=0
"""
       



##################################################################

"""

import matplotlib.pyplot as plt

import numpy as np


layout=np.array([0,1]*2048)
new=layout.reshape(64,64)

for z in [range(0,8),range(16,24),range(32,40),range(48,56)]:
    for b in [range(8,16),range(24,32),range(40,48),range(56,64)]:
        for a in z:
            for i in [0,1,2,3,4,5,6,7]:
                new[a][i]=0
            for m in [8,9,10,11,12,13,14,15]:
                new[a][m]=1
        for a in b:
            for i in [0,1,2,3,4,5,6,7]:
                new[a][i]=1
            for m in [8,9,10,11,12,13,14,15]:
                new[a][m]=0
        for a in z:
            for i in [16,17,18,19,20,21,22,23]:
                new[a][i]=0
            for m in [24,25,26,27,28,29,30,31]:
                new[a][m]=1
        for a in b:
            for i in [16,17,18,19,20,21,22,23]:
                new[a][i]=1
            for m in [24,25,26,27,28,29,30,31]:
                new[a][m]=0
        for a in z:
            for i in [32,33,34,35,36,37,38,39]:
                new[a][i]=0
            for m in [40,41,42,43,44,45,46,47]:
                new[a][m]=1
        for a in b:
            for i in [32,33,34,35,36,37,38,39]:
                new[a][i]=1
            for m in [40,41,42,43,44,45,46,47]:
                new[a][m]=0
        for a in z:
            for i in [48,49,50,51,52,53,54,55]:
                new[a][i]=0
            for m in [56,57,58,59,60,61,62,63]:
                new[a][m]=1
        for a in b:
            for i in [48,49,50,51,52,53,54,55]:
                new[a][i]=1
            for m in [56,57,58,59,60,61,62,63]:
                new[a][m]=0
            
       
   
plt.imshow(new, cmap = 'gray')

"""
###################################################




"""
problem in this code




import matplotlib.pyplot as plt

import numpy as np


layout=np.array([0,1]*2048)
new=layout.reshape(64,64)

for row in [range(0,8),range(16,24),range(32,40),range(48,56)]:
    for column in [range(8,16),range(24,32),range(40,48),range(56,64)]:
        for a in row:
            for i in row:
                new[a][i]=0
            for m in column:
                new[a][m]=1
        for a in column:
            for i in row:
                new[a][i]=1
            for m in column:
                new[a][m]=0
       
plt.imshow(new, cmap = 'gray')


"""