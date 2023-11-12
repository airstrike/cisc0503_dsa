"""This module implements a Queue data structure.

*   `Queue` implements a base class for an unbound queue with standard operations. Elements
    queue()d into the queue are dequeued in the same order (FIFO).

"""

class Queue:

    def __init__(self):
        self._elements = []

    def __repr__(self): # pragma: no cover
        return self.__str__()
    
    def __str__(self): # pragma: no cover
        return f"{self.__class__.__name__}[{' '.join([str(i) for i in self._elements])}]"

    def __len__(self):
        return self.get_size()

    def get_size(self):
        return len(self._elements)

    def is_empty(self) -> bool:
        """
        Returns True if the queue is empty, False otherwise.

        """
        return self.get_size() == 0
    
    def enqueue(self, item):
        """
        Enqueues an item into the queue.

        args:
            item - the item to enqueue into the queue.

        """
        self._elements.append(item)

    def dequeue(self) -> any:
        """
        Dequeues the first element from the queue.

        """
        if self.is_empty():
            return None
        else:
            return self._elements.pop(0)

    def peek(self) -> any:
        """
        Returns the first element from the queue without removing it.

        """
        if self.is_empty():
            return None
        else:
            return self._elements[0]
