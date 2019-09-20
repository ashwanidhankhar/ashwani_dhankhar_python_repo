# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:27:37 2019

@author: ashwa
"""
from collections import deque

queue=deque(["ravi","tejas","adtya","jony"])

print(queue)

queue.append("deep")

print(queue)

queue.append("jagan")

print(queue)

print(queue.popleft())

print(queue)


print(queue.popleft())

print(queue)





#############

from treelib import Node,Tree

new_tree=Tree()
new_tree.create_node("n1",1) #root node
new_tree.create_node("n2",2,parent=1)
new_tree.create_node("n3",3,parent=1)
new_tree.create_node("n4",4,parent=2)
new_tree.create_node("n5",5,parent=2)
new_tree.create_node("n6",6,parent=3)
new_tree.create_node("n1",7,parent=3)

new_tree.show()
