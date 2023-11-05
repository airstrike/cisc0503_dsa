import unittest
import sys

# Assignment #1

# 1.	Create a Python class called BufferArray. It will have an array to hold
# integers and a variable, called numberOfElements, that records how many values
# are being stored in the array.

# 2.	Give the BufferArray an integer constant called BUFFER_SIZE and initialize
# it to 8.

# 3.	Give the BufferArray a variable called numberOfElements and initialize it
# to 0.

# 4.	Make BUFFER_SIZE, intArray, and numberOfElements private.

# 5.	The BufferArray should have an __init__ which initializes all elements in
# the Buffer to 0. 

# 6.	Give the BufferArray a method called insert() that takes an integer
# argument, called value, and returns a Boolean. For starters, just have it
# return false. 

# 7.	Give the BufferArray a method called remove() that takes an integer
# argument, called value, and returns a Boolean. For starters, just have it
# return false. 

# 8.	Give the BufferArray a method called find() that takes an integer argument,
# called target, and returns a Boolean. For starters, just have it return false.

# 9.	Give the BufferArray a public method called display() that takes no
# arguments and prints the list. 

# 10.	Give the BufferArray a method called locationOf() that takes an integer
# argument, called target, and returns an integer. 

# 11.	Write a test driver for your BufferArray class called BufferArrayMain in a
# different file that tests the insert, display, find, and remove methods. Make
# the tests fairly thorough. 

def tests():
    """Run the tests for this assignment.

    Tests can be run either in any of the following ways: 
    
    1. importing this module and calling this function,
    2. running this file directly from the command line or IDLE
    3. running `one_tests.py` from the command line or IDLE

    """
    from tests import BufferArrayMain
    suite = unittest.TestLoader().loadTestsFromTestCase(BufferArrayMain)
    unittest.TextTestRunner(verbosity=2).run(suite)

# 12.	Have the insert method add the value argument to the next available space
# at the end of the array and increment the numberOfElements variable. Then it
# should return true. If the intArray is already full, it should just return
# false without doing anything. 

# 13.	Have the locationOf method visit every value in the array. If it finds a
# value that matches the target argument, it should return its location in the
# array (its index). If no values in the array match the target, it should
# return -1. 

# 14.	Have the find method look for the value in the intArray. If a value that
# was put in the intArray matches the argument target, it should return the
# value true. If no values that were place in the intArray matches the target,
# it should return false. Use the locationOf method to implement this behavior. 

# 15.	Have the remove method remove the first array element that matches the
# target. To do this, it should replace it with the last value in the array, and
# decrement the numberOfElements count. Then it should return true. If no
# elements match the target value, it should just return false. 

# 16.	Give the BufferArray class one more method, called stableRemove. Have the
# stableRemove method remove the first array element that matches the target and
# decrement the numberOfElements count. Then it should return true. If no
# elements match the target value, it should just return false. (In data
# structures, “stable” means that the order is not changed.)

import collections

class BufferArray:
    __numberOfElements = 0
    __BUFFER_SIZE = None

    def __init__(self, buffer_size: int = 8):
        """Initialize BufferArray"""
        
        # `collections.UserList` is a Class implementation of the built-in list
        # data type type. We can use so that we may remove some methods from it
        # and avoid using those built-in methods, which would defeat the
        # purpose of the assignment. 

        # Said differently, swapping out the two lines below would work just
        # fine, except we would not be able to remove methods from the builtin
        # list object (e.g. `self.__intArray.append = None` would not work).
        self.__intArray = collections.UserList()
        # self.__intArray = []

    
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
