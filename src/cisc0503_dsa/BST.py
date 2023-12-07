#Binary Search Tree (assignment 06 version)
class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree 
    def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True # Element is found

        return False

    def __repr__(self): # pragma: no cover
        return self._display(compact=True)

    def __str__(self): # pragma: no cover
        return self._display(compact=False)

    def display(self, compact=False): # pragma: no cover
        print(self._display(compact=compact))

    def _display(self, compact=False): # pragma: no cover
        if self.root is None:
            return "<empty tree>"

        h = self._height(self.root)
        matrix = [[' '] * (2 ** h) * 2 for _ in range(h * 2)]
        col_idx = 2 ** h
        levels = [[(self.root, col_idx)]]

        for l in range(h):
            curr_lvl = levels[l]
            next_lvl = []
            for node, col_idx in curr_lvl:
                matrix[l * 2][col_idx] = str(node.element)
                conn_row = matrix[l * 2 + 1]
                if node.left:
                    lft_idx = col_idx - 2 ** (h - l - 1)
                    next_lvl.append((node.left, lft_idx))
                    conn_row[col_idx] = "┘"
                    conn_row[lft_idx] = "┌"
                    for j in range(lft_idx + 1, col_idx):
                        conn_row[j] = "─"
                if node.right:
                    rt_idx = col_idx + 2 ** (h - l - 1)
                    next_lvl.append((node.right, rt_idx))
                    conn_row[col_idx] = "└"
                    conn_row[rt_idx] = "┐"
                    for j in range(col_idx + 1, rt_idx):
                        conn_row[j] = "─"
                if node.left and node.right:
                    conn_row[col_idx] = "┴"
            levels.append(next_lvl)

        self._left_align(matrix, compact)
        return "\n".join([''.join(row) for row in matrix])

    def _height(self, node):
        if node is None:
            return 0
        return max(self._height(node.left), self._height(node.right)) + 1

    @staticmethod
    def _left_align(matrix, compact=True):
        empty_columns = []
        for col_idx in range(len(matrix[0])):
            for row_idx in range(len(matrix)):
                symbol = matrix[row_idx][col_idx]
                if symbol == ' ' or (symbol == '─' if compact else False):
                    continue
                else:
                    break
            else:
                empty_columns.append(col_idx)

        for row_idx in range(len(matrix)):
            for col_idx in empty_columns:
                matrix[row_idx][col_idx] = ''

        return matrix

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully 
    def insertWithLoop(self, e):
        if self.root == None:
            self.root = self.createNewNode(e) # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.createNewNode(e)
            else:
                parent.right = self.createNewNode(e)

        return True # Element inserted

    # Same as insertWithWhile, but using recursion
    def insert(self, e):
        if self.root == None:
            self.root = self.createNewNode(e)
        else:
            return self._insert(e, self.root)

    def _insert(self, e, node):
        if e < node.element:
            if node.left is None:
                node.left = self.createNewNode(e)
            else:
                return self._insert(e, node.left)
        elif e > node.element:
            if node.right is None:
                node.right = self.createNewNode(e)
            else:
                return self._insert(e, node.right)
        else:
            return False

    # Create a new TreeNode for element e
    def createNewNode(self, e):
        self.size += 1
        return TreeNode(e)

    # Return the size of the tree
    def getSize(self):
        return self.size
    
    # Inorder traversal from the root
    def inorder(self):
        self.inorderHelper(self.root)
        print("")

    # Inorder traversal from a subtree 
    def inorderHelper(self, r):
        if r != None:
            self.inorderHelper(r.left)
            print(r.element, end = " ")
            self.inorderHelper(r.right)

    # Postorder traversal from the root 
    def postorder(self):
        self.postorderHelper(self.root)
        print("")

    # Postorder traversal from a subtree 
    def postorderHelper(self, root):
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end = " ")

    # Preorder traversal from the root 
    def preorder(self):
        self.preorderHelper(self.root)
        print("")

    # Preorder traversal from a subtree 
    def preorderHelper(self, root):
        if root != None:
            print(root.element, end = " ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree 
    def deleteWithLoop(self, e):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        while current != None:
            if e < current.element:
                parent = current
                current = current.left
            elif e > current.element: 
                parent = current
                current = current.right
            else:
                break # Element is in the tree pointed by current

        if current == None:
            return False # Element is not in the tree

        # Case 1: current has no left children
        if current.left == None:
            # Connect the parent with the right child of the current node
            if parent == None:
                self.root = current.right
            else:
                if e < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node in the left subtree of
            # the current node and also its parent
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right != None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right # Keep going to the right

            # Replace the element in current by the element in rightMost
            current.element = rightMost.element

            # Eliminate rightmost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                # Special case: parentOfRightMost == current
                parentOfRightMost.left = rightMost.left     

        self.size -= 1
        return True # Element deleted

    # Same as deleteWithLoop, but using recursion
    def delete(self, e):
        if self.root == None:
            return False
        else:
            return self._delete(e, self.root, None)
        
    def _delete(self, e, current, parent):
        if e < current.element:
            if current.left is None:
                return False
            else:
                return self._delete(e, current.left, current)
        elif e > current.element:
            if current.right is None:
                return False
            else:
                return self._delete(e, current.right, current)
        else: # We have found the element

            # Case 1: The current node has no left children
            if current.left is None:
                # Connect the parent with the right child of the current node
                if parent is None:
                    self.root = current.right
                    self.size -= 1
                    return True
                else:
                    if e < parent.element:
                        parent.left = current.right
                    else:
                        parent.right = current.right

            # Case 2: The current node has a left child
            # Then locate the rightmost node in the left subtree of
            # the current node and also its parent, again using recursion
            else:
                # Replace current element with the rightmost element in left subtree
                current.element = self._deleteRightmost(current, current.left)
            self.size -= 1
            return True

    def _deleteRightmost(self, parent, current):
        if current.right is not None:
            return self._deleteRightmost(current, current.right)
        else:
            if parent.right == current:
                parent.right = current.left
            else:
                parent.left = current.left
            return current.element

    # Find element using recursion and return True if the element is found, False otherwise
    def find(self, e):
        if self.root is None:
            return False
        return self._find(e, self.root)

    def _find(self, e, current):
        if current is None:
            return False  # Element is not found
        elif e == current.element:
            return True  # Element is found
        elif e < current.element:
            return self._find(e, current.left)  # Search in the left subtree
        else:
            return self._find(e, current.right)  # Search in the right subtree
                
    # Return true if the tree is empty
    def isEmpty(self):
        return self.size == 0
        
    # Remove all elements from the tree
    def clear(self):
        self.root = None
        self.size = 0

    def calcMinAndy(self):
        """Return the min value of the tree"""
        if self.root == None:
            return None
        current = self.root
        while current.left != None:
            current = current.left
        return current.element

    def calcMaxAndy(self):
        """Return the max value of the tree"""
        if self.root == None:
            return None
        current = self.root
        while current.right != None:
            current = current.right
        return current.element
   
    def countNodesAndy(self, node=None):
        """Count the number of nodes in the tree recursively.

        If the node is None (i.e., the tree is empty or it's a leaf's child), return 0.
        Otherwise, return 1 (for the current node) plus the count from the left subtree 
        and the count from the right subtree.
        """
        if node is None:
            node = self.root

        # Base case: if the node is None, return 0
        if node is None:
            return 0

        # Initialize count with the current node
        count = 1

        # Recursively count nodes in the left subtree, if it exists
        if node.left is not None:
            count += self.countNodesAndy(node.left)

        # Recursively count nodes in the right subtree, if it exists
        if node.right is not None:
            count += self.countNodesAndy(node.right)

        return count

    def deleteAllNodesAndy(self, node=None):
        """Recursively delete all nodes in the tree."""
        if self.root is None:
            return None

        if node is None:
            node = self.root

        deleted = self.delete(node.element)
        if deleted != None:
            return self.deleteAllNodesAndy(self.root)

    def leafCountAndy(self, node=None, verbose=False):
        """Return the number of leaf nodes in the tree."""
        if self.root is None:
            return 0

        if node is None:
            node = self.root

        count = 0
        if node.left is None and node.right is None:
            if verbose: print(f"Leaf node: {node.element}")
            count += 1
        else:
            if node.left is not None:
                count += self.leafCountAndy(node.left, verbose=verbose)
            if node.right is not None:
                count += self.leafCountAndy(node.right, verbose=verbose)

        return count

    def computeOneChildNodesAndy(self, node=None, verbose=False):
        """Return the number of nodes with only one child."""
        if self.root is None:
            return 0

        if node is None:
            node = self.root

        count = 0
        if (node.left is None and node.right is not None) or (node.right is None and node.left is not None):
            if verbose: print(f"One-child node: {node.element}")
            count += 1
        
        if node.left is not None:
            count += self.computeOneChildNodesAndy(node.left, verbose=verbose)
        if node.right is not None:
            count += self.computeOneChildNodesAndy(node.right, verbose=verbose)

        return count
