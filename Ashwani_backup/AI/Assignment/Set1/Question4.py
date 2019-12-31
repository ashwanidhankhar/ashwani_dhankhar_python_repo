# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:42:18 2019

@author: BSDU ADMIN
"""

def hanoi(ndisks, startPeg=1, endPeg=3):

    if ndisks:

        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)

        print("Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg))

        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)

 
num=int(input("Enter the number of disks :"))
hanoi(ndisks=num)

