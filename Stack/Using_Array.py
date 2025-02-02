class Stack:
    def __init__(self, size: int) -> None:
        self.stack: list = []
        self.size: int = size


    def push(self, data) -> None:
        if len(self.stack) <= self.size:
            self.stack.append(data)
        else:
            print("Overflow!")

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        else:
            print("Underflow!")

    def top(self) -> int:
        if self.stack:
            print(self.stack[-1])
        else:
            print("Stack is Empty!")

    def is_empty(self) -> bool:
        print(self.stack == [])
    
    def is_full(self) -> bool:
        print(len(self.stack) == self.size)

    def display(self):
        print(self.stack)


stack = Stack(5)
stack.is_empty()
stack.top()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.display()
stack.is_full()
stack.is_empty()
stack.pop()
stack.display()
stack.top()

