# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:43:30 2019

@author: ashwa
"""

#########

import tkinter

top=tkinter.Tk()
#window code

top.mainloop()



###### to define a particular window size to open through tk inter

from tkinter import *


root=Tk()

root.geometry("500x100+600+200")

root.mainloop()




####### to show a red button over a window

from tkinter import *

root=Tk()
#setting the dimensions for thr grid
root.geometry("100x100")

#settign the layout of the buuton which would be displayed on the window
btn=Button(root,text="click",bd="5",command=root.destroy,height=1,width=10,bg="red")
btn1=Button(root,text="click_1",bd="5",command=root.destroy,height=1,width=10,bg="yellow")
btn2=Button(root,text="click_2",bd="5",command=root.destroy,height=1,width=10,bg="blue")

#this is very necessary to specify the position of the button
btn.pack(side="left")
btn1.pack(side="right")
btn2.pack(side="top")



root.mainloop()



###########


import tkinter

window=tkinter.Tk()

window.title("GUI")

#Taking image from the directory and storing in a variable

icon=tkinter.PhotoImage(file="C:\\Users\\ashwa\\Pictures\\adventure-air-aircraft-36487.jpg")

#displaying the picture using a label by passing the picture vairables

label = tkinter.label(window,image = icon)

label.pack()

window.mainloop()




##### making a label

import tkinter

root=tkinter.Tk()

label=Label(root,text="Hey this a an automated text .........")

label.pack()

root.mainloop()



##entry


from tkinter import *
root = Tk() 

Label(root,text="First Name  :").grid(row=0)
Label(root,text="Papa ka Naam :").grid(row=1)

e1=Entry(root).grid(row=0, column=1)
e2=Entry(root).grid(row=1, column=1)

b1=Button(root, text = 'Exit', bd = '5', command = root.destroy, bg="blue", fg="white")
b1.grid()

root.mainloop()



# Checkbox
from tkinter import *
root = Tk() 
var1 = IntVar() 
Checkbutton(root, text='male', variable=var1).grid(row=0, sticky=W) 
var2 = IntVar() 
Checkbutton(root, text='female', variable=var2).grid(row=1, sticky=W) 
mainloop()

# Listbox
root = Tk() 
Lb = Listbox(root) 
Lb.insert(1, 'Python') 
Lb.insert(2, 'Java') 
Lb.insert(3, 'C++') 
Lb.insert(4, 'Any other') 
Lb.pack() 
root.mainloop()




