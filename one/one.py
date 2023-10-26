import logging
import unittest
from typing import Optional

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('one')

# Assignment #1

# 1.	Create a Python class called BufferArray. It will have an array to hold
# integers and a variable, called numberOfElements, that records how many values
# are being stored in the array.

class BufferArray1(object):
    intArray = []
    numberOfElements = 0

# 2.	Give the BufferArray an integer constant called BUFFER_SIZE and initialize
# it to 8.

class BufferArray2(object):
    intArray = []
    BUFFER_SIZE = 8

# 3.	Give the BufferArray a variable called numberOfElements and initialize it
# to 0.

class BufferArray3(object):
    intArray = []
    numberOfElements = 0
    BUFFER_SIZE = 8

# 4.	Make BUFFER_SIZE, intArray, and numberOfElements private.

class BufferArray4(object):
    # Python doesn't really have 'private' variables. Using a double underscore prefix
    # would make the variable names not directly accessible from outside the class,
    # but they could *still* be accessed via _BufferArray4___BUFFER_SIZE, etc.

    # Since this name mangling is frowned upon by the python community
    # (rightfully so since it doesn't actually prevent access to the variables) but
    # just makes it more cumbersome to access them, we will instead use a single
    # single underscore prefix to indicate that the variable is private. (Also
    # mostly because we do need __BUFFER_SIZE to be accessible by the time we get
    # question 12, since we don't have a sizeOf() function to test that our
    # insert() method is working correctly when the buffer is free or full.

    ___intArray = [] # renamed to intArray per the prompt
    ___numberOfElements = 0
    ___BUFFER_SIZE = 8

# 5.	The BufferArray should have an __init__ which initializes all elements in
# the Buffer to 0. 

class BufferArray5(object):
    __intArray = []
    __numberOfElements = 0
    __BUFFER_SIZE = 8

    def __init__(self):
        for i in range(self.__BUFFER_SIZE):
            self.__intArray.append(0)

# 6.	Give the BufferArray a method called insert() that takes an integer
# argument, called value, and returns a Boolean. For starters, just have it
# return false. 

class BufferArray6(object):
    __intArray: list = []
    __numberOfElements: int = 0
    __BUFFER_SIZE: int = 8

    def __init__(self):
        for i in range(self.__BUFFER_SIZE):
            self.__intArray.append(0)

    def insert(self, value: int):
        return False

# 7.	Give the BufferArray a method called remove() that takes an integer
# argument, called value, and returns a Boolean. For starters, just have it
# return false. 

class BufferArray7(object):
    __intArray = []
    __numberOfElements = 0
    __BUFFER_SIZE = 8

    def __init__(self):
        for i in range(self.__BUFFER_SIZE):
            self.__intArray.append(0)

    def insert(self, value: int):
        return False

    def remove(self, value: int):
        return False

# 8.	Give the BufferArray a method called find() that takes an integer argument,
# called target, and returns a Boolean. For starters, just have it return false.

class BufferArray8(object):
    __intArray = []
    __numberOfElements = 0
    __BUFFER_SIZE = 8

    def __init__(self):
        for i in range(self.__BUFFER_SIZE):
            self.__intArray.append(0)

    def insert(self, value: int):
        return False

    def remove(self, value: int):
        return False

    def find(self, target: int):
        return False

# 9.	Give the BufferArray a public method called display() that takes no
# arguments and prints the list. 

class BufferArray9(object):
    __intArray = []
    __numberOfElements = 0
    __BUFFER_SIZE = 8

    def __init__(self):
        for i in range(self.__BUFFER_SIZE):
            self.__intArray.append(0)

    def insert(self, value: int):
        return False

    def remove(self, value: int):
        return False

    def find(self, target: int):
        return False

    def display(self):
        result = ""
        for i in self.__numberOfElements:
            result += str(i) + " "
        print(result[:-1])

# 10.	Give the BufferArray a method called locationOf() that takes an integer
# argument, called target, and returns an integer. 

class BufferArray10(object):
    __intArray = []
    __numberOfElements = 0
    __BUFFER_SIZE = 8

    def __init__(self):
        for i in range(self.__BUFFER_SIZE):
            self.__intArray.append(0)

    def insert(self, value: int):
        return False

    def remove(self, value: int):
        return False

    def find(self, target: int):
        return False

    def display(self):
        print(self.__intArray)

    def locationOf(self, target: int) -> Optional[int]:
        try:
            return self.__intArray.index(target)
        except ValueError:
            return None

# 11.	Write a test driver for your BufferArray class called BufferArrayMain in a
# different file that tests the insert, display, find, and remove methods. Make
# the tests fairly thorough. 

def test_BufferArray10():
    from tests import BufferArray10Main
    suite = unittest.TestLoader().loadTestsFromTestCase(BufferArray10Main)
    unittest.TextTestRunner(verbosity=2).run(suite)

# 12.	Have the insert method add the value argument to the next available space
# at the end of the array and increment the numberOfElements variable. Then it
# should return true. If the intArray is already full, it should just return
# false without doing anything. 

class BufferArray12(object):
    __intArray = []
    __numberOfElements = 0
    __BUFFER_SIZE = 8

    def __init__(self):
        for i in range(self.__BUFFER_SIZE):
            self.__intArray.append(0)

    def insert(self, value: int) -> bool:
        if self.__numberOfElements == self.__BUFFER_SIZE:
            return False
        self.__intArray[self.__numberOfElements] = value
        self.__numberOfElements += 1
        return True

    def remove(self, value: int):
        return False

    def find(self, target: int):
        return False

    def display(self):
        print(self.__intArray)

    def locationOf(self, target: int) -> Optional[int]:
        try:
            return self.__intArray.index(target)
        except ValueError:
            return None

# 13.	Have the locationOf method visit every value in the array. If it finds a
# value that matches the target argument, it should return its location in the
# array (its index). If no values in the array match the target, it should
# return -1. 

class BufferArray13(object):
    __intArray = []
    __numberOfElements = 0
    __BUFFER_SIZE = 8

    def __init__(self):
        for i in range(self.__BUFFER_SIZE):
            self.__intArray.append(0)

    def insert(self, value: int) -> bool:
        if self.__numberOfElements == self.__BUFFER_SIZE:
            return False
        self.__intArray[self.__numberOfElements] = value
        self.__numberOfElements += 1
        return True

    def remove(self, value: int):
        return False

    def find(self, target: int):
        return False

    def display(self):
        print(self.__intArray)

    def locationOf(self, target: int) -> int:
        index = 0
        for value in self.__intArray:
            if value == target:
                return index
            index += 1
        return -1

# 14.	Have the find method look for the value in the intArray. If a value that
# was put in the intArray matches the argument target, it should return the
# value true. If no values that were place in the intArray matches the target,
# it should return false. Use the locationOf method to implement this behavior. 

class BufferArray14(object):
    __intArray = []
    __numberOfElements = 0
    __BUFFER_SIZE = 8

    def __init__(self):
        for _ in range(self.__BUFFER_SIZE):
            self.__intArray.append(0)

    def insert(self, value: int) -> bool:
        if self.__numberOfElements == self.__BUFFER_SIZE:
            return False
        self.__intArray[self.__numberOfElements] = value
        self.__numberOfElements += 1
        return True

    def remove(self, value: int):
        return False

    def find(self, target: int) -> bool:
        return True if self.locationOf(target) != -1 else False

    def display(self):
        print(self.__intArray)

    def locationOf(self, target: int) -> int:
        index = 0
        for value in self.__intArray:
            if value == target:
                return index
            index += 1
        return -1

# 15.	Have the remove method remove the first array element that matches the
# target. To do this, it should replace it with the last value in the array, and
# decrement the numberOfElements count. Then it should return true. If no
# elements match the target value, it should just return false. 

# 16.	Give the BufferArray class one more method, called stableRemove. Have the
# stableRemove method remove the first array element that matches the target and
# decrement the numberOfElements count. Then it should return true. If no
# elements match the target value, it should just return false. (In data
# structures, “stable” means that the order is not changed.)

if __name__ == '__main__':
    print("Running tests from question 11:")
    test_BufferArray10()
