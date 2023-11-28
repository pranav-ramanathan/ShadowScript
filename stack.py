class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]




stack1 = Stack()

for num in range(1, 10, 2):
    stack1.push(num)


print(stack1.peek())