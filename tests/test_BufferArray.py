import io
import os
import sys
import unittest

# Add the path to the src directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

from cisc0503_dsa import BufferArray

def read(fn):
    """Temporarily redirect stdout to a capture object and return the value."""
    capture = io.StringIO()
    sys.stdout = capture
    fn()
    sys.stdout = sys.__stdout__
    return capture.getvalue()

class BufferArrayMain(unittest.TestCase):
    """Test the BufferArray class."""

    def setUp(self):
        """ Create a BufferArray object with some values in it.

        This will run before each test_* method.

        """
        self.buffer = BufferArray(buffer_size=8)
        for value in [1, 9, 2, 8]:
            self.buffer.insert(value)

    def test_display(self):
        """ Test the display method.

        We run this test somewhat manually here to be explicit,
        but for the sake of conciseness we will use the helper
        function read() moving forward.

        """
        # temporarily redirect stdout to a capture object
        capture = io.StringIO()
        sys.stdout = capture
        self.buffer.display()

        # restore stdout and compare results
        sys.stdoud = sys.__stdout__
        self.assertEqual(capture.getvalue(), "1 9 2 8 \n")

    def test_locationOf(self):
        self.assertEqual(self.buffer.locationOf(1), 0)
        self.assertEqual(self.buffer.locationOf(8), 3)

        reversed_values = [8, 2, 9, 1]
        for (i, result) in enumerate(range(len(reversed_values), 0, -1)):
            self.assertEqual(self.buffer.locationOf(reversed_values[i]), result-1) # -1 because of zero indexing

    def test_insert(self):
        # insert 4 more values into the array until we fill up the buffer
        result = True
        for i in range(4):
            result = result and self.buffer.insert(i)
        # all of these should return True
        self.assertTrue(result)

        # insert one more value into the array, should return False
        self.assertFalse(self.buffer.insert(1))

        # check that the array is exactly full
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 8)

    def test_locationOf2(self):
        for (index, value) in enumerate([1, 9, 2, 8]):
            self.buffer.insert(value)
            self.assertEqual(self.buffer.locationOf(value), index)

    def test_find(self):
        for value in [4, 5, 6]:
            self.buffer.insert(value)
        results = []
        results.append(self.buffer.find(7))
        results.append(self.buffer.find(6))
        results.append(self.buffer.find(5))
        self.assertEqual(results, [False, True, True])

    def test_fastRemove(self):
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)
        self.assertEqual(self.buffer.fastRemove(5), False)
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 4)
        self.assertEqual(self.buffer.fastRemove(9), True)
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)
        self.assertEqual(self.buffer.locationOf(9), -1)
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)
        self.assertEqual(read(self.buffer.display), "1 8 2 \n")

    def test_stableRemove(self):
        self.assertEqual(self.buffer.stableRemove(5), False)
        self.assertEqual(self.buffer.stableRemove(9), True)
        self.assertEqual(self.buffer.locationOf(9), -1)
        self.assertEqual(self.buffer._BufferArray__numberOfElements, 3)
        self.assertEqual(read(self.buffer.display), "1 2 8 \n")

    def test_all(self):
        # ignore the setUp method, create a new BufferArray object
        b = BufferArray(buffer_size=8)

        # check initialized correctly
        # should have 8 elements, all set to zero
        self.assertEqual(b._BufferArray__numberOfElements, 0)
        self.assertEqual(b._BufferArray__intArray, [0, 0, 0, 0, 0, 0, 0, 0])

        # should print no elements since 0 = null for this exercise
        self.assertEqual(read(b.display), "\n")

        # should add one element and print one element, "1"
        self.assertEqual(b.insert(1), True)
        self.assertEqual(read(b.display), "1 \n")

        # should add three elements and print four elements in order: "1 9 2 8"
        self.assertEqual(b.insert(9), True)
        self.assertEqual(b.insert(2), True)
        self.assertEqual(b.insert(8), True)
        self.assertEqual(read(b.display), "1 9 2 8 \n")

        # should remove() first element, replacing it with the last element
        # so that the buffer changes from "1 9 2 8" to the resulting "8 9 2"
        self.assertEqual(b.fastRemove(1), True)
        self.assertEqual(b._BufferArray__numberOfElements, 3)
        self.assertEqual(read(b.display), "8 9 2 \n")

        # should sableRemove() the first element, maintaining the buffer
        # so that the buffer changes from "8 9 2" to "9 2"
        self.assertEqual(b.stableRemove(8), True)
        self.assertEqual(b._BufferArray__numberOfElements, 2)
        self.assertEqual(read(b.display), "9 2 \n")

        # should then add a new element, so that buffer changes from "8 9 2"
        # so that the buffer changes from "9 2" to "9 2 5"
        self.assertEqual(b.insert(5), True)
        self.assertEqual(read(b.display), "9 2 5 \n")
        self.assertEqual(b._BufferArray__numberOfElements, 3)

class BufferArrayMainNative(BufferArrayMain):

    def setUp(self):
        """ Create a BufferArray object with some values in it, using a native
        Python list.

        This will run before each test_* method.

        """
        self.buffer = BufferArray(buffer_size=8, native=True)
        for value in [1, 9, 2, 8]:
            self.buffer.insert(value)


if __name__ == '__main__': # pragma: no cover
    unittest.main()
