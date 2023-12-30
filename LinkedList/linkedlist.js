class Node {
    constructor(data, next=null) {
        this.data = data;
        this.next = next;
    }
}


class LinkedList {
    constructor(data) {
        this.head = null;
    }

    new_list(data) {
        const newNode = new Node(data)
        if (!this.head) {
            this.head = newNode;
        }
        else {
            let current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    add_first(data) {
        const newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode
    }

    add_mid(data, pos) {
        const newNode = new Node(data);
        if (!this.head) {
            console.log("Can't insert, List is empty!");
        }
        else {
            let current = this.head;
            let i = 1;
            while (i < (pos -1)) {
                current = current.next;
                i++;
            }
            newNode.next = current.next;
            current.next = newNode;
        }
    }

    add_last(data) {
        const newNode = new Node(data)
        if (!this.head) {
            console.log("Can't insert, List is empty!");
        }
        else {
            let current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    delete_first() {
        if (!this.head) {
            console.log("List is empty!");
        }
        else {
            this.head = this.head.next;
        }
    }

    delete_mid(pos) {
        if (!this.head) {
            console.log("List is empty!");
        }
        else {
            let current = this.head;
            let i = 1;
            let pre = null;
            while (i < pos) {
                pre = current;
                current = current.next;
                i++;
            }
            pre.next = current.next;
        }
    }

    delete_last() {
        if (!this.head) {
            console.log("List is empty!");
        }
        else {
            let current = this.head;
            let pre = null;
            while (current.next) {
                pre = current;
                current = current.next;
            }
            pre.next = null;
        }
    }

    swap(val1, val2) {
        let node1 = this.head;
        let node2 = this.head;
        let pre1 = null;
        let pre2 = null;
    }

    display() {
        if (!this.head) {
            console.log("List is empty!");
        }
        else {
            let current = this.head;
            let temp = "";
            while (current) {
            temp += `${current.data} <-->`;
            current = current.next;
            }
            console.log(temp);
        }
    }
}

const ll = new LinkedList();
ll.new_list(15);
ll.add_first(10);
ll.add_first(5);
ll.add_last(25);
ll.add_mid(20, 4);
ll.new_list(30)
ll.display();
ll.delete_first();
ll.display();
ll.delete_last();
ll.display();
ll.delete_mid(2);
ll.display();
