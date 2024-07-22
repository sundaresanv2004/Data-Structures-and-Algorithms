class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if self.head is None:
            print("Stack is Empty!")
        else:
            print("Removed: ", self.head.data)
            self.head = self.head.next

    def is_empty(self):
        if self.head is None:
            print("Stack is Empty!")
        else:
            print("Stack is not Empty!")
    
    def peek(self):
        if self.head is None:
            print("Stack is empty!")
        else:
            print(self.head.data)
    
    def display(self):
        if self.head is None:
            print("Stack is empty!")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

S = Stack()

arr = [5, 10, 15, 20, 25]
S.is_empty()
for i in arr:
    S.push(i)
S.display()
S.peek()
S.is_empty()
S.pop()
S.display()

