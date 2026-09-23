# ============================= What is Lambda Function =============================

"""
A Lambda Function is a small anonymous function created using
the `lambda` keyword.

Syntax:

    lambda arguments: expression

A lambda function:
    - Can take any number of arguments.
    - Contains only one expression.
    - Automatically returns the result of the expression.
    - Does not use the `return` keyword.
"""


# ============================= Basic Lambda =============================

# Example 1: Lambda with two arguments

add = lambda a, b: a + b

print(add(2, 3))
# Output: 5


# Example 2: Lambda with one argument

square = lambda x: x * x

print(square(4))
# Output: 16


# ============================= Lambda Returning Multiple Values =============================

"""
A lambda can return multiple values by putting them inside
a tuple.

The expression:

    (a + b, a - b, a * b, a / b)

creates a tuple.
"""

calculate = lambda a, b: (a + b, a - b, a * b, a / b)

sum_result, sub_result, mul_result, div_result = calculate(10, 5)

print(
    "Faruk sum:", sum_result,
    "sub:", sub_result,
    "mul:", mul_result,
    "div:", div_result
)

# Output:
# Faruk sum: 15 sub: 5 mul: 50 div: 2.0


# ============================= Lambda vs Normal Function =============================

# Normal Function

def add_func(a, b):
    return a + b


print(add_func(2, 3))
# Output: 5


# Lambda Function

print((lambda a, b: a + b)(2, 3))
# Output: 5


"""
Differences:

Lambda:
    - Uses the `lambda` keyword.
    - Usually used for short operations.
    - Contains one expression.
    - Automatically returns the expression result.
    - Commonly used as a temporary function.

Normal function:
    - Uses the `def` keyword.
    - Can contain multiple statements.
    - Can contain loops, conditions, try/except, etc.
    - Can contain documentation and complex logic.
    - Uses `return` explicitly.
"""


# ============================= Lambda with No Arguments =============================

no_arg = lambda: "Hello"

print(no_arg())
# Output: Hello


# ============================= Lambda with Single Argument =============================

add_ten = lambda x: x + 10

print(add_ten(5))
# Output: 15


# ============================= Lambda with Multiple Arguments =============================

multiply = lambda x, y: x * y

print(multiply(3, 4))
# Output: 12


# ============================= Lambda Inside Function =============================

"""
A function can return a lambda function.

This is an example of:
    - Higher-Order Function
    - Closure
"""

def power_function(n):
    return lambda x: x ** n


square = power_function(2)
cube = power_function(3)

print(square(5))
# Output: 25

print(cube(2))
# Output: 8


# ============================= Lambda with Higher-Order Functions =============================

nums = [1, 2, 3, 4, 5]


# ============================= map() =============================

"""
map() applies a function to every item.
"""

squared = list(map(lambda x: x ** 2, nums))

print(squared)
# Output: [1, 4, 9, 16, 25]


# ============================= filter() =============================

"""
filter() selects items for which the function returns True.
"""

evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)
# Output: [2, 4]


# ============================= reduce() =============================

from functools import reduce

total = reduce(lambda a, b: a + b, nums)

print(total)
# Output: 15


# ============================= sorted() with key =============================

words = ["apple", "banana", "cherry", "date"]

sorted_by_length = sorted(
    words,
    key=lambda word: len(word)
)

print(sorted_by_length)
# Output: ['date', 'apple', 'banana', 'cherry']


# ============================= Lambda with Conditional Expression =============================

"""
A lambda can contain a conditional expression.

Syntax:

    value_if_true if condition else value_if_false
"""

check_even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_even(5))
# Output: Odd

print(check_even(8))
# Output: Even


# ============================= Lambda with Multiple Conditions =============================

check_number = lambda x: (
    "Positive" if x > 0
    else "Negative" if x < 0
    else "Zero"
)

print(check_number(10))
# Positive

print(check_number(-5))
# Negative

print(check_number(0))
# Zero


# ============================= Lambda Limitations =============================

"""
Lambda functions are intentionally limited.

A lambda can contain:
    - One expression
    - Arithmetic expressions
    - Comparisons
    - Conditional expressions
    - Function calls
    - Tuple/list/dictionary expressions

A lambda cannot contain normal statements such as:
    - return statement
    - assignment statement
    - for statement
    - while statement
    - try/except statement
    - class definition
    - function definition

Example of invalid lambda:

    lambda x: (y = x + 1)

This produces a SyntaxError.
"""


# ============================= Lambda Can Call Functions =============================

"""
Although lambda cannot contain statements such as print(),
it CAN call another function.

Example:
"""

def greet(name):
    return f"Hello, {name}"


greeting = lambda name: greet(name)

print(greeting("Faruk"))
# Output: Hello, Faruk


# ============================= What is Lambda Recursion =============================

"""
Recursion means a function calling itself.

A normal recursive function can easily refer to itself by name.

Example:

    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

Lambda functions are anonymous, so directly referring to themselves
is not straightforward.

Lambda recursion is possible using techniques such as:
    - Passing the function to itself
    - Fixed-point combinators

However, this is uncommon in normal Python programming.
"""


# ============================= Basic Normal Recursion =============================

def countdown(n):

    if n == 0:
        return "Done"

    return f"{n}, " + countdown(n - 1)


print(countdown(5))
# Output:
# 5, 4, 3, 2, 1, Done


# ============================= Lambda Recursion =============================

"""
The following example uses the function-self-passing technique.

The idea is:

    f(f)

The function receives itself as an argument.
"""

factorial_lambda = (
    lambda f:
        lambda n:
            1 if n == 0
            else n * f(f)(n - 1)
)(
    lambda f:
        lambda n:
            1 if n == 0
            else n * f(f)(n - 1)
)


print(factorial_lambda(5))
# Output: 120


# ============================= Factorial using Lambda Recursion =============================

"""
Factorial:

    n! = n × (n-1) × (n-2) × ... × 1

Example:

    5! = 5 × 4 × 3 × 2 × 1
       = 120
"""

factorial = (
    lambda f:
        lambda n:
            1 if n == 0
            else n * f(f)(n - 1)
)(
    lambda f:
        lambda n:
            1 if n == 0
            else n * f(f)(n - 1)
)


print(factorial(6))
# Output: 720


# ============================= Fibonacci using Lambda Recursion =============================

"""
Fibonacci:

    F(n) = F(n-1) + F(n-2)

Base cases:

    F(0) = 0
    F(1) = 1

Sequence:

    0, 1, 1, 2, 3, 5, 8, 13, ...
"""

fibonacci = (
    lambda f:
        lambda n:
            n if n <= 1
            else f(f)(n - 1) + f(f)(n - 2)
)(
    lambda f:
        lambda n:
            n if n <= 1
            else f(f)(n - 1) + f(f)(n - 2)
)


print(fibonacci(7))
# Output: 13


# ============================= Tail Recursion =============================

"""
Tail Recursion:

A recursive function is tail-recursive when the recursive call
is the final operation performed by the function.

Example:

    return tail_fact(n - 1, acc * n)

There is no additional calculation after the recursive call returns.
"""


def tail_fact(n, acc=1):

    if n == 0:
        return acc

    return tail_fact(n - 1, acc * n)


print(tail_fact(5))
# Output: 120


# ============================= Tail Lambda Recursion =============================

tail_factorial = (
    lambda f:
        lambda n, acc=1:
            acc if n == 0
            else f(f)(n - 1, acc * n)
)(
    lambda f:
        lambda n, acc=1:
            acc if n == 0
            else f(f)(n - 1, acc * n)
)


print(tail_factorial(5))
# Output: 120


# ============================= Tail Recursion vs Normal Recursion =============================

"""
Normal Recursion:

    return n * factorial(n - 1)

The multiplication happens after the recursive call returns.

Conceptually:

    factorial(5)
        |
        -> 5 * factorial(4)
                    |
                    -> 4 * factorial(3)
                              |
                              ...


Tail Recursion:

    return tail_fact(n - 1, acc * n)

The accumulated result is passed into the next function call.

Conceptually:

    tail_fact(5, 1)
        |
        -> tail_fact(4, 5)
              |
              -> tail_fact(3, 20)
                    |
                    -> tail_fact(2, 60)
                          |
                          -> tail_fact(1, 120)
                                |
                                -> tail_fact(0, 120)
                                        |
                                        -> 120
"""


# ============================= Important Python Point =============================

"""
Python does NOT perform Tail Call Optimization (TCO).

Therefore, tail recursion in Python does NOT automatically reuse
stack frames.

For large recursive problems, iteration is often preferable when
recursion depth could become large.
"""


# ============================= Lambda Recursion Optimization =============================

"""
Possible optimization techniques:

1. Convert recursion into iteration.

2. Use memoization for repeated recursive calculations.

3. Use functools.lru_cache for suitable recursive functions.

4. Use dynamic programming for overlapping subproblems.

5. Avoid unnecessarily complex lambda recursion in production code.
"""


# ============================= Fibonacci with Memoization =============================

from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci_fast(n):

    if n <= 1:
        return n

    return fibonacci_fast(n - 1) + fibonacci_fast(n - 2)


print(fibonacci_fast(30))
# Output: 832040


# ============================= Practical Recursion Use Cases =============================

"""
Recursion is useful for problems with naturally recursive structures.

Common examples:

    1. Tree traversal
       - Preorder
       - Inorder
       - Postorder

    2. Graph traversal
       - DFS

    3. Backtracking
       - N-Queens
       - Sudoku
       - Maze solving

    4. Divide and Conquer
       - Merge Sort
       - Quick Sort

    5. Dynamic Programming
       - Recursive formulation of subproblems
"""


# ============================= Simple Tree Traversal =============================

tree = {
    "value": 1,
    "children": [
        {"value": 2},
        {
            "value": 3,
            "children": [
                {"value": 4}
            ]
        }
    ]
}


def traverse(node):

    print(node["value"])

    for child in node.get("children", []):
        traverse(child)


traverse(tree)

# Output:
# 1
# 2
# 3
# 4


# ============================= Lambda + Higher-Order Function Relationship =============================

"""
Lambda functions are often used with Higher-Order Functions.

Example:

    nums = [1, 2, 3, 4, 5]

    map(
        lambda x: x * 2,
        nums
    )

Here:

    map()   -> Higher-Order Function
    lambda  -> Callback Function
    x * 2   -> Lambda expression
"""


# ============================= Lambda + Callback =============================

def calculate(a, b, operation):

    return operation(a, b)


result = calculate(
    10,
    5,
    lambda x, y: x + y
)

print(result)
# Output: 15


# Here:
#
# calculate() -> Higher-Order Function
#
# lambda x, y: x + y
#             -> Callback Function
#
# The lambda is passed to calculate() as an argument.


# ============================= Lambda Summary =============================

"""
Lambda Function
---------------
A small anonymous function defined using lambda.

Syntax:

    lambda arguments: expression


Examples:

    lambda x: x * 2

    lambda a, b: a + b

    lambda x: "Even" if x % 2 == 0 else "Odd"


Common Uses:

    map()
    filter()
    reduce()
    sorted()
    Higher-Order Functions
    Callbacks
    Short one-time operations


Important:

    Lambda
       |
       +-- Anonymous function
       |
       +-- One expression
       |
       +-- Automatically returns expression result
       |
       +-- Commonly used as callback
       |
       +-- Can be returned from another function
       |
       +-- Can participate in recursion, but this is uncommon
"""


# ============================= Final Concept =============================

"""
                    Lambda Function
                          |
          +---------------+---------------+
          |               |               |
       map()           filter()        sorted()
          |               |               |
       Transform        Select           Key
          |
          |
    Higher-Order Function
          |
          |
       Callback
          |
          |
       Lambda


Recursion:

    Function
       |
       └── calls itself
               |
               └── smaller problem
                       |
                       └── base case


Lambda Recursion:

    Lambda
       |
       └── receives itself
               |
               └── f(f)
                    |
                    └── recursive call
"""