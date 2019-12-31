#                               SET-A


#Q1. Write a program in Python to find factorial of any user input number using Tkinter (GUI based). 

import tkinter as tk
from tkinter.colorchooser import *
 
def factorial(n):   
    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
 
def calculate():
    result=factorial(int(entryText.get()))
    info.config(text=result)
    
mw = tk.Tk()
mw.title('COLOR ME!!!')
mw.geometry("200x200") 
mw.resizable(0, 0)
 
entryText = tk.Entry(text=1, bg='white', fg='black')
entryText.place(x = 50, y = 25, width=100, height=25)
 
btn = tk.Button(text='Calculate', command=calculate)
btn.place(x = 50, y = 75, width=100, height=25)
 
info = tk.Label(text='result', bg='white', fg='black')
info.place(x = 50, y = 125, width=100, height=25)
 
mw.mainloop()


#Q2. Write a program in Python to create Stack and perform insert and delete operations items 
#from the Stack. (Simple or Library based)

stack = ['Artificial Intelligence with Python', 'Statistics with R', 'Machine Learning with Python']
stack.append('Cloud Computing')

print(stack)
print(stack.pop())
print(stack)



#Q3. Write a Web based program in Python to display one paragraph contents describing BSDU Jaipur 
#on web page (Web Browser based) using Flask.

from flask import Flask
app = Flask(__name__)
@app.route('/ria')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bhartiya Skill Development University</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center" style="background: #2f7bb3">
	<img src="https://www.fablabs.io/media/W1siZiIsIjIwMTgvMDkvMDEvMDgvMzIvMDUvZGY0YmU5MWUtMmJlNC00ZDgyLTk0NDktYTYxMjg1YzA5YjhhL0JTRFUgTG9nby5wbmciXSxbInAiLCJ0aHVtYiIsIjMwMHgzMDAiXV0/BSDU%20Logo.png?sha=982a2bf7d27b4020" style="float: left; width: 10%" >
  <h1 style="color: white" >Bhartiya Skill Development University</h1>
  <p style="color: white">Swiss Dual System of Skill Development</p> 
</div>
  
<div class="container">
  <div class="row">
    <div class="col-sm-12">
      <center><h3>WHY BSDU</h3></center>
      <p>BSDU has been incorporated as a State Private University vide GOR Act No. 3 of 2017 (BSDU Act). It is the first University in the country offering only Skills programs. It offers Skill Certificate, Diploma, Advance Diploma, Bachelor of Vocation (B.Voc), Master of Vocation (M.Voc) and Ph.D in various skill areas.</p>
      
    </div>
  </div>
</div>

</body>
</html>
'''

if __name__ == '__main__':
    app.run()
    
    
    
#Q4. Write a program in Python to implement Simple 8-Queen Problem (position based). 
#Hint-Fix position of the first queen and find position of the seven queens on the 8X8 board.

BOARD_SIZE = 8

def under_attack(col, queens):

    return col in queens or any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))

def solve(n):

    solutions = [[]]

    for row in range(n):

        solutions = (solution+[i+1]

                       for solution in solutions 

                       for i in range(BOARD_SIZE)

                       if not under_attack(i+1, solution))

    return solutions



answers = solve(BOARD_SIZE)

first_answer = next(answers)

print(list(enumerate(first_answer, start=1)))

#                                             OR
# Write a program in Python to solve Simple Tower of Hanoi problem in Python. (Simple or Using EasyAI Library)
#simple
def hanoi(ndisks, startPeg=1, endPeg=3):

    if ndisks:

        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)

        print("Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg))

        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)

hanoi(ndisks=3)
#Easy AI















#                           SET-B

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
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center" style="background: #2f7bb3">
	<img src="https://www.fablabs.io/media/W1siZiIsIjIwMTgvMDkvMDEvMDgvMzIvMDUvZGY0YmU5MWUtMmJlNC00ZDgyLTk0NDktYTYxMjg1YzA5YjhhL0JTRFUgTG9nby5wbmciXSxbInAiLCJ0aHVtYiIsIjMwMHgzMDAiXV0/BSDU%20Logo.png?sha=982a2bf7d27b4020" style="float: left; width: 10%" >
  <h1 style="color: white" >Bhartiya Skill Development University</h1>
  <p style="color: white">Swiss Dual System of Skill Development</p> 
</div>
  
<div class="container">
  <div class="row">
    <div class="col-sm-12">
      <center><h3><b><u>What is AI?    Definitions</u></b></h3></center><br><br>
      <ol>
      	<li>ERich: AI is the study of how to make computers do things at which, at present, people are better.</li>
      	<li>Barr and Figenbaum: h/b of AI - AI is the qualitative expansion of the computers ability</li>
      	<li>Charnaik & Mcdermott:  Study of mental faculties by the use of computational models.</li>
      	<li>Buchanen: AI provides tools for symbolic processing using non-algorithmic methods.
</li>
      	<li>Others:  AI is the study of techniques for solving exponentially hard problems in polynomial time, by exploiting knowledge about the problem domain.</li>
      </ol>
      
    </div>
  </div>
</div>

</body>
</html>
'''
if __name__ == '__main__':
    app.run()


#Q4. Write a program in Python for Tic Tac Toe with MinMax (Negamax), AI Bot based using EasyAI library.

from easyAI import TwoPlayersGame

from easyAI.Player import Human_Player



class TicTacToe( TwoPlayersGame ):

    def __init__(self, players):

        self.players = players

        self.board = [0 for i in range(9)]

        self.nplayer = 1 # player 1 starts.

    

    def possible_moves(self):

        return [i+1 for i,e in enumerate(self.board) if e==0]

    

    def make_move(self, move):

        self.board[int(move)-1] = self.nplayer



    def unmake_move(self, move): # optional method (speeds up the AI)

        self.board[int(move)-1] = 0

    

    def lose(self):

        """ Has the opponent "three in line ?" """

        return any( [all([(self.board[c-1]== self.nopponent)

                      for c in line])

                      for line in [[1,2,3],[4,5,6],[7,8,9], # horiz.

                                   [1,4,7],[2,5,8],[3,6,9], # vertical

                                   [1,5,9],[3,5,7]]]) # diagonal

        

    def is_over(self):

        return (self.possible_moves() == []) or self.lose()

        

    def show(self):

        print ('\n'+'\n'.join([

                        ' '.join([['.','O','X'][self.board[3*j+i]]

                        for i in range(3)])

                 for j in range(3)]) )

                 

    def scoring(self):

        return -100 if self.lose() else 0

  

if __name__ == "__main__":

    

    from easyAI import AI_Player, Negamax

    ai_algo = Negamax(6)

    TicTacToe( [Human_Player(),AI_Player(ai_algo)]).play()
#                                                 OR

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

 
 
 
 
 

