class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []
    
    def enqueue(self, data):
        if len(self.queue) < self.size:
            self.queue.append(data)
        else:
            print("Queue is Full!")
    
    def dequeue(self):
        if not self.queue:
            print("Queue is Empty!")
        else:
            print("Removed: ", self.queue.pop(0))
    
    def peek(self):
        if not self.queue:
            print("Queue is Empty!")
        else:
            print(self.queue[0])
    
    def isEmpty(self):
        if not self.queue:
            print("Queue is Empty!")
        else:
            print("Queue is not Empty")
    
    def isFull(self):
        if  len(self.queue) == self.size:
            print("Queue is Full!")
        else:
            print("Queue is not Full")
    
    def display(self):
        if not self.queue:
            print("Queue is Empty!")
        else:
            print(self.queue)

Q = Queue(5)
Q.isEmpty()
Q.isFull()
for i in range(1, 7):
    Q.enqueue(i)
Q.display()
Q.isFull()
Q.dequeue()
Q.isEmpty()
Q.peek()
Q.display()
