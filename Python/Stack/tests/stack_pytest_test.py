import pytest

from ..src.stack import Stack



@pytest.fixture
def stack():
    return Stack()


def test_pop(stack):
    stack.push(1)
    stack.push(2)
    value = stack.pop()
    assert value == 2
    assert stack.size() == 1


def test_peek(stack):
    stack.push(1)
    stack.push(2)
    value = stack.peek()
    assert value == 2
    assert stack.size() == 2


def test_push(stack):
    stack.push(1)
    assert stack.size() == 1


def test_push_and_peek():
    stack = Stack()
    stack.push(10)
    assert stack.peek() == 10
    stack.push(20)
    assert stack.peek() == 20


def test_size(stack):
    assert stack.size() == 0
    stack.push(1)
    assert stack.size() == 1
    stack.push(2)
    assert stack.size() == 2
    stack.pop()
    assert stack.size() == 1


def test_empty(stack):
    assert stack.empty()
    stack.push(1)
    assert not stack.empty()
    stack.pop()
    assert stack.empty()


def test_pop_empty_stack(stack):
    with pytest.raises(IndexError):
        stack.pop()


def test_peek_empty_stack(stack):
    with pytest.raises(IndexError):
        stack.peek()


def test_large_number_of_elements():
    stack = Stack()
    for i in range(1000):
        stack.push(i)
    assert stack.size() == 1000
    for i in reversed(range(1000)):
        assert stack.pop() == i
    assert stack.size() == 0


def test_push_multiple(stack):
    for i in range(5):
        stack.push(i)
    assert stack.size() == 5
    assert stack.peek() == 4


def test_initialize_with_data():
    stack = Stack(data=10)
    assert stack.peek() == 10
    assert stack.size() == 1
