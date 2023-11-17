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
            self.ll.add_last(i)

        # modify the 2nd item to equal the first
        self.ll.set(1, 0)

        # the resulting will look like:
        # LinkedList([0, 0, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(f'{self.ll}', 'LinkedList([0, 0, 2, 3, 4, 5, 6, 7, 8, 9])')
        
        self.empty_ll = LinkedList()

    def test_add_first(self):
        self.ll.add_first(100)
        self.assertEqual(self.ll.get_size(), 11)
        self.assertEqual(self.ll.get_first(), 100)

    def test_add_last(self):
        self.ll.add_last(100)
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

    def test_add(self):
        self.ll.insert(0, 100)
        self.assertEqual(self.ll.get_size(), 11)
        self.assertEqual(self.ll.get_first(), 100)

        self.ll.insert(5, 100)
        self.assertEqual(self.ll.get_size(), 12)
        self.assertEqual(self.ll.get(5), 100)

        self.ll.insert(12, 100)
        self.assertEqual(self.ll.get_size(), 13)
        self.assertEqual(self.ll.get_last(), 100)

        # test calling add() at the first index
        self.ll.insert(0, 200)

        # test calling add() at the last index
        self.ll.insert(13, 300)

        # test calling add() on first index of empty list
        self.empty_ll.insert(0, 100)

    def test_remove(self):
        self.ll.remove(0)
        self.assertEqual(self.ll.get_size(), 9)
        self.assertEqual(self.ll.get_first(), 0)

        self.ll.remove(9) # actually removes the element with value `9`
        self.assertEqual(self.ll.get_size(), 8)
        self.assertEqual(self.ll.get_last(), 8)

        self.ll.remove(4) # actually removes the element with value `5`
        self.assertEqual(self.ll.get_size(), 7)
        self.assertEqual(self.ll.get(4), 6)

        # test calling remove() at the first index
        self.assertEqual(self.ll.removeAt(0), 0)

        # test calling remove() at the last element
        last = self.ll[len(self.ll) - 1]

        self.assertEqual(self.ll.removeAt(len(self.ll) - 1), last)

        # test calling remove*() on first/last index of empty list
        self.assertFalse(self.empty_ll.removeAt(0))
        self.assertFalse(self.empty_ll.remove_first())
        self.assertFalse(self.empty_ll.remove_last())

        # test calling remove_last() on single element list/pdb
        
        self.empty_ll.add_last(100)
        self.assertEqual(self.empty_ll.remove_last(), 100)

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
        mostly_equal = self.ll.__class__() # make a copy of self.ll, whatever type it is
        for i in range(10):
            mostly_equal.add_last(i)
        self.assertNotEqual(self.ll, mostly_equal)
        mostly_equal.set(1, 0) # make the 2nd item equal to the first
        self.assertEqual(self.ll, mostly_equal)

        self.assertEqual(self.empty_ll, LinkedList())
        self.assertNotEqual(self.ll, self.empty_ll)

    def test_copies(self):
        self.assertEqual(self.ll.copy(), self.ll)

    def test_addions_change_size(self):
        self.assertEqual(self.ll.get_size(), 10)
        self.ll.add_first(100)
        self.assertEqual(self.ll.get_size(), 11)
        self.ll.add_last(100)
        self.assertEqual(self.ll.get_size(), 12)
        self.ll.insert(0, 100)
        self.assertEqual(self.ll.get_size(), 13)
        self.ll.insert(5, 100)
        self.assertEqual(self.ll.get_size(), 14)

    def test_removals_change_size(self):
        self.assertEqual(self.ll.get_size(), 10)
        self.ll.remove(0) # removes the element with value `0`
        self.assertEqual(self.ll.get_size(), 9)
        self.ll.removeAt(8)
        self.assertEqual(self.ll.get_size(), 8)
        self.ll.removeAt(4)
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

    def test_clear(self):
        self.ll.clear()
        self.assertEqual(self.ll.get_size(), 0)
        self.assertEqual(self.ll.get_first(), None)
        self.assertEqual(self.ll.get_last(), None)

        self.empty_ll.clear()
        self.assertEqual(self.empty_ll.get_size(), 0)

    def test_get_node(self):
        self.assertEqual(self.ll.get_node(0).element, 0)
        self.assertEqual(self.ll.get_node(10000), None)

class DoublyLinkedListTest(LinkedListTest):
    """Inherits from LinkedListTest and overrides the setUp() method to use a DoublyLinkedList
    """

    def setUp(self):
        self.ll = DoublyLinkedList()
        for i in range(10):
            self.ll.add_last(i)

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

class MidtermTests(unittest.TestCase):

    def test_midterm_tests(self):
        lst = LinkedList()
        print("\nMIDTERM TESTS:")
        print(lst.isEmpty())
     
        print(lst.countList() == 0)
        lst.add(1) 
        lst.add(2) 
        lst.add(3) 
        print(lst.countList() == 3)
        lst.add(-3)
        print(lst.countList() == 4)

    
        print(lst)
        print(not lst.isEmpty())

        print()
        

        lst.removeFirst()
        print(lst)

        lst.addLast(99)
        print(lst)

        lst.addFirst(9)
        print(lst)

        print(lst.countList() == 5)

class Assignment4Tests(unittest.TestCase):

    def setUp(self):
        self.sll = LinkedList()
        self.dll = DoublyLinkedList()
        for ll in [self.sll, self.dll]:
            ll.add("a")
            ll.add(1)
            ll.add(-1)

    def test_contains(self):
        # Return True if this list contains the element otherwise False
        for ll in [self.sll, self.dll]:
            self.assertTrue(ll.contains("a"))
            self.assertFalse(ll.contains(100))
            self.assertTrue(ll.contains(1))
            self.assertTrue(ll.contains(-1))

    def test_remove(self):
        # Remove the element and return True if the element is in the list 
        for ll in [self.sll, self.dll]:
            self.assertTrue(ll.remove("a"))
            self.assertFalse(ll.remove("a")) # should be false since we already removed "a"
            self.assertFalse(ll.contains("a")) # should be false since we already removed "a"

            self.assertFalse(ll.remove(100))
            self.assertTrue(ll.remove(1))
            self.assertTrue(ll.remove(-1))

    def test_get(self):
        # Return the element from this list at the specified index otherwise None
        for ll in [self.sll, self.dll]:
            self.assertEqual(ll.get(0), "a")
            self.assertEqual(ll.get(1), 1)
            self.assertEqual(ll.get(2), -1)

            self.assertIsNone(ll.get(3))
            self.assertIsNone(ll.get(-1))

    def test_indexOf(self):
        # Return the index of the head matching element in this list.
        # Return -1 if no match.
        for ll in [self.sll, self.dll]:
            self.assertEqual(ll.indexOf("a"), 0)
            self.assertEqual(ll.indexOf(1), 1)
            self.assertEqual(ll.indexOf(-1), 2)

            ll.add("a")
            self.assertEqual(ll.indexOf("a"), 0)

            self.assertEqual(ll.indexOf(100), -1)

    def test_lastIndexOf(self):
        # Return the index of the last matching element in this list
        #  Return -1 if no match. 
        for ll in [self.sll, self.dll]:
            self.assertEqual(ll.lastIndexOf("a"), 0)
            self.assertEqual(ll.lastIndexOf(1), 1)
            self.assertEqual(ll.lastIndexOf(-1), 2)

            ll.add("a")
            self.assertEqual(ll.lastIndexOf("a"), 3)

            self.assertEqual(ll.lastIndexOf(100), -1)

    def test_set(self):
        # Replace the element at the specified position in this list
        #  with the specified element. */
        for ll in [self.sll, self.dll]:
            ll.set(0, "b")
            ll.set(1, 1) # set it to the same value
            ll.set(2, -2)

            self.assertEqual(ll.get(0), "b")
            self.assertEqual(ll.get(1), 1)
            self.assertEqual(ll.get(2), -2)

            self.assertFalse(ll.contains("a"))
            self.assertTrue(ll.contains("b"))
            self.assertTrue(ll.contains(1))
            self.assertFalse(ll.contains(-1))
            self.assertTrue(ll.contains(-2))

            self.assertEqual(ll.indexOf("b"), 0)
            self.assertEqual(ll.lastIndexOf("b"), 0)
            self.assertEqual(ll.indexOf(-1), -1)

            self.assertEqual(ll._size, 3)

class ExtensiveLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.sll = LinkedList()
        self.dll = DoublyLinkedList()

    def test_extensive_operations(self):
        # Initialize LinkedList
        for ll in [self.sll, self.dll]:

            # Test adding elements
            ll.add(1)  # Add to empty list
            ll.add_first(0)  # Add at head
            ll.add_last(2)  # Add at tail

            self.assertEqual(ll.get_size(), 3)
            self.assertEqual(ll.get_first(), 0)
            self.assertEqual(ll.get_last(), 2)
            self.assertIsNotNone(ll._head)
            self.assertIsNotNone(ll._tail)

            # Test inserting elements
            ll.insert(1, 10)  # Insert at middle
            ll.insert(0, -1)  # Insert at head
            ll.insert(5, 100)  # Insert at tail

            self.assertEqual(ll.get_size(), 6)
            self.assertEqual(ll.get_first(), -1)
            self.assertEqual(ll.get_last(), 100)
            self.assertEqual(ll.get(2), 10)

            # Test removing elements
            ll.remove(10)  # Remove by value (middle element)
            ll.remove_first()  # Remove first element
            ll.remove_last()  # Remove last element

            self.assertEqual(ll.get_size(), 3)
            self.assertEqual(ll.get_first(), 0)
            self.assertEqual(ll.get_last(), 2)

            # Test removeAt method
            self.assertEqual(ll.removeAt(0), 0)  # Remove first
            self.assertEqual(ll.remove(1), 1)  # Remove last (since list size is 2 now)
            self.assertFalse(ll.remove(10))
            list_copy = ll.copy()
            list_copy.clear()
            ll.removeAt(0)  # Remove the remaining element

            self.assertEqual(ll.get_size(), 0)
            self.assertEqual(list_copy, ll)
            self.assertIsNone(ll._head)
            self.assertIsNone(ll._tail)

            # Add elements again to check if list is still functioning
            ll.add_first(5)
            ll.add_last(6)

            self.assertEqual(ll.get_size(), 2)
            self.assertEqual(ll.get_first(), 5)
            self.assertEqual(ll.get_last(), 6)
            self.assertIsNotNone(ll._head)
            self.assertIsNotNone(ll._tail)

            self.assertEqual(list(ll.filter(5)), [0])

            ll.add(5)
            ll.add(5)

            self.assertEqual(list(ll.filter(5)), [0, 2, 3])

class TestCompatibility(unittest.TestCase):

    def setUp(self):
        self.sll = LinkedList()
        self.original_ll = OriginalLinkedList()
        for i in range(10):
            self.sll.add_last(i)
            self.original_ll.addLast(i)
    
    def test_methods(self):
        new, old = self.sll, self.original_ll

        def test_equals():
            self.assertEqual(new, old)

        # Test size (and do it repeatedly after each operation)
        # self.assertEqual(new.getSize(), old.getSize())
        test_equals()

        # Test getFirst
        self.assertEqual(new.getFirst(), old.getFirst())

        # Test getLast
        self.assertEqual(new.getLast(), old.getLast())
        self.assertEqual(new.getSize(), old.getSize())

        # Test addFirst
        self.assertEqual(new.addFirst(100), old.addFirst(100))
        test_equals()

        # Test addLast
        self.assertEqual(new.addLast(200), old.addLast(200))
        test_equals()

        # Test insert
        self.assertEqual(new.insert(0, 200), old.insert(0, 200))
        self.assertEqual(new.insert(5, 300), old.insert(5, 300))
        self.assertEqual(new.insert(12, 400), old.insert(12, 400))
        test_equals()

        # Test removeFirst
        self.assertEqual(new.removeFirst(), old.removeFirst())
        self.assertEqual(new.removeFirst(), old.removeFirst())
        test_equals()

        # Test removeLast
        self.assertEqual(new.removeLast(), old.removeLast())
        self.assertEqual(new.removeLast(), old.removeLast())
        self.assertEqual(new.removeLast(), old.removeLast())
        test_equals()

        # Test removeAt
        self.assertEqual(new.removeAt(0), old.removeAt(0))
        self.assertEqual(new.removeAt(2), old.removeAt(2))
        test_equals()

        # Test isEmpty
        self.assertEqual(new.isEmpty(), old.isEmpty())
        self.assertEqual(new.__class__().isEmpty(), old.__class__().isEmpty())
        test_equals()

        # Test getSize
        self.assertEqual(new.getSize(), old.getSize())

        # Print both lists
        # print(f"\n{new} {"!=" if new != old else "=="} {old}")

        # Test clear and equality with variations of == != and assertEqual
        self.assertEqual(new, old)
        new.set(0, 100)
        self.assertFalse(new == old)
        new.removeAt(0)
        self.assertFalse(new == old)
        new.clear()
        self.assertNotEqual(new, old)
        old.clear()
        self.assertTrue(new == old)

# ---------------------------------------------------------------------
# below are the original modules provided to us in LinkList.py
# ---------------------------------------------------------------------
# the only two modification were:
#   1. making private attrs such as __head semi- private with one
#      underscore e.g. _head for easier access in testing
#   2. fixing clear() so that it also sets self._size = 0
# ---------------------------------------------------------------------

class OriginalNode: # pragma: no cover
    def __init__(self, e):
        self.element = e
        self.next = None


#Implementation of Link List
# All the nodes connected. 

class OriginalLinkedList: # pragma: no cover
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # Return the head element in the list 
    def getFirst(self):
        if self._size == 0:
            return None
        else:
            return self._head.element
    
    # Return the last element in the list 
    def getLast(self):
        if self._size == 0:
            return None
        else:
            return self._tail.element

    # Add an element to the beginning of the list 
    def addFirst(self, e):
        newNode = OriginalNode(e) # Create a new node
        newNode.next = self._head # link the new node with the head
        self._head = newNode # head points to the new node
        self._size += 1 # Increase list size

        if self._tail == None: # the new node is the only node in list
            self._tail = self._head

    # Add an element to the end of the list 
    def addLast(self, e):
        newNode = OriginalNode(e) # Create a new node for e
    
        if self._tail == None:
            self._head = self._tail = newNode # The only node in list
        else:
            self._tail.next = newNode # Link the new with the last node
            self._tail = self._tail.next # tail now points to the last node
    
        self._size += 1 # Increase size

    # Same as addLast 
    def add(self, e):
        self.addLast(e)

    # Insert a new element at the specified index in this list
    # The index of the head element is 0 
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e) # Insert first
        elif index >= self._size:
            self.addLast(e) # Insert last
        else: # Insert in the middle
            current = self._head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = OriginalNode(e)
            (current.next).next = temp
            self._size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node. 
    def removeFirst(self):
        if self._size == 0:
            return None # Nothing to delete
        else:
            temp = self._head # Keep the first node temporarily
            self._head = self._head.next # Move head to point the next node
            self._size -= 1 # Reduce size by 1
            if self._head == None: 
                self._tail = None # List becomes empty 
            return temp.element # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self._size == 0:
            return None # Nothing to remove
        elif self._size == 1: # Only one element in the list
            temp = self._head
            self._head = self._tail = None  # list becomes empty
            self._size = 0
            return temp.element
        else:
            current = self._head
        
            for i in range(self._size - 2):
                current = current.next
        
            temp = self._tail
            self._tail = current
            self._tail.next = None
            self._size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list. 
    def removeAt(self, index):
        if index < 0 or index >= self._size:
            return None # Out of range
        elif index == 0:
            return self.removeFirst() # Remove first 
        elif index == self._size - 1:
            return self.removeLast() # Remove last
        else:
            previous = self._head
    
            for i in range(1, index):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self._size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self._size == 0
    
    # Return the size of the list
    def getSize(self):
        return self._size

    def __str__(self):
        result = "["

        current = self._head
        for i in range(self._size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string

        return result

    # Clear the list */
    def clear(self):
        self._head = self._tail = None
        self._size = 0

# ---------------------------------------------------------------------
# end of original modules provided to us in LinkList.py
# ---------------------------------------------------------------------

if __name__ == '__main__': # pragma: no cover
    unittest.main()
