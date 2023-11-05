import unittest
import sys

import collections

class BufferArray:
    __numberOfElements = 0
    __BUFFER_SIZE = None

    def __init__(self, buffer_size: int = 8, native=False):
        """Initialize BufferArray"""
        
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
        self.__BUFFER_SIZE = buffer_size
        for i in range(self.__BUFFER_SIZE):
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
        return f'BufferArray({self.__intArray})'

    def display(self):
        """Displays the contents of the buffer.

        This approach matches that of the `run()` command
        in the `simple_sort.py` file from the first class.

        One possible improvement would to remove the trailing
        space at the end of the output, prior to the newline.
        That isn't done here since that was not a requirement
        from the assignment prompt.

        """
        i = 0
        for n in range(self.__BUFFER_SIZE):
            if self.__intArray[n] != 0:
                i += 1
                print(self.__intArray[n], end=" ") 
            if i == self.__numberOfElements:
                break
        print('')


    def locationOf(self, target: int) -> int:
        """Returns the index of a value in the buffer.

        Args:
            target (int): The value to find in the buffer.
        Returns:
            int: The index of target in the buffer, or -1 if not found.
        
        """
        index = 0
        for value in self.__intArray:
            if value == target:
                return index
            index += 1
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

    def remove(self, target: int) -> bool:
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
            self.__intArray[self.__numberOfElements-1] = 0
            self.__numberOfElements -= 1
            return True
        return False

    def _oldRemove(self, target: int) -> bool:
        if self.__numberOfElements == 0:
            return False
        for i in range(self.__BUFFER_SIZE):
            if self.__intArray[i] == target:
                self.__intArray[i] = self.__intArray[self.__numberOfElements-1]
                self.__intArray[self.__numberOfElements-1] = 0
                self.__numberOfElements -= 1
                return True
        return False

    def _oldStableRemove(self, target: int) -> bool:
        # if we have no elements to remove, quickly return False
        # if self.__numberOfElements == 0:
        #     return False

        # create a new buffer with the same type as self.__intArray
        # without caring whether it is `collections.UserList` or `list`
        newArray = type(self.__intArray)()

        i, j = 0, 0
        result = False
        for i in range(self.__BUFFER_SIZE):
            newArray.append(0)
            value = self.__intArray[i]
            if value != target and value != 0:
                newArray[j] = self.__intArray[i]
                j += 1

        if j == self.__numberOfElements:
            # then we didn't remove any elements
            return False

        self.__intArray = newArray
        self.__numberOfElements = j
        return True
