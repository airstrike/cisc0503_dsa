"""This module implements a Linked List data structure.

*   `Node` implements a base class for a node in a linked list.
*   `LinkedList` implements a base class for a singly linked list with standard operations.
*   `DoublyLinkedList` inherits from `LinkedList` to implement a doubly linked list with standard operations.
"""

class Node:
    def __init__(self, element):
        self.element = element
        self.next: Node = None
        self.prev: Node = None
    
    def __repr__(self): # pragma: no cover
        return self.__str__()

    def __prev__(self, with_self=True): # pragma: no cover
        """Returns a string representation of the chain of previous nodes."""
        return (f"{self.prev.__prev__()} <- " if self.prev else "") + (f"({self.element})" if with_self else "")

    def __next__(self, with_self=True): # pragma: no cover
        """Returns a string representation of the chain of next nodes."""
        return (f"({self.element}) " if with_self else "") + (f"-> {self.next.__next__()}" if self.next else "")
    
    def __repr__(self): # pragma: no cover
        return self.__str__()
    
    def __str__(self): # pragma: no cover
        prev_str = self.__prev__(with_self=False)
        next_str = self.__next__(with_self=False)
        return f"{prev_str} Node({self.element}) {next_str}".strip()

class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        self.node_class = Node

    def make_node(self, element):
        return self.node_class(element)
    
    def __repr__(self): # pragma: no cover
        return self.__str__()
    
    def __str__(self): # pragma: no cover
        # use __iter__ to traverse the list and display the elements
        return f"{self.__class__.__name__}({[element for element in self]})"

    def __iter__(self):
        return self.traverse()

    def __len__(self):
        return self.get_size()

    def __copy__(self):
        new_list = LinkedList()
        for element in self:
            new_list.insert_last(element)
        return new_list

    def copy(self):
        return self.__copy__()

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for element1, element2 in zip(self, other):
            if element1 != element2:
                return False
        return True
    
    def get_size(self):
        return self._size
    
    def is_empty(self) -> bool:
        """Returns True if the list is empty, False otherwise.

        """
        return len(self) == 0

    def insert_first(self, element):
        """Insert an element at the beginning of the list.

        """
        node = self.make_node(element)
        node.next = self._head
        self._head = node
        self._size += 1
        if self._tail is None:
            self._tail = self._head

    def insert_last(self, element):
        """Insert an element at the end of the list.

        """
        node = self.make_node(element)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = self._tail.next
        self._size += 1 

    def insert(self, index, element):
        """Insert an element at the specified index in the list.

        """
        if index == 0:
            self.insert_first(element)
        elif index >= len(self):
            self.insert_last(element)
        else:
            current = self._head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = self.make_node(element)
            current.next.next = temp
            self._size += 1

    def remove_first(self):
        """Remove the first element in the list.

        """
        if self._size == 0:
            return False
        else:
            temp = self._head
            self._head = self._head.next
            self._size -= 1
            if self._head is None:
                self._tail = None
            return True

    def remove_last(self):
        """Remove the last element in the list.

        """
        if self._size == 0:
            return False
        elif self._size == 1:
            return self.remove_first()
        else:
            current = self._head
            for i in range(self._size - 2):
                current = current.next
            temp = self._tail
            self._tail = current
            self._tail.next = None
            self._size -= 1
            return True

    def remove(self, index):
        """Remove the element at the specified index in the list.

        """
        if index < 0 or index >= self._size:
            return False
        elif index == 0:
            return self.remove_first()
        elif index == self._size - 1:
            return self.remove_last()
        else:
            previous = self._head
            for i in range(1, index):
                previous = previous.next
            current = previous.next
            previous.next = current.next
            self._size -= 1
            return True

    def set(self, index, element):
        """Set the element at the specified index in the list.

        """
        if index < 0 or index >= self._size:
            return None
        else:
            current = self._head
            for i in range(index):
                current = current.next
            current.element = element
            return current.element

    def get_first(self):
        """Return the first element in the list.

        """
        if self._size == 0:
            return None
        else:
            return self._head.element
        
    def get_last(self):
        """Return the last element in the list.

        """
        if self._size == 0:
            return None
        else:
            return self._tail.element

    def get(self, index):
        """Return the element at the specified index in the list.

        """
        if index < 0 or index >= self._size:
            return None
        else:
            current = self._head
            for i in range(index):
                current = current.next
            return current.element

    def __getitem__(self, index):
        """Return the element at the specified index in the list.

        """
        return self.get(index)

    def traverse(self):
        """Iterate over the elements in the list.

        """
        current = self._head
        while current:
            yield current.element
            current = current.next

    def contains(self, element):
        """Return True if the list contains the specified element, False otherwise.

        """
        for current in self:
            if current == element:
                return True
        return False

    def indexOf(self, element):
        """Return the index of the first matching element in the list.

        """
        return self.index(element, reverse=False)

    def lastIndexOf(self, element):
        """Return the index of the last matching element in the list.

        """
        return self.index(element, reverse=True)

    def index(self, element, reverse=False):
        """Return the index of the first matching element in the list, searching
        in the specified direction.

        args:
            element - the element to search for.
            direction - the direction to traverse the list. 1 for forward, -1 for backward.
        """
        index = -1
        for i, current in enumerate(self.traverse()):
            if current == element and not reverse:
                index = i
                break
            elif current == element and reverse:
                index = i
        return index


class DoublyLinkedList(LinkedList):

    def insert(self, index, element):
        """Insert an element at the specified index in the list.

        """
        if index == 0:
            self.insert_first(element)
        elif index >= len(self):
            self.insert_last(element)
        else:
            current = self._head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = self.make_node(element)
            current.next.prev = current
            current.next.next = temp
            temp.prev = current.next
            self._size += 1

    def insert_first(self, index):
        """Insert an element at the beginning of the list.

        """
        node = self.make_node(index)
        node.next = self._head
        self._head = node
        self._size += 1
        if self._tail is None:
            self._tail = self._head

    def insert_last(self, index):
        """Insert an element at the end of the list.

        """
        node = self.make_node(index)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = self._tail.next
        self._size += 1

    def remove(self, index):
        """Remove an element from the list and update references

        """
        if index < 0 or index >= self._size:
            return False
        if index == 0:
            return self.remove_first()
        if index == self._size - 1:
            return self.remove_last()
        else:
            current = self._head
            for i in range(1, index):
                current = current.next
            current.next = current.next.next
            current.next.prev = current
            self._size -= 1
            return True
    
    def remove_first(self):
        """Remove the first element in the list.

        """
        if self._size == 0:
            return False
        else:
            temp = self._head
            self._head = self._head.next
            self._size -= 1
            if self._head is None:
                self._tail = None
            return True

    def remove_last(self):
        """Remove the last element in the list.

        """
        if self._size == 0:
            return False
        elif self._size == 1:
            return self.remove_first()
        else:
            temp = self._tail
            self._tail = self._tail.prev
            self._tail.next = None
            self._size -= 1
            return True

    def traverse(self, reverse=False):
        """Iterate over the elements in the list.

        """
        if reverse:
            current = self._tail
            while current:
                yield current.element
                current = current.prev
        else:
            current = self._head
            while current:
                yield current.element
                current = current.next

    def __iter__(self):
        return self.traverse()

    def index(self, element, reverse=False):
        """Return the index of the first matching element in the list, searching
        in the specified direction.

        args:
            element - the element to search for.
            direction - the direction to traverse the list. 1 for forward, -1 for backward.
        """

        index = -1
        for i, current in enumerate(self.traverse(reverse=reverse)):
            if current == element:
                index = self._size - i - 1 if reverse else i
                break
        return index

    def lastIndexOf(self, element):
        """Return the index of the last matching element in the list.

        """
        return self.index(element, reverse=True)
