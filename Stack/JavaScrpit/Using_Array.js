class Stack {
  constructor(size) {
    this.stack = [];
    this.size = size;
  }

  push(data) {
    if (this.stack.length <= this.size) {
      this.stack.push(data);
    } else {
      confirm.log("Overflow!");
    }
  }

  pop() {
    if (this.stack) this.stack.pop();
    else console.log("Underflow!");
  }

  isEmpty() {
    console.log(this.stack.length === 0);
  }

  display() {
    console.log(this.stack);
  }
}

let stack = new Stack(5);
stack.push(5);
stack.push(4);
stack.push(3);
stack.display();
stack.pop();
stack.display();
