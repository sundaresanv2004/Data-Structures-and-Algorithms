class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def display(self):
        if self.queue == []:
            print("Queue is Empty!")
        else:
            pass