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
        new_list = self.__class__()
        for element in self:
            new_list.add_last(element)
        return new_list

    def copy(self):
        return self.__copy__()

    def __eq__(self, other):
        if self._size != other._size:
            return False
        # for element1, element2 in zip(self, other):
        #     if element1 != element2:
        #         return False
        head1 = self._head
        head2 = other._head

        # if self._head == self._tail and other._head == other._tail:
        #     return True
        
        if hasattr(other._head, "__prev__"):
            while head1 and head2:
                if head1.element != head2.element or \
                    head1.next and not head2.next or \
                    not head1.next and head2.next or \
                    head1.prev and not head2.prev or \
                    not head1.prev and head2.prev:
                    return False
                head1 = head1.next
                head2 = head2.next
            return True
        else:
            while head1 and head2:
                if head1.element != head2.element or \
                    head1.next and not head2.next or \
                    not head1.next and head2.next:
                    return False
                head1 = head1.next
                head2 = head2.next
            return True
    
    def is_empty(self) -> bool:
        """Returns True if the list is empty, False otherwise.

        """
        return len(self) == 0

    def insert(self, index, element):
        """Insert an element at the specified index in the list.

        """
        if index == 0:
            self.add_first(element)
        elif index >= len(self):
            self.add_last(element)
        else:
            one_before = self.get_node(index - 1)
            node = self.make_node(element)
            self._size += 1
            node.next = one_before.next
            one_before.next = node


    def add_first(self, element):
        """Add an element at the beginning of the list.

        """
        node = self.make_node(element)
        node.next = self._head
        self._head = node
        self._size += 1
        if self._tail is None:
            self._tail = self._head

    def add_last(self, element):
        """Add an element at the end of the list.

        """
        node = self.make_node(element)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = self._tail.next
        self._size += 1 

    def remove_first(self):
        """Remove the first element in the list.

        """
        if self._size == 0:
            return False
        else:
            node = self._head
            self._head = self._head.next
            self._size -= 1
            if self._head is None:
                self._tail = None
            return node.element

    def remove_last(self):
        """Remove the last element in the list.

        """
        if self._size == 0:
            return False
        elif self._size == 1:
            return self.remove_first()
        else:
            old_tail = self._tail
            new_tail = self.get_node(self._size - 2)
            new_tail.next = None
            self._tail = new_tail
            self._size -= 1
            return old_tail.element

    def removeAt(self, index):
        """Remove the element at the specified index in the list.

        """
        if index < 0 or index >= self._size:
            return False
        elif index == 0:
            return self.remove_first()
        elif index == self._size - 1:
            return self.remove_last()
        else:
            previous_node = self.get_node(index - 1)
            node = previous_node.next
            previous_node.next = node.next
            self._size -= 1
            return node.element

    def remove(self, element):
        """Remove the specified element if it is in the list.

        args:
            element - the element to remove.
        return:
            bool - True if the element was removed, False otherwise.
        """
        index = self.indexOf(element)
        if index == -1:
            return False
        else:
            return self.removeAt(index)

    def set(self, index, element):
        """Set the element at the specified index in the list.

        """
        if index < 0 or index >= self._size:
            return None
        else:
            node = self.get_node(index)
            node.element = element
            return node.element

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
            node = self.get_node(index)
            return node.element

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
            reverse - the direction to traverse the list. True for backward, False for forward.
        """
        index = -1
        for i, current in enumerate(self.traverse()):
            if current == element and not reverse:
                index = i
                break
            elif current == element and reverse:
                index = i
        return index

    def clear(self):
        """Clear the entire list
        """
        self._head = None
        self._tail = None
        self._size = 0

    # from Midterm question
    def countList(self):
        current = self._head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def filter(self, element):
        """Return a list of indices of all matching elements in the list.

        """
        for i, current in enumerate(self.traverse()):
            if current == element:
                yield i

    def get_node(self, index):
        """Return the node at the specified index in the list.

        """
        if index < 0 or index >= self._size:
            return None
        else:
            current = self._head
            for _ in range(index):
                current = current.next
            return current

    # Aliases
    def add(self, element): # pragma: no cover
        """Same as add_last() per requirements.
        """
        self.add_last(element)

    def addLast(self, element): # pragma: no cover
        self.add_last(element)

    def addFirst(self, element): # pragma: no cover
        self.add_first(element)

    def removeLast(self): # pragma: no cover
        return self.remove_last()

    def removeFirst(self): # pragma: no cover
        return self.remove_first()

    def getFirst(self): # pragma: no cover
        return self.get_first()
    
    def getLast(self): # pragma: no cover
        return self.get_last()

    def getSize(self): # pragma: no cover
        return self.get_size()

    def get_size(self): # pragma: no cover
        return self._size

    def isEmpty(self) -> bool: # pragma: no cover
        return self.is_empty()

class DoublyLinkedList(LinkedList):

    def insert(self, index, element):
        """Insert an element at the specified index in the list.

        """
        if index == 0:
            self.add_first(element)
        elif index >= len(self):
            self.add_last(element)
        else:
            previous_node = self.get_node(index - 1)
            next_node = previous_node.next
            node = self.make_node(element)
            self._size += 1
            node.next = next_node
            node.prev = previous_node
            previous_node.next = node
            next_node.prev = node

    def add_first(self, index):
        """Add an element at the beginning of the list.

        """
        node = self.make_node(index)
        node.next = self._head
        self._head = node
        self._size += 1
        if self._tail is None:
            self._tail = self._head

    def add_last(self, index):
        """Add an element at the end of the list.

        """
        node = self.make_node(index)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = self._tail.next
        self._size += 1

    def removeAt(self, index):
        """Remove an element from the list and update references

        """
        if index < 0 or index >= self._size:
            return False
        if index == 0:
            return self.remove_first()
        if index == self._size - 1:
            return self.remove_last()
        else:
            node = self.get_node(index)
            node.prev.next = node.next
            node.next.prev = node.prev
            self._size -= 1
            return node.element
    
    def remove_first(self):
        """Remove the first element in the list.

        """
        if self._size == 0:
            return False
        else:
            node = self._head
            self._head = self._head.next
            if self._head is not None:
                self._head.prev = None
            self._size -= 1
            if self._head is None:
                self._tail = None
            return node.element

    def remove_last(self):
        """Remove the last element in the list.

        """
        if self._size == 0:
            return False
        elif self._size == 1:
            return self.remove_first()
        else:
            node = self._tail
            self._tail = self._tail.prev
            self._tail.next = None
            self._size -= 1
            return node.element

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
            reverse - the direction to traverse the list. True for backward, False for forward.
        """

        index = -1
        for i, current in enumerate(self.traverse(reverse=reverse)):
            if current == element:
                index = self._size - i - 1 if reverse else i
                break
        return index
