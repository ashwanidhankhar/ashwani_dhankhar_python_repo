# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:21:24 2019

@author: BSDU ADMIN
"""



def factorial():
    global e1
    fact=1
    num=int(str(e1.get()))
    for i in range(num,1,-1):
            fact=i*fact
            Button(root,width=30, text = ("Factorial of the number is -",fact), bd = '5', bg="black", fg="white").grid(row=4,column=1)
            



from tkinter import *

root=Tk()

root.geometry("500x100+600+200")


Label(root, text='Enter the number for factorial').grid(row=0) 
e1 = Entry(root) 
e1.grid(row=0, column=1) 
b1=Button(root, text = 'Find', bd = '5',command=factorial, bg="blue", fg="white")
b1.grid(row=2,column=1)
root.mainloop()










































