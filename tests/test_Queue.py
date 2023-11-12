import os
import sys
import unittest

# Add the path to the src directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

from cisc0503_dsa import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        for i in [1, 9, 2, 8]:
            self.queue.enqueue(i)
        self.empty_queue = Queue()

    def test_queue(self):
        # Test the queue
        self.queue.enqueue(3)
        self.empty_queue.enqueue(1)

    def test_dequeue(self):
        # Test the dequeue method
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 9)
        self.assertIsNone(self.empty_queue.dequeue())

    def test_size(self):
        # Test the size method
        self.assertEqual(self.queue.get_size(), 4)
        self.assertEqual(self.empty_queue.get_size(), 0)
        self.assertEqual(len(self.queue), self.queue.get_size())
        self.assertEqual(len(self.empty_queue), self.empty_queue.get_size())

    def test_peek(self):
        # Test the peek method
        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.empty_queue.peek(), None)
    
