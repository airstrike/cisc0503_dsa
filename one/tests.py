import io
import logging
import sys
import unittest
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('tests')

from one import BufferArray10, BufferArray12, BufferArray13, BufferArray14

class BufferArray10Main(unittest.TestCase):
    def setUp(self):
        self.buffer = BufferArray10()

    def test_insert(self):
        self.assertFalse(self.buffer.insert(1))
    
    def test_remove(self):
        self.assertFalse(self.buffer.remove(1))

    def test_find(self):
        self.assertFalse(self.buffer.find(1))

    def test_display(self):
        # temporarily redirect stdout to a capture object
        capture = io.StringIO()
        sys.stdout = capture
        self.buffer.display()

        # store intended output in a string that looks a
        # list with brackets and n 0s separated by comma-and-space
        intended = f"[{', '.join(['0'] * self.buffer._BUFFER_SIZE)}]\n"

        # restore stdout
        sys.stoud = sys.__stdout__
        self.assertEqual(capture.getvalue(), intended)

    def test_locationOf(self):
        self.assertEqual(self.buffer.locationOf(1), None)
        self.assertEqual(self.buffer.locationOf(0), 0)
    
class BufferArray12Main(unittest.TestCase):
    def setUp(self):
        self.buffer = BufferArray12()
    
    def test_insert(self):
        # insert n values into the array until we fill up the buffer
        result = True
        for i in range(self.buffer._BUFFER_SIZE):
            result = result and self.buffer.insert(i)
        # all of these should return True
        self.assertTrue(result)

        # insert one more value into the array, should return False
        self.assertFalse(self.buffer.insert(1))

class BufferArray13Main(unittest.TestCase):
    def setUp(self):
        self.buffer = BufferArray13()

    def test_locationOf(self):
        for (index, value) in enumerate([1, 7, 3]):
            self.buffer.insert(value)
            self.assertEqual(self.buffer.locationOf(value), index)

class BufferArray14Main(unittest.TestCase):
    def setUp(self):
        self.buffer = BufferArray14()

    def test_find(self):
        for value in [4, 5, 6]:
            self.buffer.insert(value)
        results = []
        results.append(self.buffer.find(7))
        results.append(self.buffer.find(6))
        results.append(self.buffer.find(5))
        self.assertEqual(results, [False, True, True])


if __name__ == '__main__':
    unittest.main()