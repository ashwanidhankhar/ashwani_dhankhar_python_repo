# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:55:47 2019

@author: BSDU ADMIN
"""





#                        SET-B

#Q1. Write a program in Python to generate Fibonacci series using recursive function. 
#Accept number of elements from user input and print the series 
#elements on window screen (Use Tkinter-GUI based).
user_input = int(input("Enter a positive number>>"))
fibo_list=[]
def Fibo(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibo(n-1)+Fibo(n-2) 
  
for i in range(1,user_input+1):
    
    fibo_list.append(Fibo(i)) 
    
root = tk.Tk()
tk.Label(root,text="Fibonacci series:").grid(row=0,column=0)
for j in range(0,len(fibo_list)):
    l1 = tk.Label(root,text=fibo_list[j],width=5)
    l1.grid(row=j+1,column=1)
root.mainloop()
       

#Q2. Write a program in Python to create Queue and perform insert and delete 
#operations items from the Queue. (Simple or Library based)
#deque
#queue
import queue   
L = queue.Queue(maxsize=20)  
L.put(5) 
L.put(9) 
L.put(1) 
L.put(7) 
print(L.get()) 
print(L.get()) 
print(L.get()) 
print(L.get()) 
print(L.get()) 


#Q3. Write a Web based program in Python to display Definitions of “Artificial Intelligence” 
#on web page (Web Browser based) using Flask.
from flask import Flask
app = Flask(__name__)
@app.route('/ria')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>AI Defination</title>
</head>
<body>

<p> AI is the study of how to make computers do things at which, at present, people are better.</li>
      	<li>Barr and Figenbaum: h/b of AI - AI is the qualitative expansion of the computers ability</li>
      	<li>Charnaik & Mcdermott:  Study of mental faculties by the use of computational models.</li>
      	<li>Buchanen: AI provides tools for symbolic processing using non-algorithmic methods.</p>

</body>
</html>
'''
if __name__ == '__main__':
    app.run()
    
    
    
#Write a program in Python to develop 3X3 board and generate random numbers from 1 to 9 
#on the blocks of board (GUI based).

import tkinter as tk
import numpy as np
root = tk.Tk()
root.title('3X3 board of random numbers')

random_list = list(np.random.randint(1,9,9))

for i in range(0,3):
    for j in range(0,3):
        button1 = tk.Button(root,text=random_list[i+j],height=5,width=10,bg="light blue")
        button1.grid(row=i,column=j)
        
root.mainloop()