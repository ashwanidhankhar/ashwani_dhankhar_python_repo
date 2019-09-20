# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:50:58 2019

@author: ashwa
"""


#number of moves  = (2**n-1)

def hanoi(ndisks,startpeg=1,endpeg=3):
    if ndisks:
        hanoi(ndisks - 1,startpeg,6-startpeg-endpeg)
        print("Moves disk %d from peg %d to peg %d" % (ndisks,startpeg,endpeg))
        #or
        #print("Move disk {} from peg {} to peg {}".format(ndisks,startpeg,endpeg))
        hanoi(ndisks-1,6-startpeg-endpeg,endpeg)


# input the number os disks
hanoi(ndisks=3)