"""Postfix and infix expression conversion and evaluation.

This module provides common functions for converting between infix and postfix and
evaluating postfix expressions.

"""

try:
    from .stack import Stack
    from .queue import Queue as Q
except ImportError: # pragma: no cover
    from stack import Stack
    from .queue import Queue as Q

OPERATORS = [
    "+",
    "-",
    "*",
    "/",
    "^",
]
LPARENS = "("
RPARENS = ")"
PARENS = [LPARENS, RPARENS]

def apply_operator(operator, operand1, operand2):
    match operator:
        case "+":
            return operand1 + operand2
        case "-":
            return operand1 - operand2
        case "*":
            return operand1 * operand2
        case "/":
            return int(operand1 / operand2)
        case "^":
            return operand1 ** operand2

def postfix_eval(postfix: str) -> int:
    """Evaluate a postfix expression.

    Assumes operands are integers and operators are any of +, -, *, /, or ^.

    args:
        postfix (str): A postfix expression containing only operators and operands.

    returns:
        int: The result of the postfix expression.
    
    """
    stack = Stack()

    for token in tokenize(postfix):
        if token in OPERATORS:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.push(apply_operator(token, int(operand1), int(operand2)))
        else:
            stack.push(token)

    return stack.pop()

def tokenize(expr: str) -> list:
    """
    Tokenize an expression into numbers, operators, and parentheses.

    args:
        expr (str): The expression to tokenize.

    returns:
        Generator: Yields tokens one at a time.
    """
    number = ''
    for char in expr:
        if char.isdigit():
            number += char  # Accumulate the digit characters
        else:
            if number:
                yield int(number)  # Yield the accumulated number
                number = ''  # Reset for the next number
            if char in OPERATORS or char in PARENS:
                yield char
            elif char == " ":
                continue  # Ignore spaces
            else:
                raise ValueError(f"Invalid character in expression: {char}.")

    # Yield the last number if there is one
    if number:
        yield int(number)

def infix_to_postfix(infix: str) -> str:
    """
    Convert an infix expression to a postfix expression.

    args:
        infix (str): An infix expression.

    returns:
        str: The corresponding postfix expression.
    """
    precedence = {
        "^": 4,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }

    output = []
    op_stack = Stack()

    for token in tokenize(infix):
        if isinstance(token, int) or token.isalpha():  # Operand
            output.append(token)
        elif token == LPARENS:
            op_stack.push(token)
        elif token == RPARENS:
            top_token = op_stack.pop()
            while top_token != LPARENS:
                output.append(top_token)
                top_token = op_stack.pop()
        else:  # Operator
            while (not op_stack.is_empty()) and (precedence[op_stack.peek()] >= precedence[token]):
                output.append(op_stack.pop()) ### TEST COVERAGE SHOW THIS LINE NEVER EXECUTES
            op_stack.push(token)

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return ' '.join(map(str, output))