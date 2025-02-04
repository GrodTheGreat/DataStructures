import pytest
from src.linked_list import LinkedList


class TestLinkedList:
    def test_insert_head(self):
        ll = LinkedList()
        ll.insert_head(10)
        assert ll.get_head().get_data() == 10
        assert ll.size == 1

    def test_insert_tail(self):
        ll = LinkedList()
        ll.insert_head(10)
        ll.insert_tail(20)
        assert ll.get_tail().get_data() == 20
        assert ll.size == 2

    def test_remove_first(self):
        ll = LinkedList()
        ll.insert_head(10)
        ll.insert_head(20)
        ll.remove_first()
        assert ll.get_head().get_data() == 10
        assert ll.size == 1

    def test_is_empty(self):
        ll = LinkedList()
        assert ll.is_empty()
        ll.insert_head(10)
        assert not ll.is_empty()

    def test_size(self):
        ll = LinkedList()
        assert ll.size == 0
        ll.insert_head(10)
        assert ll.size == 1
        ll.insert_tail(20)
        assert ll.size == 2

    def test_get_head(self):
        ll = LinkedList()
        ll.insert_head(10)
        assert ll.get_head().get_data() == 10

    def test_get_tail(self):
        ll = LinkedList()
        ll.insert_head(10)
        ll.insert_tail(20)
        assert ll.get_tail().get_data() == 20

    def test_clear(self):
        ll = LinkedList()
        ll.insert_head(10)
        ll.insert_tail(20)
        ll.clear()
        assert ll.is_empty()
        assert ll.size == 0


if __name__ == "__main__":
    pytest.main()
