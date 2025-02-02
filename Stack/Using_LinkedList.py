class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_node

    def pop(self):
        if self.head is None:
            print("Underflow!")
        else:
            temp = self.head
            pre = None
            while temp.next:
                pre = temp
                temp = temp.next
            pre.next = None
    
    def top(self):
        if self.head is None:
            print("Stack is Empty")
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            print(temp.data)
    
    def is_empty(self):
        print(self.head is None)
    

    def display(self):
        if self.head is None:
            print("Stack is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" <--> ")
                temp = temp.next
            print()



stack = Stack()
stack.is_empty()
stack.push(5)
stack.push(4)
stack.push(3)
stack.display()
stack.pop()
stack.display()
stack.top()
stack.display()
stack.is_empty()


