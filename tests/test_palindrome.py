import os
import sys
import unittest

# Add the path to the src directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

from cisc0503_dsa.palindrome import StackForPalindrome, QueueForPalindrome
from cisc0503_dsa import Stack, Queue

PALINDROMES = [
    "racecar",
    "A man, a plan, a canal, Panama!",
    "Was it a car or a cat I saw?",
    "No 'x' in Nixon",
    "A Toyota's a Toyota",
]

NON_PALINDROMES = [
    "Hello, World!",
    "This is not a palindrome",
    "This is a palindrome",
]

def is_palindrome(string: str) -> bool:
    """
    Returns True if the given string is a palindrome, False otherwise.

    args:
        string - the string to check.

    """
    string = f"{string}" # Cast input to string
    if len(string) < 2:
        raise ValueError("String must be at least 2 characters long")

    queue = Queue()
    stack = Stack()

    for char in string:
        if char.isalpha():
            queue.enqueue(char.lower())
            stack.push(char.lower())

    while not queue.is_empty():
        dq = queue.dequeue()
        p = stack.pop()
        if dq != p:
            return False

    return True

def is_palindrome_with_provided_classes(string: str) -> bool:
    """
    Returns True if the given string is a palindrome, False otherwise.

    Uses the classes provided to us with Stack_List.py and Que_List.py

    args:
        string - the string to check.

    """
    string = f"{string}" # Cast input to string
    if len(string) < 2:
        raise ValueError("String must be at least 2 characters long")

    # Initialize stacks and queue
    stack = StackForPalindrome()
    stack2 = StackForPalindrome()
    queue = QueueForPalindrome()

    # Add characters to stack
    for ch in string:
        if ch.isalpha():
            stack.push(ch.lower())
            stack2.push(ch.lower())

    # Pop from stack and add to queue
    while not stack.isEmpty():
        queue.enque(stack.peek())
        stack.pop()

    if f"{queue}" == f"{stack2}":
        return True

    return False

def palindromeTest(test: str): # pragma: no cover
    """
    Alias for `is_palindrome_with_provided_classes()` to match question prompt

    """
    return is_palindrome_with_provided_classes(test)

class PalindromeTest(unittest.TestCase):
    """Test the is_palindrome function
    with our own classes and the ones provided to us.
    
    """
    def test_palindromes(self):
        """Ensure is_palindrome returns True for palindromes."""
        for palindrome in PALINDROMES:
            self.assertTrue(is_palindrome(palindrome))

    def test_non_palindromes(self):
        """Ensure is_palindrome returns False for non-palindromes."""
        for non_palindrome in NON_PALINDROMES:
            self.assertFalse(is_palindrome(non_palindrome))

    def test_palindromes_with_provided_classes(self):
        """Ensure is_palindrome_with_provided_classes returns True for palindromes."""
        for palindrome in PALINDROMES:
            self.assertTrue(is_palindrome_with_provided_classes(palindrome))

    def test_non_palindromes_with_provided_classes(self):
        """Ensure is_palindrome_with_provided_classes returns False for non-palindromes."""
        for non_palindrome in NON_PALINDROMES:
            self.assertFalse(is_palindrome_with_provided_classes(non_palindrome))
    
    def test_string_too_short(self):
        """Ensure is_palindrome raises a ValueError if the string is too short."""
        for s in ["", "a", 1]:
            with self.assertRaises(ValueError):
                is_palindrome(s)
            with self.assertRaises(ValueError):
                is_palindrome_with_provided_classes(s)
        for s in ["aaa", "abc"]:
            # does not return error
            is_palindrome(s)
            is_palindrome_with_provided_classes(s)

        


if __name__ == '__main__': # pragma: no cover
    unittest.main()