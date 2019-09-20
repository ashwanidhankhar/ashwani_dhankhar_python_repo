# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 00:38:56 2019

@author: ashwa
"""

import tkinter
from tkinter import *

root=Tk()

root.geometry("580x620")
root.title("Chess Board")



n=0
a=0
z="black"
x="white"
for i in range(8):
    b_n=Button(root,text=' ',bd=5, bg=z,height=4,width=8)
    b_n.grid(row=a,column=0)
    b_n=Button(root,text=' ',bd=5, bg=x,height=4,width=8)
    b_n.grid(row=a,column=1)
    b_n=Button(root,text=' ',bd=5, bg=z,height=4,width=8)
    b_n.grid(row=a,column=2)
    b_n=Button(root,text=' ',bd=5, bg=x,height=4,width=8)
    b_n.grid(row=a,column=3)
    b_n=Button(root,text=' ',bd=5, bg=z,height=4,width=8)
    b_n.grid(row=a,column=4)
    b_n=Button(root,text=' ',bd=5 , bg=x,height=4,width=8)
    b_n.grid(row=a,column=5)
    b_n=Button(root,text=' ',bd=5, bg=z,height=4,width=8)
    b_n.grid(row=a,column=6)
    b_n=Button(root,text=' ',bd=5, bg=x,height=4,width=8)
    b_n.grid(row=a,column=7)
    n+=1
    a+=1
    z,x=x,z


root.mainloop()