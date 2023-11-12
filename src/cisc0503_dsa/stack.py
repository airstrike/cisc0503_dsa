"""This module implements the Stack data structure.

*   `Stack` implements a base class for an unbound stack with standard operations.

*   `BoundStack` inherits from `Stack` to implement a bounded stack (i.e. with a maximum size).

*   `ThresholdStack` also inherits from `Stack` to implement two stacks sharing a single array,
    with a threshold parameter dividing the two stacks. Each stack can take up to the entire array,
    with both of them sharing the same (bound) space, such that the sum of the sizes of the two
    stacks is equal to the size of the array. We will call the stack at or below the threshold the
    "lower" stack, and the stack above the threshold the "upper" stack.

    Because we don't know _a priori_ how big each stack will be, we can't simply divide the array
    into two halves (or any other arbitrary length). But we can place the elements of the lower stack
    at the beginning of the array (i.e. with its first element at index 0) and subsequent elements
    at increasing indices. Then if we place the elements of the upper stack at the end of the array
    (i.e. with its first element as the very last element of the array) and subsequent elements at
    decreasing indices, we can keep track of the size of each stack by keeping track of two pointers.

    The lower stack pointer is increased as items are pushed onto the stack, whereas the second stack
    pointer is decreased as items are pushed onto the stack--i.e. it keeps track of the distance from
    the end of the array.

    Neither the push nor pop operations are affected by the size of the stacks or the array that holds
    them. They only involve constant-time operations, so their time complexity is O(1).
"""

class Stack:
    """
    Base class implementing an unbound stack with standard operations.

    """
    _elements = []

    def __init__(self):
        self._size = -1
        self._elements = []

    def __repr__(self): # pragma: no cover
        return self.__str__()

    def __str__(self): # pragma: no cover
        """
        Representation of the Stack object as a string
        
        For debugging purposes only, not used anywhere.

        Example in the Python shell:
        >>> from stack import Stack
        >>> s = Stack()
        >>> s
        Stack[]
        """
        return f"{self.__class__.__name__}[{' '.join([str(i) for i in self._elements])}]"

    @property
    def elements(self):
        raise Exception("Cannot access elements directly")

    def get_size(self):
        return len(self._elements)

    def __len__(self):
        # allows us to use len(stack) instead of stack.get_size()
        return self.get_size()

    def is_empty(self) -> bool:
        """
        Returns True if the stack is empty, False otherwise.

        """
        return self.get_size() == 0

    def push(self, item):
        """
        Pushes an item onto the stack.

        args:
            item - the item to push onto the stack.

        """
        self._elements.append(item)

    def pop(self) -> any:
        """
        Remove and return the top item on the stack.

        returns:
            any - the top item on the stack.
            None - if the stack is empty.
        """
        if self.is_empty():
            return None
        return self._elements.pop()

    def peek(self) -> any:
        """
        Returns the _top item on the stack without removing it.

        returns:
            any - the _top item on the stack.
            None - if the stack is empty.
        """
        if self.is_empty():
            return None
        return self._elements[-1]

    def is_full(self) -> bool:
        """
        An unbound stack is never full
        """
        return False


class BoundStack(Stack):
    """
    Bound stack with a maximum size.

    Here we keep track of the "top" of the stack rather than using native Python list methods.
    
    """

    def __init__(self, size):
        if size <= 0:
            raise Exception(f"{self.__class__.__name__} requires a bounded size equal to a positive integer")
        self._size = size
        self._elements = [None] * size
        self._top = 0

    def get_size(self):
        return self._top

    def is_empty(self):
        return self._top == 0

    def is_full(self):
        return self.get_size() == self._size

    def push(self, item):
        """
        Pushes an item onto the stack.

        args:
            item - the item to push onto the stack.

        """
        if self.is_full():
            raise Exception("Stack is full")
        self._elements[self._top] = item
        self._top += 1

    def pop(self):
        """
        Remove and return the top item on the stack.

        returns:
            any - the top item on the stack.
            None - if the stack is empty.
        """
        if self.is_empty():
            return None
        self._top -= 1
        return self._elements[self._top]

    def peek(self):
        """
        Returns the top item on the stack without removing it.

        returns:
            any - the _top item on the stack.
            None - if the stack is empty.
        """
        if self.is_empty():
            return None
        return self._elements[self._top -1] # _top is one past the last element
    

class ThresholdStack(Stack):
    """
    Two-way stack controlled by a _threshold which divides it into two.

    args:
        size - the maximum size of the stack. If not provided, the stack will be unbounded.
        threshold - the _threshold for the two stacks. If not provided, the _threshold will be 100.
    """
    _threshold = 100

    def __init__(self, size, threshold):
        if size <= 0:
            raise Exception(f"{self.__class__.__name__} requires a bounded size equal to a positive integer")
        self._size = size
        self._elements = [None] * size
        self._threshold = threshold
        self._top = 0
        self._top2 = size - 1

    def is_full(self):
        """
        Returns True if the stack is full, False otherwise.
        """
        return self._top == (self._top2 + 1)

    def push(self, value):
        if self.is_full():
            raise Exception("Stack is full")
        if value > self._threshold:
            self._top2 -= 1
            self._elements[self._top2] = value
        else:
            self._elements[self._top] = value
            self._top += 1

    def pop(self):
        raise NotImplementedError("Use pop1 or pop2 instead")

    def pop1(self):
        if self.is_empty1():
            return None
        self._top -= 1
        return self._elements[self._top]

    def pop2(self):
        if self.is_empty2():
            return None
        self._top2 += 1
        return self._elements[self._top2 - 1]

    def is_empty(self):
        """Returns True if both stacks are empty, False otherwise"""
        return self.is_empty1() and self.is_empty2()

    def is_empty1(self):
        """Returns True if the stack at/below the threshold is empty, False otherwise"""
        return self._top == 0

    def is_empty2(self):
        """Returns True if the stack above the threshold is empty, False otherwise"""
        return self._top2 == self._size - 1

    def get_size(self):
        """Total size of the stack"""
        return self.get_size1() + self.get_size2()

    def get_size1(self):
        """Size of the stack at/below the threshold"""
        return self._top
    
    def get_size2(self):
        """Size of the stack above the threshold"""
        return self._size - self._top2 - 1
