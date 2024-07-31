class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        
    def dequeue(self):
        if self.head is None:
            print("Queue is Empty!")
        else:
            print("Removed: ", self.head.data)
            self.head = self.head.next
    
    def peek(self):
        if self.head is None:
            print("Queue is Empty!")
        else:
            print(self.head.data)
    
    def isempty(self):
        if self.head is None:
            print("Queue is Empty!")
        else:
            print("Queue is not Empty!")
        
    def display(self):
        if self.head is None:
            print("Queue is Empty!")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

Q = Queue()
Q.isempty()
arr = [1, 2, 3, 4, 5, 6]
for i in arr:
    Q.enqueue(i)
Q.display()
Q.isempty()
Q.dequeue()
Q.peek()
Q.display()