import os
import sys
import unittest

# Add the path to the src directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

from cisc0503_dsa import LinkedList

class LinkedListTest(unittest.TestCase):
    """Test the LinkedList class"""

    def setUp(self):
        self.ll = LinkedList()
        for i in range(10):
            self.ll.insert_last(i)
        
        self.empty_ll = LinkedList()
