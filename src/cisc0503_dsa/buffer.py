import unittest
import sys

import collections

class BufferArray:
    __numberOfElements = 0
    __BUFFER_SIZE = 0
    __intArray = []

    def __init__(self, buffer_size: int, native=False):
        """Initialize BufferArray"""
        self.__BUFFER_SIZE = buffer_size
        
        # `collections.UserList` is a Class implementation of the built-in list
        # data type type. We can use so that we may remove some methods from it
        # and avoid using those built-in methods, which would defeat the
        # purpose of the assignment. 

        # Said differently, swapping out the two lines below would work just
        # fine, except we would not be able to remove methods from the builtin
        # list object (e.g. `self.__intArray.append = None` would not work).
        if native:
            self.__intArray = []
        else:
            self.__intArray = collections.UserList()

    
        # Initialize all of the elements in the BufferArray to `0`. We must
        # run this before removing methods from the list, otherwise we can't
        # call `self.__intArray.append(0)`
        for i in range(buffer_size):
            self.__intArray.append(0)

        # If we used `collections.UserList()` above, we can now remove the
        # following methods:
        if type(self.__intArray) is collections.UserList:
            self.__intArray.append = None
            self.__intArray.extend = None
            self.__intArray.insert = None
            self.__intArray.remove = None
            self.__intArray.pop = None
            self.__intArray.clear = None
            self.__intArray.count = None
            self.__intArray.__str__ = None

    def __str__(self):
        """Representation of the BufferArray (as a string)
        
        For debugging purposes only, not used anywhere.

        Example in the Python shell:
        >>> from one import *
        >>> b = BufferArray()
        >>> b.insert(1)
        True
        >>> print(b)
        BufferArray([1, 0, 0, 0, 0, 0, 0, 0])
        
        """
        return self.__repr__() # avoid duplicating code
        # alternatively one could do:
        # return '%s' % self.display()

    def __repr__(self):
        """Representation of the BufferArray object
        
        For debugging purposes only, not used anywhere.

        Example in the Python shell:
        >>> from one import *
        >>> b = BufferArray()
        >>> b.insert(1)
        True
        >>> b
        BufferArray([1, 0, 0, 0, 0, 0, 0, 0])
        
        """
        realElements = self.__intArray[:self.__numberOfElements]
        staleElements = self.__intArray[self.__numberOfElements:]
        return f'{self.__class__.__name__}({realElements}) {staleElements}'

    def display(self):
        """Displays the contents of the buffer.

        This approach matches that of the `run()` command
        in the `simple_sort.py` file from the first class.

        One possible improvement would to remove the trailing
        space at the end of the output, prior to the newline.
        That isn't done here since that was not a requirement
        from the assignment prompt.

        """
        for n in range(self.__numberOfElements):
            print(self.__intArray[n], end=" ") 
        print('')


    def locationOf(self, target: int) -> int:
        """Returns the index of a value in the buffer.

        Args:
            target (int): The value to find in the buffer.
        Returns:
            int: The index of target in the buffer, or -1 if not found.
        
        """
        for i in range(self.__numberOfElements):
            if self.__intArray[i] == target:
                return i
        return -1

    def find(self, target: int) -> bool:
        """Checks if a value is present in the buffer.
        
        Args:
            target (int): The value to find in the buffer.
        Returns:
            bool: True if target was found, False otherwise.
        
        """
        return True if self.locationOf(target) != -1 else False

    def insert(self, value: int) -> bool:
        """Inserts a value into the end of the buffer.

        Args:
            value (int): The value to insert into the buffer.
        Returns:
            bool: False if we're already at capacity, True otherwise.

        """
        if self.__numberOfElements == self.__BUFFER_SIZE:
            return False
        self.__intArray[self.__numberOfElements] = value
        self.__numberOfElements += 1
        return True

    def fastRemove(self, target: int) -> bool:
        """Removes the first instance of target from the buffer,
        replacing it with the last element in the buffer.

        Args:
            target (int): The value to remove from the buffer.
        Returns:
            bool: True if target was found and removed, False otherwise.

        """
        location = self.locationOf(target)
        if location != -1:
            self.__intArray[location] = self.__intArray[self.__numberOfElements-1]
            self.__numberOfElements -= 1
            return True
        return False
    
    def stableRemove(self, target: int) -> bool:
        """Removes the first instance of target from the buffer,
        maintaining the order of the buffer.

        Args:
            target (int): The value to remove from the buffer.
        Returns:
            bool: True if target was found and removed, False otherwise.

        """
        # create a copy of the intArray
        location = self.locationOf(target)

        if location != -1:
            # loop through numberOfElements starting at the location
            # and set the value to the next value in the array
            # at the end, set the very last element to 0 and reduce
            # the number of elements
            for i in range(location, self.__numberOfElements-1):
                self.__intArray[i] = self.__intArray[i+1]

            # the next line isn't needed as we will eventually overwrite
            # the last element with a new value when we call insert.
            # since every method uses numberOfElements, it is safe to
            # leave it as is.
            # self.__intArray[self.__numberOfElements-1] = 0

            self.__numberOfElements -= 1
            return True
        return False
