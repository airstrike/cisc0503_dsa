import os
import sys
import unittest

# Add the path to the src directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

from cisc0503_dsa import Stack, infix_to_postfix, postfix_eval

class TestPostfix(unittest.TestCase):

    def setUp(self):
        self.expressions = [
            # ("1", "1", 1),
            # ("* 3", "3 *", 3),
            ("1 - 2", "1 2 -", -1),
            ("1 * 2 - 3", "1 2 * 3 -", -1),
            ("2 / 1 ^ 3", "2 1 3 ^ /", 2),
            ("(2 / 1) ^ 3", "2 1 / 3 ^", 8),
            ("(1 + 2) * 3", "1 2 + 3 *", 9),
            ("2 * (1 + 3)", "2 1 3 + *", 8),
            ("(1 + 2) * (3 + 4)", "1 2 + 3 4 + *", 21),
            ("(1 + (2 + 3) * 4) - 5", "1 2 3 + 4 * + 5 -", 16),
            ("((1 + 2) - 3)", "1 2 + 3 -", 0),
            ("(10 + 20) * 30", "10 20 + 30 *", 900),
        ]

    def test_postfix_eval(self):
        for (_, postfix, result) in self.expressions:
            self.assertEqual(postfix_eval(postfix), result)

    def test_infix_to_postfix(self):
        for (infix, postfix, _) in self.expressions:
            self.assertEqual(infix_to_postfix(infix), postfix)
    
    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            postfix_eval("1 2 $")


