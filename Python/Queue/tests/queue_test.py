import pytest
from ..src.queue import Queue  # Assuming your class is in queue_implementation.py


def test_enqueue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.size == 2
    assert q.peek() == 1  # First element should be 1


def test_dequeue():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.dequeue() == 10  # First in, first out
    assert q.size == 1
    assert q.dequeue() == 20
    assert q.is_empty()


def test_dequeue_empty():
    q = Queue()
    with pytest.raises(IndexError, match="Dequeue from an empty queue"):
        q.dequeue()


def test_peek():
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    assert q.peek() == "A"  # Should return front element without removing it
    assert q.size == 2  # Size should remain the same


def test_peek_empty():
    q = Queue()
    with pytest.raises(IndexError, match="Peek from an empty queue"):
        q.peek()


def test_is_empty():
    q = Queue()
    assert q.is_empty()  # New queue should be empty
    q.enqueue(5)
    assert not q.is_empty()


def test_size():
    q = Queue()
    assert q.size == 0
    q.enqueue(100)
    q.enqueue(200)
    assert q.size == 2
    q.dequeue()
    assert q.size == 1


def test_clear():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.clear()
    assert q.is_empty()
    assert q.size == 0


def test_to_list():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.to_list() == [1, 2, 3]
