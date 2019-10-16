# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:02:39 2019

@author: BSDU ADMIN
"""

from easyAI import TwoPlayersGame,Human_Player,AI_Player,Negamax

class GameofBones(TwoPlayersGame):
    
    def __init__(self,players):
        self.players=players
        self.pile=20 #start with 20 bones in the pile
        self.nplayer=2 #player 1 starts
        
    def possible_moves(self):
        return['1','2','3']
    def make_move(self,move):
        self.pile -= int(move)
    def win(self):
        return self.pile <=0
    def is_over(self): 
        return self.win()
    def show(self):
        print("%d bones left in the pile"%self.pile)
    def scoring(self): 
        return 100 if game.win() else 0  # for the AI
    
    
ai= Negamax(13)


game=GameofBones([Human_Player(),AI_Player(ai)])

history = game.play()