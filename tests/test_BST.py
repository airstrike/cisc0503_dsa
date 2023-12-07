import io
import os
import sys
import unittest

# Add the path to the src directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

try:
     from cisc0503_dsa import BST
except ImportError: # pragma: no cover
     try:
          from BST import BST # type: ignore # pragma: no cover
     except ImportError:
          raise ImportError("Could not find BST.py in src or current directory.")

class BSTMain(unittest.TestCase):
     def setUp(self):
          self.tree = BST()
          for e in ["George", "Michael", "Tom", "Adam", "Jones", "Peter", "Daniel"]:
               self.tree.insert(e)

          self.intTree = BST()
          for e in [2, 4, 3, 1, 8, 5, 6, 7]:
               self.intTree.insert(e)

     def test_traverse(self):
          # Traverse tree
          print("Inorder (sorted): ", end = "")
          self.tree.inorder()
          print("\nPostorder: ", end = "")
          self.tree.postorder()
          print("\nPreorder: ", end = "")
          self.tree.preorder()
          print("\nThe number of nodes is", self.tree.getSize())

     def test_search(self):
          # Search for an element
          print("Is Peter in the tree?", self.tree.search("Peter"))
          self.assertTrue(self.tree.search("Peter"))
          self.assertFalse(self.tree.search("Andy"))

     def test_inorder(self):
          print("\nInorder (sorted): ", end = "")
          self.intTree.inorder()

     def test_minValue(self):
          # Calculate minimum value
          print("\nThe minimum value should be 1:", self.intTree.calcMinAndy())
          self.assertEqual(self.intTree.calcMinAndy(), 1)
          self.assertEqual(BST().calcMinAndy(), None)

     def test_maxValue(self):
          # Calculate maximum value
          print("\nThe maximum value should be 8:", self.intTree.calcMaxAndy())
          self.assertEqual(self.intTree.calcMaxAndy(), 8)
          self.assertEqual(BST().calcMaxAndy(), None)

     def test_countNodes(self):
          # Count nodes
          print(f"\nThe number of nodes should be 8: {self.intTree.countNodesAndy()}")
          self.assertEqual(self.intTree.countNodesAndy(), 8)
          self.assertEqual(BST().countNodesAndy(), 0)

     def test_display(self):
          # Our tree should look like this:
          #  2      
          # ┌┴─┐    
          # 1  4    
          #   ┌┴───┐
          #   3    8
          #     ┌──┘
          #     5   
          #     └┐  
          #      6  
          #      └┐ 
          #       7 
          self.intTree.display(compact=True)

     def test_leafCount(self):
          # Count leaf nodes (should be nodes 1, 3 and 7)
          print("The number of leaf nodes should be 3:", self.intTree.leafCountAndy())
          self.intTree.leafCountAndy(verbose=True)
          self.assertEqual(self.intTree.leafCountAndy(), 3)
          self.assertEqual(BST().leafCountAndy(), 0)

     def test_oneChildNodes(self):
          # Count nodes with only one child (should be nodes 8, 5 and 6)
          print("\nThe number of nodes with only one child should be 3:", self.intTree.computeOneChildNodesAndy())
          self.intTree.computeOneChildNodesAndy(verbose=True)
          self.assertEqual(self.intTree.computeOneChildNodesAndy(), 3)
          self.assertEqual(BST().computeOneChildNodesAndy(), 0)

     def test_deleteAllNodes(self):
          # Delete all nodes recursively
          self.intTree.deleteAllNodesAndy()
          self.tree.deleteAllNodesAndy()

          # Count nodes
          print("\nAfter deleting nodes recursively, intTree has size", self.intTree.getSize())
          self.assertEqual(self.intTree.getSize(), 0)
          self.assertEqual(self.intTree.isEmpty(), True)
          print("\nAfter deleting nodes recursively, tree has size", self.tree.getSize())
          self.assertEqual(self.tree.getSize(), 0)
          self.assertEqual(self.tree.isEmpty(), True)

          self.assertIsNone(self.tree.deleteAllNodesAndy())
          self.assertIsNone(self.intTree.deleteAllNodesAndy())

     def test_cannotInsertDuplicate(self):
          self.assertFalse(self.tree.insert("Peter"))
          self.assertFalse(self.intTree.insertWithLoop(1))

     def test_clear(self):
          self.tree.clear()
          self.intTree.clear()
          self.assertTrue(self.tree.isEmpty())
          self.assertEqual(self.intTree.getSize(), 0)

     def test_delete(self):
          self.assertTrue(self.tree.delete("Peter"))
          self.assertTrue(self.intTree.deleteWithLoop(1))
          self.assertFalse(self.tree.search("Peter"))
          self.assertFalse(self.intTree.search(1))

          self.assertTrue(self.tree.delete("George"))
          self.assertTrue(self.intTree.deleteWithLoop(7))

          self.assertFalse(BST().delete("George"))

     def test_deleteWithLoop(self):
          self.assertTrue(self.tree.deleteWithLoop("Peter"))
          self.assertTrue(self.intTree.deleteWithLoop(1))
          self.assertFalse(self.tree.search("Peter"))
          self.assertFalse(self.intTree.search(1))

          self.assertTrue(self.tree.deleteWithLoop("George"))
          self.assertTrue(self.intTree.deleteWithLoop(7))

          self.assertFalse(BST().deleteWithLoop("George"))

          tree = BST()
          tree.insert(1)
          tree.insert(5)
          tree.insert(3)
          tree.insert(9)
          for i in [5, 3, 1, 9]:
               self.assertTrue(tree.deleteWithLoop(i))
               self.assertFalse(tree.deleteWithLoop(2))
               self.assertFalse(tree.deleteWithLoop(10))
          self.assertFalse(BST().deleteWithLoop("George"))

          tree = BST()
          tree.insert(1)
          tree.insert(5)
          tree.insert(3)
          tree.insert(9)
          for i in [5, 3, 1, 9]:
               self.assertTrue(tree.delete(i))
               self.assertFalse(tree.delete(2))
               self.assertFalse(tree.delete(10))

     def test_find(self):
          self.assertTrue(self.tree.find("Peter"))
          self.assertTrue(self.intTree.find(1))
          self.assertFalse(self.tree.find("Andy"))
          self.assertFalse(self.intTree.find(9))
          self.assertFalse(BST().find("Empty Tree"))

     def test_compare_inserts(self):
          self.treeCopy = BST()
          for e in ["George", "Michael", "Tom", "Adam", "Jones", "Peter", "Daniel"]:
               self.treeCopy.insertWithLoop(e)

          self.intTreeCopy = BST()
          for e in [2, 4, 3, 1, 8, 5, 6, 7]:
               self.intTreeCopy.insertWithLoop(e)

          for (a, b) in [(self.tree, self.treeCopy), (self.intTree, self.intTreeCopy)]:
               i = a.root.right.left.element
               j = b.root.right.left.element

               self.assertEqual(i, j)

     def test_compare_deletes(self):
          self.treeCopy = BST()
          for e in ["George", "Michael", "Tom", "Adam", "Jones", "Peter", "Daniel"]:
               self.treeCopy.insert(e)

          self.intTreeCopy = BST()
          for e in [2, 4, 3, 1, 8, 5, 6, 7]:
               self.intTreeCopy.insert(e)

          for (a, b) in [(self.tree, self.treeCopy), (self.intTree, self.intTreeCopy)]:
               i = a.root.right.left.element
               j = b.root.right.left.element

               self.assertEqual(i, j) # we are testing the same element
               self.assertEqual(a.delete(i), b.deleteWithLoop(j))
               self.assertEqual(a.root.element, b.root.element)
               self.assertEqual(a.countNodesAndy(), b.countNodesAndy())
               self.assertEqual(a.isEmpty(), b.isEmpty())
               self.assertEqual(a.computeOneChildNodesAndy(), b.computeOneChildNodesAndy())
          


if __name__ == "__main__": # pragma: no cover
     unittest.main()
