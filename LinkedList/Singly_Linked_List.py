class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert at the beginning
    def insert_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Insert at a specific position
    def insert_mid(self, data, pos):
        if pos < 1:
            print("Invalid position!")
            return 
        
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            i = 1
            while i < (pos - 1):
                curr = curr.next
                i += 1
            new_node.next = curr.next
            curr.next = new_node
    
    # Insert at the end
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            
            curr.next = new_node
    
    # Delete from the beginning
    def delete_first(self):
        if not self.head:
            print("List is Empty!")
        else:
            self.head = self.head.next
    
    # Delete a specific node
    def delete_mid(self, pos):
        if not self.head:
            print("List is Empty!")
        else:
            i = 1
            curr = self.head
            pre = None
            while i < (pos - 1):
                pre = curr
                curr = curr.next
                i += 1

            pre.next = curr.next            

    
    # Delete from the end
    def delete_end(self):
        if not self.head:
            print("List is Empty!")
        else:
            curr = self.head
            pre = None
            while curr.next:
                pre = curr
                curr = curr.next

            pre.next = None
    
    # Searching in Singly Linked List
    def search(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                print(True)
                return
            curr = curr.next
            
        print(False)
    
    # Length of Singly Linked List
    def list_len(self):
        curr = self.head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        print(length)

    
    # Display
    def display(self):
        if not self.head:
            print("List is Emtpy!")
        else:
            curr = self.head
            while curr:
                print(curr.data, end=" <-> ")
                curr = curr.next
            print()



ll = LinkedList()
ll.list_len()
ll.insert_first(10)
ll.insert_first(5)
ll.insert_end(20)
ll.insert_end(25)
ll.list_len()
ll.display()
ll.insert_mid(15, 3)
ll.insert_end(30)
ll.display()
ll.search(20)
ll.delete_first()
ll.delete_end()
ll.display()
ll.list_len()
ll.search(30)

