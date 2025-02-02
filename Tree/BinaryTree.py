
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def PreOrder(node):
    if not node:
        return
    print(node.value, end=" ")
    
    PreOrder(node.left)
    PreOrder(node.right)

def InOrder(node):
    if not node:
        return
    
    InOrder(node.left)
    print(node.value, end=" ")
    InOrder(node.right)
    


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# a.left = b
# b.right = c
# c.left = d
# d.right = e
# e.left = f
# f.left = g

InOrder(a)