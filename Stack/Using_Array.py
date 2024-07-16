# Implementation of Stack using Array


class Stack:

    def __init__(self, capacity):
        self.arr = []
        self.capacity = capacity
        self.top = -1

    def push(self, data):
        if len(self.arr) > self.capacity:
            print("Stack is Full!")
        else:
            self.arr.append(data)
            self.top += 1

    def pop(self):
        if self.top == -1:
            print("Stack is Empty!")
        else:
            print(f"Removed: {self.arr.pop()}")
            self.top -= 1

    def peek(self):
        if len(self.arr) == 0:
            print("Stack is Empty!")
        else:
            print("Top element:", self.arr[-1])

    def size(self):
        if len(self.arr) == 0:
            print("Stack is Empty!")
        else:
            print(f"Size of the Stack: {self.top + 1}")

    def display(self):
        if len(self.arr) == 0:
            print("Stack is Empty!")
        else:
            for e in self.arr:
                print(e, end=" ")
            print()


S = Stack(5)
arr = [5, 10, 15, 20, 25, 30]
for i in arr:
    S.push(i)
S.display()
S.peek()
S.pop()
S.display()
S.size()
