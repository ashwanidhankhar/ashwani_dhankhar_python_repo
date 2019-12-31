# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:16:51 2019

@author: BSDU ADMIN
"""

import theano.tensor as T
from theano import function

#converting normal variable to scalar vairable
a = T.dscalar('a')
b = T.dscalar('b')

c= a*b

#Converting into scalar function
f=function([a,b],c)

f(3,12)

##############################################

# converting into vector variable

a = T.vector('a')

b = T.vector('b')

c=a*b

f=function([a,b],c)

f([1,2,3],[1,2,3])


##############################################

#converting into matrix

a =  T.matrix('a')

b = T.matrix('b')


c=a+b

f=function([a,b],c)

f([[1,2,3],
  [4,5,6]],
  [[1,2,3],
   [8,9,10]])




#########################################


#gradient = (dy/dx)

x= T.dscalar('x')

#dy/dx of x**3 = 3x**2
y=x**3

dy=T.grad(y,x)

f=function([x],dy)

#passing the value of x in dy/dx of x**3
f(4)