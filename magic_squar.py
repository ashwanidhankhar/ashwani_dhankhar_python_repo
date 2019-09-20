# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:21:44 2019

@author: ashwani
"""
#importing numpy
import numpy as np

#taking user input for the dimension of matrix
Number= int(input(" Enter an odd number for NxN matrix :"))

#initializing a zero matrix of NxN dimensions
magic_square = np.zeros((Number,Number),dtype=int)

n=1

i,j=0,Number//2

#looping for placing the value inside the magic square
while (n <= Number**2):
    magic_square[i,j]=n
    n+=1
    newi,newj=(i-1)%Number,(j+1)%Number
    if magic_square[newi,newj]:
        i+=1
    else:
        i,j=newi,newj
        
from tkinter import *

root = Tk()

root.geometry("1000x1000")
root.title("Magic square")

for a in range(Number):
    for z in range(Number):
        b_n=Button(root,text=magic_square[a][z],bd=4, bg="lightblue",height=4,width=8)
        b_n.grid(row=a,column=z)

        
root.mainloop()
