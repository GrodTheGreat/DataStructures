class Node:
    def __init__(self, data):
        self.__data: any = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node


class LinkedList:
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__size: int = 0

    # Insert Items
    def insert_head(self, data):
        node = Node(data)
        if self.__head:
            node.set_next(self.__head)

        self.__head = node
        self.__size += 1

        return self

    def insert_tail(self, data):
        node = Node(data)
        if self.__tail:
            self.__tail.set_next(node)

        self.__tail = node
        self.__size += 1

        return self

    def insert_at(self, index: int, data):
        if index > self.__size + 2:
            raise IndexError("Index larger than list.")
        if index == 0:
            return self.insert_head(data)
        if index == self.__size + 1:
            return self.insert_tail(data)
        pass

    # Get Items
    def get_head(self) -> Node:
        return self.__head

    def get_tail(self) -> Node:
        return self.__tail

    def get(self, index: int) -> Node:
        pass

    # Delete Items
    def remove_first(self):
        next_node = self.__head
        self.__head = next_node.get_next()
        del next_node
        self.__size -= 1

        return self

    def remove_last(self):
        pass

    def remove(self, index: int):
        pass

    def remove_data(self, data):
        pass

    # Search
    def index_of(self) -> int:
        pass

    def last_index_of(self) -> int:
        pass

    def contains(self) -> bool:
        # Might be a dunder method for this...
        pass

    # Other
    @property
    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return not self.__size > 0

    def clear(self) -> None:
        node = self.__head
        while node:
            print(self.__size)
            temp = node
            node = node.get_next()
            del temp
            self.__size -= 1

        return self

    def iterator(self):
        pass

    def clone(self):
        pass

    def reverse(self):
        pass

    def sort(self):
        pass
