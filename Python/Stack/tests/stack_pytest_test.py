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
    assert stack.size == 1


def test_peek(stack):
    stack.push(1)
    stack.push(2)
    value = stack.peek()
    assert value == 2
    assert stack.size == 2


def test_push(stack):
    stack.push(1)
    assert stack.size == 1


def test_push_and_peek():
    stack = Stack()
    stack.push(10)
    assert stack.peek() == 10
    stack.push(20)
    assert stack.peek() == 20


def test_size(stack):
    assert stack.size == 0
    stack.push(1)
    assert stack.size == 1
    stack.push(2)
    assert stack.size == 2
    stack.pop()
    assert stack.size == 1


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
    assert stack.size == 1000
    for i in reversed(range(1000)):
        assert stack.pop() == i
    assert stack.size == 0


def test_push_multiple(stack):
    for i in range(5):
        stack.push(i)
    assert stack.size == 5
    assert stack.peek() == 4


def test_initialize_with_data():
    stack = Stack(10)
    assert stack.peek() == 10
    assert stack.size == 1


def test_arg_parameters():
    stack = Stack(1, 2, 3, 4, 5)
    assert stack.peek() == 5
    assert stack.size == 5
    for i in reversed(range(5)):
        assert stack.pop() == i + 1
    assert stack.empty()


def test_arg_push():
    stack = Stack()
    stack.push(1, 2, 3, 4, 5)
    assert stack.peek() == 5
    assert stack.size == 5
    for i in reversed(range(5)):
        assert stack.pop() == i + 1
    assert stack.empty()


def test_length(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert len(stack) == 3
    stack.pop()
    stack.pop()
    assert len(stack) == 1
    stack.pop()
    assert len(stack) == 0


def test_bool(stack):
    assert not bool(stack)
    stack.push(1)
    assert bool(stack)
    stack.pop()
    assert not bool(stack)


def test_equality(stack):
    integer = 5
    stack.push(5)
    assert stack != integer
    other = Stack(5)
    assert stack == other


def test_iteration(stack):
    stack.push(0, 1, 2, 3, 4)
    for item, i in zip(stack, reversed(range(5))):
        assert item == i


def test_peek_on_empty_stack(stack):
    with pytest.raises(IndexError):
        stack.peek()


def test_single_element_stack():
    stack = Stack(1)
    assert stack.peek() == 1
    assert stack.size == 1
    stack.pop()
    assert stack.empty()


def test_max_size(stack):
    max_size_stack = Stack(1, 2, 3, max_size=3)
    assert max_size_stack.size == 3

    with pytest.raises(IndexError, match="Stack has reached it's max size"):
        max_size_stack.push(4)


def test_pop_and_push_with_max_size():
    max_size_stack = Stack(1, 2, 3, max_size=3)
    max_size_stack.pop()
    max_size_stack.push(4)
    assert max_size_stack.size == 3
    assert max_size_stack.peek() == 4


def test_large_number_of_elements_with_max_size():
    max_size_stack = Stack(max_size=1000)

    for i in range(1000):
        max_size_stack.push(i)

    assert max_size_stack.size == 1000

    with pytest.raises(IndexError):
        max_size_stack.push(1001)


def test_iteration_empty_stack(stack):
    for item in stack:
        assert False, "Iteration should not yield any items"


def test_threaded_push_pop():
    import threading
    stack = Stack(max_size=10)

    def push_elements():
        for i in range(5):
            stack.push(i)

    def pop_elements():
        for i in range(5):
            stack.pop()

    thread1 = threading.Thread(target=push_elements)
    thread2 = threading.Thread(target=pop_elements)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # The final stack size should be 0
    assert stack.size == 0
