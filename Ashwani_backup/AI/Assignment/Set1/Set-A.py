# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:58:14 2019

@author: BSDU ADMIN
"""


##########################           SET A

#  Question 1

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












#######   Question 2

stack=['ash','ank','luv']

print(stack)

stack.pop()

print(stack)

stack.append("ankit")

print(stack)



##### question -3


from flask import Flask

app=Flask(__name__)

@app.route("/ashwani")

def BSDU():
    return "<h1>BSDU</h1><br>Welcome to Bhartiya Skill Development University,Jaipur"

if __name__=="__main__":
    app.run()
    
    
    
    ########### question 4
    
    
def hanoi(ndisks, startPeg=1, endPeg=3):

    if ndisks:

        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)

        print("Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg))

        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)

 
num=int(input("Enter the number of disks :"))
hanoi(ndisks=num)

