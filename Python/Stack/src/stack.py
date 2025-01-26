from threading import Lock

class Stack:
    # Interfaces
    def __init__(self, *args):
        self.__data: list[any] = []
        self.__size: int = 0
        self.__index: int = -1
        self.__lock: Lock = Lock()
        #TODO Add max size?
        #TODO **kwargs?

        for arg in args:
            self.push(arg)

    def __repr__(self):
        return f"Stack({', '.join(map(str, self.__data))}, size={self.__size}, index={self.__index})"

    def __str__(self):
        if self.empty():
            return "Stack is empty"
        return f"Stack(top -> {', '.join(map(str, reversed(self.__data)))} -> bottom)"

    def __eq__(self, other):
        if type(other) is not Stack:
            return False

        return self.__data == other.__data

    def __iter__(self):
        self.__iter_index = self.__index
        return self

    def __next__(self):
        if self.__iter_index == -1:
            raise StopIteration

        value = self.__data[self.__iter_index]
        self.__iter_index -= 1

        return value

    def __len__(self):
        return self.__size

    def __bool__(self):
        return not self.empty()

    # Properties
    @property
    def size(self):
        return self.__size

    #Public Methods
    def empty(self):
        return not bool(self.__size)

    def peek(self):
        with self.__lock:
            if self.__size == 0:
                raise IndexError('Stack is empty')

            return self.__data[self.__index]

    def pop(self):
        with self.__lock:
            if self.__size == 0:
                raise IndexError('Stack is empty')

            value = self.__data[self.__index]
            del self.__data[self.__index]
            self.__index -= 1
            self.__size -= 1

            return value

    def push(self, *args):
        with self.__lock:
            for arg in args:
                self.__data.append(arg)
                self.__size += 1
                self.__index += 1

            return self

    # Class Methods (None so far...)

    # Static methods (None so far...)
