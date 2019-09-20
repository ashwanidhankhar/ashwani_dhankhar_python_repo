stack = ['Sakshi', 'Arohi', 'Parul']
stack.append('Lavish')
stack.append('Rahul')

print(stack)
print(stack.pop())
print(stack)


from collections import deque
queue = deque(['Ravi','Tejas','Aditya','Jony'])
print(queue)
queue.append('Deep')
print(queue)

print(queue.popleft())
print(queue)
print(queue.pop())
print(queue)


from treelib import Node, Tree

new_tree = Tree()
new_tree.create_node("n1",1) # Root Node
new_tree.create_node("n2",2, parent=1)

new_tree.create_node("n3",3,parent=1) # Parent of n4 and n5
new_tree.create_node("n4",4,parent=3)
new_tree.create_node("n5",5,parent=3)

new_tree.show()

# PRACTICE
prac_tree = Tree()
prac_tree.create_node("A",1)
prac_tree.create_node("B",2,parent=1)

prac_tree.create_node("C",3,parent=1)
prac_tree.create_node("E",4,parent=3)
prac_tree.create_node("F",5,parent=3)
prac_tree.create_node("G",6,parent=5)
prac_tree.create_node("H",7,parent=5)

prac_tree.create_node("D",8,parent=1)
prac_tree.create_node("I",9,parent=8)
prac_tree.create_node("J",10,parent=8)

prac_tree.show()