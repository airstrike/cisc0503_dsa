import io
import os
import sys
import unittest

# Add the path to the src directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

try:
     from cisc0503_dsa import quickSort, _quickSort, medianOfThree, partition, partitionSimple, quickSortIterative
except ImportError: # pragma: no cover
     try:
          from quick_sort import * # type: ignore # pragma: no cover
     except ImportError:
          raise ImportError("Could not find quick_sort.py in src or current directory.")

class QuickSortMain(unittest.TestCase):

    def setUp(self):
        self.lsts = (
            [2, 3, 2, 5, 6, 1, -2, 3, 14, 12],
            [9, 7, 3, 1, 2, 8, 4, 6, 5],
            [12, 2, 16, 30, 8, 28, 4, 10, 20, 6, 18]
        )

    def test_quickSort(self):
        for lst in self.lsts:
            for boolean in (False, True):
                print(f"\nTesting quickSort with {'median of three' if not boolean else 'simple partition'} on {lst}:")
                a = b = lst.copy()
                quickSort(a, simple=boolean)
                self.assertEqual(a, sorted(b))

    def test_quickSortVerbose(self):
        for lst in self.lsts:
            for boolean in (True, False):
                print(f"\nVERBOSE Testing quickSort with {'median of three' if not boolean else 'simple partition'} on {lst}:")
                a = b = lst.copy()
                quickSort(a, simple=boolean, verbose=True)
                self.assertEqual(a, sorted(b))

    def test_zquickSortNonRecursive(self):
        lst = [9, 7, 3, 1, 2, 8, 4, 6, 5]
        orig = lst.copy()
        recurse = lst.copy()
        print(f"\nTesting nonRecursiveQuickSort on {lst}:")
        quickSortIterative(lst, simple=False, verbose=True)
        self.assertEqual(lst, sorted(orig))
        quickSort(recurse, simple=False, verbose=True)
        self.assertEqual(lst, recurse)

if __name__ == '__main__': # pragma: no cover
    unittest.main()
