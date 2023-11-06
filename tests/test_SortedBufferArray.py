import os
import random
import sys
import unittest

# Add the path to the src directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

from cisc0503_dsa import SortedBufferArrayNoDups, SortedBufferArrayWithDups

class SortedBufferArrayNoDupsTest(unittest.TestCase):
    """Test the SortedBufferArrayNoDups class."""

    def setUp(self):
        """ Create a SortedBufferArrayNoDups object with unique values in it. """
        self.buffer = SortedBufferArrayNoDups(buffer_size=8)
        for value in [1, 9, 2, 8]:
            self.buffer.insert(value)

    def test_array_is_sorted(self):
        """ Ensure the array is sorted even though we inserted values in a random order. """
        self.assertTrue(all(self.buffer._BufferArray__intArray[i] <= self.buffer._BufferArray__intArray[i+1] for i in range(self.buffer._BufferArray__numberOfElements-1)))

    def test_insert_no_dups(self):
        """ Ensure no duplicate values can be inserted and the buffer remains sorted. """
        self.assertFalse(self.buffer.insert(9), "Duplicate value should not be inserted.")
        
        # Ensure buffer size remains the same
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)

        # Ensure buffer remains sorted
        self.assertTrue(all(self.buffer._BufferArray__intArray[i] <= self.buffer._BufferArray__intArray[i+1] for i in range(self.buffer._BufferArray__numberOfElements-1)))

    def test_insert_sorted(self):
        """ Ensure values are inserted in sorted order. """
        self.buffer.insert(5)
        self.buffer.insert(3)
        self.buffer.insert(10)

        # Ensure buffer remains sorted
        self.assertTrue(all(self.buffer._BufferArray__intArray[i] <= self.buffer._BufferArray__intArray[i+1] for i in range(self.buffer._BufferArray__numberOfElements-1)))

    def test_stableRemove_after_attempted_duplicate_insert(self):
        """ Ensure values can be removed even after attempting to insert duplicates and buffer remains sorted. """
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)
        
        # Attempt to insert a duplicate
        self.assertFalse(self.buffer.insert(9))
        
        # Ensure the number of elements did not change
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)

        # Attempt to remove the duplicated value
        self.assertTrue(self.buffer.stableRemove(9))
        
        # Ensure buffer size decreases by 1
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)

        # Ensure buffer remains sorted
        self.assertTrue(all(self.buffer._BufferArray__intArray[i] <= self.buffer._BufferArray__intArray[i+1] for i in range(self.buffer._BufferArray__numberOfElements-1)))

    def test_fastRemove_throwsError(self):
        """ Ensure fastRemove throws an error on a sorted buffer. """
        with self.assertRaises(NotImplementedError):
            self.buffer.fastRemove(9)

class SortedBufferArrayWithDupsTest(unittest.TestCase):
    """Test the SortedBufferArrayWithDups class."""

    def setUp(self):
        """ Create a SortedBufferArrayWithDups object with values in it. """
        self.buffer = SortedBufferArrayWithDups(buffer_size=8)
        for value in [1, 4, 3, 2, 4, 6, 4]:
            self.buffer.insert(value)

    def test_array_is_sorted(self):
        """ Ensure the array is sorted even though we inserted values in a random order. """
        self.assertTrue(all(self.buffer._BufferArray__intArray[i] <= self.buffer._BufferArray__intArray[i+1] for i in range(self.buffer._BufferArray__numberOfElements-1)))

    def test_insert_with_dups(self):
        """ Ensure duplicate values can be inserted and the buffer remains sorted. """
        self.assertTrue(self.buffer.insert(4), "Duplicate value should be inserted.")
        
        # Ensure buffer size increases
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 8)

        # Ensure buffer remains sorted
        self.assertTrue(all(self.buffer._BufferArray__intArray[i] <= self.buffer._BufferArray__intArray[i+1] for i in range(self.buffer._BufferArray__numberOfElements-1)))

    def test_findAll(self):
        """ Ensure findAll returns the correct number of occurrences. """
        self.assertEqual(self.buffer.findAll(4), 3)
        self.assertEqual(self.buffer.findAll(6), 1)
        self.assertEqual(self.buffer.findAll(5), 0)

    def test_stableRemoveAll(self):
        """ Ensure all occurrences of a value are removed and buffer remains sorted. """
        removed_count = self.buffer.stableRemoveAll(4)
        
        # Ensure 3 occurrences of '4' are removed
        self.assertEqual(removed_count, 3)
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)

        # Ensure buffer remains sorted
        self.assertTrue(all(self.buffer._BufferArray__intArray[i] <= self.buffer._BufferArray__intArray[i+1] for i in range(self.buffer._BufferArray__numberOfElements-1)))

    def test_fastRemove_throwsError(self):
        """ Ensure fastRemove throws an error on a sorted buffer. """
        with self.assertRaises(NotImplementedError):
            self.buffer.fastRemove(4)

class SortedBuffersFuzzyTest(unittest.TestCase):
    """ Test both SortedBufferArray classes with a large number of random values. """

    def setUp(self):
        """ Create a SortedBufferArrayNoDups object with unique values in it. """
        self.size = random.randint(1, 10) * 2 # even number to make tests easier
        self.nodups = SortedBufferArrayNoDups(buffer_size=self.size)
        self.dups = SortedBufferArrayWithDups(buffer_size=self.size)

    def test_insert_no_dups(self):
        """ Ensure no duplicate values can be inserted and the buffer remains sorted. """
        # Randomly generate unique values
        values = [i for i in range(1, self.size * 2)]
        random_values = random.sample(values, self.size)
        
        # insert all n random values
        for value in random_values:
            self.assertTrue(self.nodups.insert(value))
            self.assertFalse(self.nodups.insert(value))

        # fail when trying to insert one more value
        self.assertFalse(self.nodups.insert(-100)) # we know -100 is not in the buffer

    def test_insert_with_dups(self):
        """ Ensure no duplicate values can be inserted and the buffer remains sorted. """
        # Randomly generate unique values
        values = [i for i in range(1, self.size * 2)]
        random_values = random.sample(values, self.size)
        
        # insert half of the n random values, twice each
        for (i, value) in enumerate(random_values):
            if i % 2 == 0:
                self.assertTrue(self.dups.insert(value))
                self.assertTrue(self.dups.insert(value))

        # fail when trying to insert one more value
        self.assertFalse(self.dups.insert(-100)) # we know -100 is not in the buffer


if __name__ == "__main__":
    unittest.main()
