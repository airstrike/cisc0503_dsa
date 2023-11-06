import os
import sys
import unittest

# Add the path to the src directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

from cisc0503_dsa import BufferArrayNoDups, BufferArrayWithDups

class BufferArrayNoDupsTest(unittest.TestCase):
    """Test the BufferArrayNoDups class."""

    def setUp(self):
        """ Create a BufferArrayNoDups object with unique values in it. """
        self.buffer = BufferArrayNoDups(buffer_size=8)
        for value in [1, 9, 2, 8]:
            self.buffer.insert(value)

    def test_insert_no_dups(self):
        """ Ensure no duplicate values can be inserted. """
        self.assertFalse(self.buffer.insert(9), "Duplicate value should not be inserted.")
        
        # Ensure buffer size remains the same
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)

    def test_remove_after_attempted_duplicate_insert(self):
        """ Ensure values can be removed even after attempting to insert duplicates. """
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)
        # Attempt to insert a duplicate
        self.assertFalse(self.buffer.insert(9))
        # Ensure the number of elements did not change
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)

        # Attempt to remove the duplicated value
        self.assertTrue(self.buffer.fastRemove(9))
        # Ensure buffer size decreases by 1
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)

    def test_stableRemove_after_attempted_duplicate_insert(self):
        """ Ensure values can be removed even after attempting to insert duplicates. """
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)
        # Attempt to insert a duplicate
        self.assertFalse(self.buffer.insert(9))
        # Ensure the number of elements did not change
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)

        # Attempt to remove the duplicated value
        self.assertTrue(self.buffer.stableRemove(9))
        # Ensure buffer size decreases by 1
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)

class BufferArrayWithDupsTest(unittest.TestCase):
    """Test the BufferArrayWithDups class."""

    def setUp(self):
        """ Create a BufferArrayWithDups object with some values in it. """
        self.buffer = BufferArrayWithDups(buffer_size=8)
        for value in [1, 9, 2, 9, 8]:
            self.buffer.insert(value)

    def test_insert_with_dups(self):
        """ Ensure duplicate values can be inserted. """
        result = self.buffer.insert(9)
        self.assertTrue(result, "Duplicate value should be inserted.")
        
        # Ensure buffer size increases by 1
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 6)

    def test_remove_all(self):
        """ Ensure one instance of a duplicate value can be removed at a time. """
        # Ensure we have 5 elements to begin with
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 5)

        # Add two more duplicates of a new value
        self.assertTrue(self.buffer.insert(4))
        self.assertTrue(self.buffer.insert(4))
        # Ensure we have 7 elements now
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 7)

        # Remove both 4s and ensure we're back to 5 elements
        self.assertEqual(self.buffer.fastRemoveAll(4), 2) # 2 elements removed
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 5)

        # Remove both starting 9s and ensure we're down to 3 elements
        self.assertEqual(self.buffer.fastRemoveAll(9), 2) # 2 elements removed
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)

        # Try removing another 9 and ensure we're still at 3 elements
        self.assertEqual(self.buffer.fastRemoveAll(9), 0) # 0 elements removed
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)

    def test_remove_single(self):
        # Insert a few more duplicates
        self.buffer.insert(4)
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 6)

        # Ensure we can remove a 4
        self.assertEqual(self.buffer.fastRemove(4), 1)
        # Ensure buffer size decreases by 1
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 5)

        # Ensure we can remove a 9
        self.assertEqual(self.buffer.fastRemove(9), 1)
        # Ensure buffer size decreases by 1
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)

        # Ensure we can remove another 9
        self.assertEqual(self.buffer.fastRemove(9), 1)
        # Ensure buffer size decreases by 1 again
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)

        # There are no 9s left, so ensure we can't remove another 9
        self.assertEqual(self.buffer.fastRemove(9), 0)
        # Ensure buffer size doesn't decrease
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)

    def test_stable_remove_all(self):
        """ Ensure all instances of a duplicate value can be removed at a time. """
        # Ensure we have 5 elements to begin with
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 5)

        # Add two more duplicates of a new value
        self.assertTrue(self.buffer.insert(4))
        self.assertTrue(self.buffer.insert(4))
        # Ensure we have 7 elements now
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 7)

        # Remove both 4s and ensure we're back to 5 elements
        self.assertEqual(self.buffer.stableRemoveAll(4), 2)
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 5)

        # Remove both starting 9s and ensure we're down to 3 elements
        self.assertEqual(self.buffer.stableRemoveAll(9), 2)
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)

        # Try removing another 9 and ensure we're still at 3 elements
        self.assertEqual(self.buffer.stableRemoveAll(9), 0)
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)

    def test_stable_remove_single(self):
        # Insert a few more duplicates
        self.buffer.insert(4)
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 6)

        # Ensure we can remove a 4
        self.assertEqual(self.buffer.stableRemove(4), 1)
        # Ensure buffer size decreases by 1
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 5)

        # Ensure we can remove a 9
        self.assertEqual(self.buffer.stableRemove(9), 1)
        # Ensure buffer size decreases by 1
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)

        # Ensure we can remove another 9
        self.assertEqual(self.buffer.stableRemove(9), 1)
        # Ensure buffer size decreases by 1 again
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)

        # There are no 9s left, so ensure we can't remove another 9
        self.assertEqual(self.buffer.stableRemove(9), 0)
        # Ensure buffer size doesn't decrease
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)

if __name__ == "__main__":
    unittest.main()
