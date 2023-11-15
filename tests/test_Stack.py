import os
import sys
import unittest

# Add the path to the src directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

from cisc0503_dsa import Stack, BoundStack, ThresholdStack, DoublePopStack

class StackTest(unittest.TestCase):
    """Test the base Stack class"""

    def setUp(self):
        """ Create a Stack object. """
        self.stack = Stack()
        self.empty_stack = Stack()
        for value in [1, 9, 2, 8]:
            self.stack.push(value)

    def test_cannot_access_elements_directly(self):
        with self.assertRaises(Exception):
            self.stack.elements

    def test_is_empty(self):
        self.assertFalse(self.stack.is_empty())
        self.assertTrue(self.empty_stack.is_empty())

    def test_is_full(self):
        self.assertFalse(self.stack.is_full())
        self.assertFalse(self.empty_stack.is_full())

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 8)
        self.assertEqual(self.empty_stack.peek(), None)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 8)
        self.assertEqual(self.empty_stack.pop(), None)

    def test_push(self):
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 3)

    def test_size(self):
        self.assertEqual(self.stack.get_size(), 4)
        self.assertEqual(self.empty_stack.get_size(), 0)

class BoundStackTest(unittest.TestCase):
    def setUp(self):
        """ Create a Stack object. """
        self.stack = BoundStack(10)
        for value in [1, 9, 2, 8]:
            self.stack.push(value)
        
        self.empty_stack = BoundStack(10)

    def test_size_must_be_positive(self):
        with self.assertRaises(Exception):
            BoundStack(0)
        with self.assertRaises(Exception):
            BoundStack(-1)

    def test_is_empty(self):
        self.assertFalse(self.stack.is_empty())
        self.assertTrue(self.empty_stack.is_empty())

    def test_is_full(self):
        self.assertFalse(self.stack.is_full())
        fullStack = BoundStack(4)
        for value in [1, 9, 2, 8]:
            fullStack.push(value)
        self.assertTrue(fullStack.is_full())

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 8)
        self.assertEqual(self.empty_stack.peek(), None)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 8)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.empty_stack.pop(), None)

    def test_push(self):
        self.stack = BoundStack(3)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
        with self.assertRaises(Exception):
            self.stack.push(1)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 5)

    def test_size(self):
        self.assertEqual(self.stack.get_size(), 4)
        self.assertEqual(self.empty_stack.get_size(), 0)

class ThresholdStackTest(unittest.TestCase):
    def setUp(self):
        self.stack = ThresholdStack(20, 100)
        # add 10 items to the stack in mixed order:
        # - 3 above the threshold
        # - 7 below the threshold
        for value in [1, 9, 2, 8, 100, 900, 200, 800, 40, 0]:
            self.stack.push(value)
        self.empty_stack = ThresholdStack(20, 100)

    def test_size_must_be_positive(self):
        with self.assertRaises(Exception):
            ThresholdStack(0, 100)
        with self.assertRaises(Exception):
            ThresholdStack(-1, 100)

    def test_cannot_pop_without_specifying_stack(self):
        with self.assertRaises(Exception):
            self.stack.pop()

    def test_can_push_to_both_stacks(self):
        self.stack.push(5)
        self.empty_stack.push(1)

    def test_cant_push_to_full_stack(self):
        size = 2
        stack = ThresholdStack(size, 100)
        stack.push(1)
        stack.push(2)
        with self.assertRaises(Exception):
            stack.push(3)

    def test_get_sizes(self):
        self.assertEqual(self.stack.get_size2(), 3)
        self.assertEqual(self.stack.get_size1(), 7)
        self.assertEqual(self.stack.get_size(), 10)
        self.assertEqual(len(self.stack), self.stack.get_size())

        threshold = 100
        stack = ThresholdStack(10, threshold)
        self.assertEqual(stack.get_size1(), 0)
        self.assertEqual(stack.get_size2(), 0)
        self.assertEqual(stack.get_size2(), 0)
        self.assertEqual(len(stack), stack.get_size())
        stack.push(threshold)

        self.assertEqual(stack.get_size1(), 1)
        self.assertEqual(stack.get_size2(), 0)
        self.assertEqual(stack.get_size(), 1)
        self.assertEqual(len(stack), stack.get_size())

    def test_is_empty(self):
        self.assertFalse(self.stack.is_empty())
        self.assertTrue(self.empty_stack.is_empty())
    
    def test_is_full(self):
        self.assertFalse(self.stack.is_full())
        self.assertFalse(self.empty_stack.is_full())
        even_full_stack = ThresholdStack(4, 100)
        odd_full_stack = ThresholdStack(5, 100)
        for value in [1, 9, 200, 800]:
            even_full_stack.push(value)
            odd_full_stack.push(value)

        self.assertTrue(even_full_stack.is_full())
        self.assertFalse(odd_full_stack.is_full())

        even_full_stack.pop1()
        odd_full_stack.push(-1)

        self.assertFalse(even_full_stack.is_full())
        self.assertTrue(odd_full_stack.is_full())

    def test_all(self):
        """
        - Test that we keep track of pointers accurately
        - Test that size and threshold do not affect the behavior of stack operations
        - Test that we can push and pop from both stacks until they are full but no
        further than that
        - Test that when one stack is full, we cannot push to either stack, but the
          other stack is empty.
            - Since the other stack is empty, we can't pop from it
            - Since one stack is full, the entire array is full
        """
        for threshold in [0, -100, 100]:
            for size in [4, 5]:
                stack = ThresholdStack(size, threshold)
                self.assertEqual(stack._top, 0)
                self.assertEqual(stack._top2, size-1)

                # Push `size` items above the threshold onto the stack
                for i, n in enumerate(range(threshold + 1, threshold + size + 1)):
                    i = i + 1 # enumerate() is 0-based, so add 1
                    stack.push(n)
                    self.assertEqual(stack._top, 0)
                    self.assertEqual(stack._top2, size-i-1) 
                
                # Stack is full, we can't push anymore
                with self.assertRaises(Exception):
                    stack.push(threshold)
                with self.assertRaises(Exception):
                    stack.push(threshold +1)
                self.assertTrue(stack.is_full())

                # Can't pop from the lower stack
                self.assertIsNone(stack.pop1())
                # ...because it's empty
                self.assertTrue(stack.is_empty1())
                # ...but the combined stack is not empty
                self.assertFalse(stack.is_empty())
                
                # Pop `size` items off the upper stack
                for i in range(size):
                    self.assertNotEqual(None, stack.pop2())

                # Push `size` items *at* and below the threshold onto the stack
                for i, n in enumerate(range(threshold - size, threshold)):
                    i = i + 1 # enumerate() is 0-based, so add 1
                    stack.push(n)
                    self.assertEqual(stack._top, i)
                    self.assertEqual(stack._top2, size-1)

                # Stack is full, we can't push anymore
                with self.assertRaises(Exception):
                    stack.push(threshold)
                with self.assertRaises(Exception):
                    stack.push(threshold+1)
                self.assertTrue(stack.is_full())

                # Can't pop from the upper stack
                self.assertIsNone(stack.pop2())
                # ...because it's empty
                self.assertTrue(stack.is_empty2())
                # ...but the combined stack is not empty
                self.assertFalse(stack.is_empty())

                # Pop `size` items off the lower stack
                for i in range(size):
                    self.assertNotEqual(None, stack.pop1())

    def test_pops_simple(self):
        self.assertEqual(self.stack.pop2(), 800)
        self.assertEqual(self.stack.pop2(), 200)
        self.assertEqual(self.stack.pop2(), 900)
        self.assertEqual(self.stack.pop2(), None)

        self.assertEqual(self.stack.pop1(), 0)
        self.assertEqual(self.stack.pop1(), 40)
        self.assertEqual(self.stack.pop1(), 100)
        self.assertEqual(self.stack.pop1(), 8)
        self.assertEqual(self.stack.pop1(), 2)
        self.assertEqual(self.stack.pop1(), 9)
        self.assertEqual(self.stack.pop1(), 1)
        self.assertEqual(self.stack.pop1(), None)

    def test_is_empties(self):
        self.assertFalse(self.stack.is_empty1())
        self.assertFalse(self.stack.is_empty2())
        self.assertFalse(self.stack.is_empty())
        self.assertTrue(self.empty_stack.is_empty1())
        self.assertTrue(self.empty_stack.is_empty2())
        self.assertTrue(self.empty_stack.is_empty())

        for i in range(self.stack.get_size1()):
            self.assertNotEqual(None, self.stack.pop1())

        self.assertTrue(self.stack.is_empty1())
        
        for i in range(self.stack.get_size2()):
            self.assertNotEqual(None, self.stack.pop2())

        self.assertTrue(self.stack.is_empty2())
    
class DoublePopStackTest(unittest.TestCase):

    def setUp(self):
        self.stack = DoublePopStack()
        for value in [5, 1, 9, 2, 8]:
            self.stack.push(value)

    def test_double_pop(self):
        self.assertEqual(self.stack.pop(), (8, 2))
        self.assertEqual(self.stack.pop(), (9, 1))
        self.assertEqual(self.stack.pop(), (5, None))
        self.assertEqual(self.stack.pop(), (None, None))

    def test_is_empty(self):
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.stack.pop()
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
        
if __name__ == "__main__": # pragma: no cover
    unittest.main()
