class Stack:
    # Interfaces
    def __init__(self, *args):
        self.__data = []
        self.__size: int = 0
        self.__index: int = -1
        #TODO Add threading?
        #TODO Add max size?
        #TODO **kwargs?

        for arg in args:
            self.push(arg)

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __next__(self):
        raise NotImplementedError

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
        if self.__size == 0:
            raise IndexError('Stack is empty')

        return self.__data[self.__index]

    def pop(self):
        #TODO Add threading?
        if self.__size == 0:
            raise IndexError('Stack is empty')

        value = self.__data[self.__index]
        del self.__data[self.__index]
        self.__index -= 1
        self.__size -= 1

        return value

    def push(self, *args):
        #TODO Add threading?
        for arg in args:
            self.__data.append(arg)
            self.__size += 1
            self.__index += 1

        return self

    # Class Methods (None so far...)

    # Static methods (None so far...)
