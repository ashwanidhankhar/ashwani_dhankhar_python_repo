# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 05:30:40 2019

@author: ashwa
"""

"""
Water jug problem tree

Using 3 gallon and 4 gallon water jugs we need 2 gallons of water in either of jugs.
We can use infinte water supply
No measures on jug
"""

from treelib import Node,Tree

new_tree=Tree()
new_tree.create_node("(0,0)",1) #root node
new_tree.create_node("(0,3)",2,parent=1)
new_tree.create_node("(4,0)",3,parent=1)
new_tree.create_node("(3,0)",4,parent=2)
new_tree.create_node("(3,3)",5,parent=4)
new_tree.create_node("(4,2)",6,parent=5)
new_tree.create_node("(1,3)",7,parent=3)
new_tree.create_node("(1,0)",8,parent=7)
new_tree.create_node("(0,1)",9,parent=8)
new_tree.create_node("(4,1)",10,parent=9)
new_tree.create_node("(2,3)",11,parent=10)

new_tree.show()

