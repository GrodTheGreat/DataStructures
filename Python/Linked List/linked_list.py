class Node:
    def __init__(self, data):
        self.data: any = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class PyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0

    # Insert Items
    def insert_head(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.size += 1

        return self

    def insert_tail(self, data):
        node = Node(data)
        self.tail.set_next(node)
        self.tail = node
        self.size += 1

        return self

    def insert_at(self, index: int, data):
        pass

    # Get Items
    def get_first(self) -> Node:
        return self.head

    def get_last(self) -> Node:
        return self.tail

    def get(self, index: int) -> Node:
        pass

    # Delete Items
    def remove_first(self):
        next_node = self.head
        self.head = next_node.get_next()
        del next
        self.size -= 1

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
    def size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size > 0

    def clear(self) -> None:
        pass

    def iterator(self):
        pass

    def clone(self):
        pass

    def reverse(self):
        pass

    def sort(self):
        pass
