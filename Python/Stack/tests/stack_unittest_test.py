import unittest

from ..src.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_and_peek(self):
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)

    def test_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        value = self.stack.pop()
        self.assertEqual(value, 20)
        self.assertEqual(self.stack.peek(), 10)

    def test_size(self):
        self.assertEqual(self.stack.size, 0)
        self.stack.push(10)
        self.assertEqual(self.stack.size, 1)
        self.stack.push(20)
        self.assertEqual(self.stack.size, 2)
        self.stack.pop()
        self.assertEqual(self.stack.size, 1)

    def test_empty(self):
        self.assertTrue(self.stack.empty())
        self.stack.push(10)
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
        for i in range(1000):  # Push a large number of elements
            self.stack.push(i)
        self.assertEqual(self.stack.size, 1000)
        for i in reversed(range(1000)):  # Pop all elements and verify
            self.assertEqual(self.stack.pop(), i)
        self.assertEqual(self.stack.size, 0)

    def test_initialize_with_data(self):
        stack = Stack(10)
        self.assertEqual(stack.peek(), 10)
        self.assertEqual(stack.size, 1)

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.size, 1)

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        value = self.stack.peek()
        self.assertEqual(value, 2)
        self.assertEqual(self.stack.size, 2)

    def test_push_multiple(self):
        for i in range(5):
            self.stack.push(i)
        self.assertEqual(self.stack.size, 5)
        self.assertEqual(self.stack.peek(), 4)

if __name__ == '__main__':
    unittest.main()