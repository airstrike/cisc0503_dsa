import os
import sys
import unittest

# Add the path to the src directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

from cisc0503_dsa import LinkedList, DoublyLinkedList

class LinkedListTest(unittest.TestCase):
    """Test the LinkedList class"""

    def setUp(self):
        self.ll = LinkedList()
        for i in range(10):
            self.ll.insert_last(i)

        # modify the 2nd item to equal the first
        self.ll.set(1, 0)
        
        self.empty_ll = LinkedList()

    def test_insert_first(self):
        self.ll.insert_first(100)
        self.assertEqual(self.ll.get_size(), 11)
        self.assertEqual(self.ll.get_first(), 100)

    def test_insert_last(self):
        self.ll.insert_last(100)
        self.assertEqual(self.ll.get_size(), 11)
        self.assertEqual(self.ll.get_last(), 100)

    def test_traverse(self):
        self.assertEqual(len([node for node in self.ll.traverse()]), self.ll.get_size())
        self.assertEqual([node for node in self.ll.traverse()], [0,0,2,3,4,5,6,7,8,9])
        self.assertEqual([node for node in self.ll], [0,0,2,3,4,5,6,7,8,9])

        self.ll.remove(4)
        self.assertEqual(len([node for node in self.ll.traverse()]), self.ll.get_size())
        self.assertEqual([node for node in self.ll.traverse()], [0,0,2,3,5,6,7,8,9])
        self.assertEqual([node for node in self.ll], [0,0,2,3,5,6,7,8,9])

    def test_get_size(self):
        self.assertEqual(self.ll.get_size(), 10)
        self.assertEqual(self.empty_ll.get_size(), 0)
        self.assertEqual(len(self.ll), 10)
        self.assertEqual(len(self.empty_ll), 0)

    def test_is_empty(self):
        self.assertFalse(self.ll.is_empty())
        self.assertTrue(self.empty_ll.is_empty())

    def test_insert(self):
        self.ll.insert(0, 100)
        self.assertEqual(self.ll.get_size(), 11)
        self.assertEqual(self.ll.get_first(), 100)

        self.ll.insert(5, 100)
        self.assertEqual(self.ll.get_size(), 12)
        self.assertEqual(self.ll.get(5), 100)

        self.ll.insert(12, 100)
        self.assertEqual(self.ll.get_size(), 13)
        self.assertEqual(self.ll.get_last(), 100)

        # test calling insert() at the first index
        self.ll.insert(0, 200)

        # test calling insert() at the last index
        self.ll.insert(13, 300)

        # test calling insert() on first index of empty list
        self.empty_ll.insert(0, 100)

    def test_remove(self):
        self.ll.remove(0)
        self.assertEqual(self.ll.get_size(), 9)
        self.assertEqual(self.ll.get_first(), 0)

        self.ll.remove(8) # actually removes the element with value `9`
        self.assertEqual(self.ll.get_size(), 8)
        self.assertEqual(self.ll.get_last(), 8)

        self.ll.remove(4) # actually removes the element with value `5`
        self.assertEqual(self.ll.get_size(), 7)
        self.assertEqual(self.ll.get(4), 6)

        # test calling remove() at the first index
        self.assertTrue(self.ll.remove(0))

        # test calling remove() at the last element
        self.assertTrue(self.ll.remove(len(self.ll) - 1))

        # test calling remove*() on first/last index of empty list
        self.assertFalse(self.empty_ll.remove(0))
        self.assertFalse(self.empty_ll.remove_first())
        self.assertFalse(self.empty_ll.remove_last())

        # test calling remove_last() on single element list
        self.empty_ll.insert_last(100)
        self.assertTrue(self.empty_ll.remove_last())

    def test_set(self):
        self.ll.set(0, 100)
        self.assertEqual(self.ll.get(0), 100)

        self.ll.set(9, 100)
        self.assertEqual(self.ll.get(9), 100)

        self.ll.set(4, 100)
        self.assertEqual(self.ll.get(4), 100)

        # test calling set() on empty list
        self.empty_ll.set(0, 100)

    def test_get(self):
        self.assertEqual(self.ll.get(0), 0)
        self.assertEqual(self.ll.get(9), 9)
        self.assertEqual(self.ll.get(4), 4)
        self.assertEqual(self.ll.get(5), self.ll[5])
        self.assertIsNone(self.ll.get(100))
        self.assertIsNone(self.ll[200])

        # test get_first and get_last
        self.assertEqual(self.ll.get(0), self.ll.get_first())
        self.assertEqual(self.ll.get_first(), 0)
        self.assertEqual(self.ll.get(9), self.ll.get_last())
        self.assertEqual(self.ll.get_last(), 9)

        # test get, get_first and get_last on empty list
        self.assertIsNone(self.empty_ll.get(0))
        self.assertIsNone(self.empty_ll.get_first())
        self.assertIsNone(self.empty_ll.get_last())

    def test_equality(self):
        mostly_equal = LinkedList()
        for i in range(10):
            mostly_equal.insert_last(i)
        self.assertNotEqual(self.ll, mostly_equal)
        mostly_equal.set(1, 0) # make the 2nd item equal to the first
        self.assertEqual(self.ll, mostly_equal)

        self.assertEqual(self.empty_ll, LinkedList())
        self.assertNotEqual(self.ll, self.empty_ll)

    def test_copies(self):
        self.assertEqual(self.ll.copy(), self.ll)

    def test_insertions_change_size(self):
        self.assertEqual(self.ll.get_size(), 10)
        self.ll.insert_first(100)
        self.assertEqual(self.ll.get_size(), 11)
        self.ll.insert_last(100)
        self.assertEqual(self.ll.get_size(), 12)
        self.ll.insert(0, 100)
        self.assertEqual(self.ll.get_size(), 13)
        self.ll.insert(5, 100)
        self.assertEqual(self.ll.get_size(), 14)

    def test_removals_change_size(self):
        self.assertEqual(self.ll.get_size(), 10)
        self.ll.remove(0)
        self.assertEqual(self.ll.get_size(), 9)
        self.ll.remove(8)
        self.assertEqual(self.ll.get_size(), 8)
        self.ll.remove(4)
        self.assertEqual(self.ll.get_size(), 7)

    def test_contains(self):
        self.assertTrue(self.ll.contains(0))
        self.assertTrue(self.ll.contains(9))
        self.assertTrue(self.ll.contains(4))
        self.assertFalse(self.ll.contains(100))
        self.assertFalse(self.empty_ll.contains(100))
    
    def test_index(self):
        self.assertEqual(self.ll.index(0), 0)
        self.assertEqual(self.ll.index(9), 9)
        self.assertEqual(self.ll.index(4), 4)
        self.assertEqual(self.ll.index(100), -1)
        self.assertEqual(self.empty_ll.index(100), -1)

        # test indexOf
        self.assertEqual(self.ll.indexOf(0), self.ll.index(0))

        # test index in opposite direction
        self.assertEqual(self.ll.index(0, reverse=True), 1)

    def test_last_indexOf(self):
        self.assertEqual(self.ll.lastIndexOf(0), 1)
        self.assertEqual(self.ll.lastIndexOf(9), 9)
        self.assertEqual(self.ll.lastIndexOf(4), 4)
        self.assertEqual(self.ll.lastIndexOf(100), -1)
        self.assertEqual(self.empty_ll.lastIndexOf(100), -1)

class DoublyLinkedListTest(LinkedListTest):
    """Inherits from LinkedListTest and overrides the setUp() method to use a DoublyLinkedList
    """

    def setUp(self):
        self.ll = DoublyLinkedList()
        for i in range(10):
            self.ll.insert_last(i)

        # modify the 2nd item to equal the first
        self.ll.set(1, 0)
        
        self.empty_ll = DoublyLinkedList()

    def test_traverse_reverse(self):
        self.assertEqual(len([node for node in self.ll.traverse(reverse=True)]), self.ll.get_size())
        self.assertEqual([node for node in self.ll.traverse(reverse=True)], [9,8,7,6,5,4,3,2,0,0])
        self.assertEqual([node for node in self.ll], [0,0,2,3,4,5,6,7,8,9])

        self.ll.remove(4)
        self.assertEqual(len([node for node in self.ll.traverse(reverse=True)]), self.ll.get_size())
        self.assertEqual([node for node in self.ll.traverse(reverse=True)], [9,8,7,6,5,3,2,0,0])
        self.assertEqual([node for node in self.ll], [0,0,2,3,5,6,7,8,9])