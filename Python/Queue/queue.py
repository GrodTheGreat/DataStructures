class Queue:
    def __init__(self):
        self.__data = []
        self.__head = 0
        self.__tail = -1
        self.__size = 0

    @property
    def size(self):
        return self.__size

    def enqueue(self, item):
        self.__tail = (self.__tail + 1) % self.size
        self.__data.append(item)
        # self.__data.insert(self.__tail, item)
        self.__size += 1

        return self

    def dequeue(self):
        if not self.size > 0:
            raise IndexError("Dequeue from an empty queue")

        item = self.__data[self.__head]
        self.__head = (self.__head + 1) % self.size
        self.__size -= 1

        return item

    def peek(self):
        if not self.size > 0:
            raise IndexError("Peek from an empty queue")

        return self.__data[0]

    def is_empty(self):
        return not self.size > 0

    def clear(self):
        self.__data = []
        self.__head = 0
        self.__tail = -1
        self.__size = 0

        return self

    def to_list(self):
        return self.__data
