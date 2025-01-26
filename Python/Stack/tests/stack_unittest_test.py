import unittest

from ..src.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        value = self.stack.pop()
        self.assertEqual(value, 2)
        self.assertEqual(self.stack.size, 1)

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        value = self.stack.peek()
        self.assertEqual(value, 2)
        self.assertEqual(self.stack.size, 2)

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.size, 1)

    def test_push_and_peek(self):
        stack = Stack()
        stack.push(10)
        self.assertEqual(stack.peek(), 10)
        stack.push(20)
        self.assertEqual(stack.peek(), 20)

    def test_size(self):
        self.assertEqual(self.stack.size, 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size, 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size, 2)
        self.stack.pop()
        self.assertEqual(self.stack.size, 1)

    def test_empty(self):
        self.assertTrue(self.stack.empty())
        self.stack.push(1)
        self.assertFalse(self.stack.empty())
        self.stack.pop()
        self.assertTrue(self.stack.empty())

    def test_pop_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_large_number_of_elements(self):
        stack = Stack()
        for i in range(1000):
            stack.push(i)
        self.assertEqual(stack.size, 1000)
        for i in reversed(range(1000)):
            self.assertEqual(stack.pop(), i)
        self.assertEqual(stack.size, 0)

    def test_push_multiple(self):
        for i in range(5):
            self.stack.push(i)
        self.assertEqual(self.stack.size, 5)
        self.assertEqual(self.stack.peek(), 4)

    def test_initialize_with_data(self):
        stack = Stack(10)
        self.assertEqual(stack.peek(), 10)
        self.assertEqual(stack.size, 1)

    def test_arg_parameters(self):
        stack = Stack(1, 2, 3, 4, 5)
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.size, 5)
        for i in reversed(range(5)):
            self.assertEqual(stack.pop(), i + 1)
        self.assertTrue(stack.empty())

    def test_arg_push(self):
        stack = Stack()
        stack.push(1, 2, 3, 4, 5)
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.size, 5)
        for i in reversed(range(5)):
            self.assertEqual(stack.pop(), i + 1)
        self.assertTrue(stack.empty())

    def test_length(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(len(self.stack), 3)
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(len(self.stack), 1)
        self.stack.pop()
        self.assertEqual(len(self.stack), 0)

    def test_bool(self):
        self.assertFalse(bool(self.stack))
        self.stack.push(1)
        self.assertTrue(bool(self.stack))
        self.stack.pop()
        self.assertFalse(bool(self.stack))

    def test_equality(self):
        integer = 5
        self.stack.push(5)
        self.assertNotEqual(self.stack, integer)
        other = Stack(5)
        self.assertEqual(self.stack, other)

    def test_iteration(self):
        self.stack.push(0, 1, 2, 3, 4)
        for item, i in zip(self.stack, reversed(range(5))):
            self.assertEqual(item, i)

    def test_peek_on_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_single_element_stack(self):
        stack = Stack(1)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.size, 1)
        stack.pop()
        self.assertTrue(stack.empty())

    def test_max_size(self):
        max_size_stack = Stack(1, 2, 3, max_size=3)
        self.assertEqual(max_size_stack.size, 3)
        with self.assertRaises(IndexError):
            max_size_stack.push(4)

    def test_pop_and_push_with_max_size(self):
        max_size_stack = Stack(1, 2, 3, max_size=3)
        max_size_stack.pop()
        max_size_stack.push(4)
        self.assertEqual(max_size_stack.size, 3)
        self.assertEqual(max_size_stack.peek(), 4)

    def test_large_number_of_elements_with_max_size(self):
        max_size_stack = Stack(max_size=1000)
        for i in range(1000):
            max_size_stack.push(i)
        self.assertEqual(max_size_stack.size, 1000)
        with self.assertRaises(IndexError):
            max_size_stack.push(1001)

    def test_iteration_empty_stack(self):
        for item in self.stack:
            self.fail("Iteration should not yield any items")

    def test_threaded_push_pop(self):
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
        self.assertEqual(stack.size, 0)

if __name__ == '__main__':
    unittest.main()