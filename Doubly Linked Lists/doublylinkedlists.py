class Node:

    def __init__(self, value, next_val=None, prev_val=None):
        self.data = value
        self.next = next_val
        self.prev = prev_val


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def create_list(self, value):
        self.head = Node(value)

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            print("List is empty, can't insert!")
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def add_mid(self, value, pos):
        new_node = Node(value)
        if self.head is None:
            print("List is empty, can't insert!")
            return
        else:
            temp = self.head
            i = 1
            while i < (pos - 1):
                temp = temp.next
                i += 1
            new_node.next = temp.next
            temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp

    def reverse_list(self):
        curr = self.head
        new_head = None
        while curr is not None:
            curr.next, curr.prev = curr.prev, curr.next
            new_head = curr
            curr = curr.prev

        self.head = new_head

    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        else:
            temp = self.head
            while temp:
                print(str(temp.data) + " <--> ", end='')
                temp = temp.next
            print()


ll = DoublyLinkedList()
ll.create_list(15)
ll.add_first(5)
ll.add_last(25)
ll.add_first(1)
ll.add_last(20)
ll.add_mid(16, 4)
ll.add_mid(21, 5)
ll.display()
ll.reverse_list()
ll.display()
"""
print()
print("-----  LinkedList  -----")
print()
while True:
    print()
    print("--- Options ---")
    print()
    print("1. Create the first node.")
    print("2. Insert at first.")
    print("3. Insert at middle.")
    print("4. Insert at last.")
    print("5. Delete first node.")
    print("6. Delete middle node.")
    print("7. Delete last node.")
    print("8. Swap two nodes.")
    print("9. Display.")
    print("10. Exit.")
    print()
    user_input = str(input("Enter the option: "))
    print()
    if user_input == "1":
        a = int(input("Enter the Number: "))
        ll.new_list(a)
        ll.display()
    elif user_input == "2":
        a = int(input("Enter the Number: "))
        ll.add_first(a)
        ll.display()
    elif user_input == "3":
        a = int(input("Enter the Number: "))
        b = int(input("Enter the position: "))
        ll.add_mid(a, b)
        ll.display()
    elif user_input == "4":
        a = int(input("Enter the Number: "))
        ll.add_last(a)
        ll.display()
    elif user_input == "5":
        ll.delete_first()
        ll.display()
    elif user_input == "6":
        b = int(input("Enter the position: "))
        ll.delete_mid(b)
        ll.display()
    elif user_input == "7":
        ll.delete_last()
        ll.display()
    elif user_input == "8":
        a1 = int(input("Enter the 1st Number: "))
        a2 = int(input("Enter the 2nd Number: "))
        ll.swap_elements(a1, a2)
        ll.display()
    elif user_input == "9":
        ll.display()
    elif user_input == "10":
        print()
        print("--- Thank You ---")
        print()
        break
    else:
        print()
        print("*** Enter a valid option number! ***")
        print()
"""
