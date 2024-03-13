class Node:
    def __init__(self, value, next_value=None):
        self.data = value
        self.next = next_value


class LinkedList:
    def __init__(self):
        self.head = None

    def new_list(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_mid(self, value, pos):
        if self.head is None:
            print("List is empty, can't insert!")
            return
        else:
            new_node = Node(value)
            temp = self.head
            i = 1
            while i < (pos - 1):
                temp = temp.next
                i += 1
            new_node.next = temp.next
            temp.next = new_node

    def add_last(self, value):
        if self.head is None:
            print("List is empty, can't insert!")
            return
        else:
            new_node = Node(value)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete_first(self):
        if self.head is None:
            print("List is empty, can't delete!")
            return
        else:
            self.head = self.head.next

    def delete_mid(self, pos):
        if self.head is None:
            print("List is empty, can't delete!")
            return
        else:
            temp = self.head
            i = 1
            pre = temp
            while i < pos:
                pre = temp
                temp = temp.next
                i += 1
            pre.next = temp.next

    def delete_last(self):
        if self.head is None:
            print("List is empty, can't delete!")
            return
        else:
            temp = self.head
            pre = temp
            while temp.next:
                pre = temp
                temp = temp.next
            pre.next = None

    def swap_elements(self, value1, value2):
        node1 = self.head
        node2 = self.head
        pre_node1 = None
        pre_node2 = None

        if value1 == value2:
            print("Both the elements are same, swap no needed!")
            return

        while node1 is not None:
            if node1.data == value1:
                break
            pre_node1 = node1
            node1 = node1.next

        while node2 is not None:
            if node2.data == value2:
                break
            pre_node2 = node2
            node2 = node2.next

        if node1 is None or node2 is None:
            print("Can't Swap!")
            return

        if pre_node1 is None:
            self.head = node2
        else:
            pre_node1.next = node2

        temp = node1.next

        if pre_node2 is None:
            self.head = node1
        else:
            pre_node2.next = node1

        node1.next = node2.next
        node2.next = temp

    def reverse(self):
        if self.head is None:
            print("List is Empty!")
        else:
            prev = None
            temp = self.head
            while temp:
                next_node = temp.next
                temp.next = prev
                prev = temp
                temp = next_node
            self.head = prev

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


ll = LinkedList()
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
    print("9. Reverse.")
    print("10. Display.")
    print("11. Exit.")
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
        ll.reverse()
        ll.display()
    elif user_input == "10":
        ll.display()
    elif user_input == "11":
        print()
        print("--- Thank You ---")
        print()
        break
    else:
        print()
        print("*** Enter a valid option number! ***")
        print()
