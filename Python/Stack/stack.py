class Stack:
    data = []
    stack_size = None
    index = None

    def __init__(self, data = None):
        if data:
            self.index = 0
            self.stack_size = self.index + 1
            self.data[self.index] = data

    def pop(self):
        value = self.data[self.index]
        del self.data[self.index]
        self.index -= 1
        self.stack_size -= 1

        return value

    def peek(self):
        return self.data[self.index]

    def push(self, value):
        if not self.stack_size:
            self.index = 0
        self.data[self.index] = value
        self.stack_size = self.index + 1
        self.index += 1

        return self

    def size(self):
        return self.stack_size

    def empty(self):
        return bool(self.stack_size)