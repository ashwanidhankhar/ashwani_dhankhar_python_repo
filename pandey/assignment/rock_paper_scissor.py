# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 01:11:23 2019

@author: ashwa
"""

print("Welcome to rock,paper,scissor game")
print("""You can choose one of these
Rock
Paper
Scissor
Type EXIT in both input boxes to exit the program
\n """)

while(True):
    
    user1=input("Player 1 Enter your input ---  ").lower()
    user2=input("Player 2 Enter your input ---  ").lower()
    
    print("\n")

    if(user1=="rock" and user2=="paper"):
        print("Paper beats Rock...Player 2 wins \n")
    
    elif(user1=="rock" and user2=="scissor"):
        print("Rock beats Scissor...Player 1 wins\n")
    
    elif(user1=="paper" and user2=="scissor"):
        print("Scissor beats Paper...Player 2 wins\n")
    
    elif(user1=="paper" and user2=="rock"):
        print("Paper beats Rock...Player 1 wins\n")
    
    elif(user1=="scissor" and user2=="paper"):
        print("Scissor beats Paper...Player 1 wins\n")
    
    elif(user1=="scissor" and user2=="sock"):
        print("Rock beats Scissor...Player 2 wins\n")

    elif(user1=="exit" or user2=="exit"):
        break        

    elif(user1==user2):
        print ("Clash\n")

   
