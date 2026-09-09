class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]

    def get_min(self):
        if len(self.stack) > 0:
            return min(self.stack)


stack = MinStack()

stack.push(5)
stack.push(3)
stack.push(7)

print("Stack:", stack.stack)
print("Top:", stack.top())
print("Minimum:", stack.get_min())

stack.pop()

print("Stack after pop:", stack.stack)
print("Minimum after pop:", stack.get_min())