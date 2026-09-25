# ============================= What is Recursion =============================

"""
Recursion is a programming technique where a function calls itself
to solve a problem.

A recursive problem is usually divided into smaller versions of
the same problem.

Every recursive function should have:

    1. Base Case
    2. Recursive Case


Base Case:
    The condition that stops recursion.

Recursive Case:
    The part where the function calls itself with a smaller
    or simpler problem.


General Structure:

    def function(problem):

        if base_case:
            return result

        return function(smaller_problem)
"""


# ============================= Basic Recursion =============================

def demo(n):

    # Base Case
    if n == 0:
        return

    print("demo:", n)

    # Recursive Case
    return demo(n - 1)


demo(5)

# Output:
# demo: 5
# demo: 4
# demo: 3
# demo: 2
# demo: 1


# ============================= Recursion Flow =============================

"""
Example:

    demo(3)

Execution:

    demo(3)
       |
       v
    demo(2)
       |
       v
    demo(1)
       |
       v
    demo(0)
       |
       v
    return


Call Stack:

    demo(3)
    demo(2)
    demo(1)
    demo(0)

Then the calls return in reverse order.
"""


# ============================= Factorial Using Recursion =============================

"""
Factorial:

    n! = n × (n-1) × (n-2) × ... × 1

Example:

    5! = 5 × 4 × 3 × 2 × 1
       = 120
"""


def fact(n):

    # Base Case
    if n == 0 or n == 1:
        return 1

    # Recursive Case
    return n * fact(n - 1)


print(fact(5))
# Output: 120


# ============================= Factorial Recursion Flow =============================

"""
fact(5)

    = 5 * fact(4)
            |
            = 4 * fact(3)
                    |
                    = 3 * fact(2)
                            |
                            = 2 * fact(1)
                                    |
                                    = 1

Returning:

    fact(1) = 1
    fact(2) = 2 * 1 = 2
    fact(3) = 3 * 2 = 6
    fact(4) = 4 * 6 = 24
    fact(5) = 5 * 24 = 120
"""


# ============================= Fibonacci Using Recursion =============================

"""
Fibonacci Sequence:

    F(0) = 0
    F(1) = 1

    F(n) = F(n-1) + F(n-2)

Sequence:

    0, 1, 1, 2, 3, 5, 8, 13, ...
"""


def fib(n):

    # Base Case
    if n == 0 or n == 1:
        return n

    # Recursive Case
    return fib(n - 1) + fib(n - 2)


print(fib(6))
# Output: 8


# ============================= Print Fibonacci Numbers =============================

print("Fibonacci Sequence:")

for i in range(10):
    print(fib(i), end=" ")

print()

# Output:
# 0 1 1 2 3 5 8 13 21 34


# ============================= Fibonacci Recursion Tree =============================

"""
fib(5)

                fib(5)
               /      \
          fib(4)      fib(3)
          /   \       /   \
      fib(3) fib(2) fib(2) fib(1)
       / \
   fib(2) fib(1)

Notice:

    fib(3)
    fib(2)

and other subproblems are calculated repeatedly.

Therefore, naive recursive Fibonacci has exponential
time complexity.

Approximate Complexity:

    Time  : O(2^n)
    Space : O(n)

Space is O(n) because the maximum recursion depth is O(n).
"""


# ============================= Sum Using Recursion =============================

def recursive_sum(n):

    # Base Case
    if n == 0:
        return 0

    # Recursive Case
    return n + recursive_sum(n - 1)


print(recursive_sum(5))
# Output: 15

# 5 + 4 + 3 + 2 + 1 = 15


# ============================= Print List Using Recursion =============================

def print_list(lst):

    # Base Case
    if len(lst) == 0:
        return

    print(lst[0])

    # Recursive Case
    print_list(lst[1:])


print_list([1, 2, 3, 4, 5])


# ============================= Print List Using Index =============================

"""
Using an index avoids creating a new sliced list on every call.
"""


def print_list_index(lst, idx=0):

    # Base Case
    if idx == len(lst):
        return

    print(lst[idx])

    # Recursive Case
    print_list_index(lst, idx + 1)


print_list_index([1, 2, 3, 4, 5])


# ============================= Print List in Reverse =============================

def print_reverse(lst, idx=0):

    # Base Case
    if idx == len(lst):
        return

    # Recursive call first
    print_reverse(lst, idx + 1)

    # Print while returning
    print(lst[idx])


print_reverse([1, 2, 3, 4, 5])

# Output:
# 5
# 4
# 3
# 2
# 1


# ============================= Efficient Palindrome Using Recursion =============================

"""
A palindrome reads the same from both directions.

Examples:

    madam
    racecar
    level


Efficient recursive approach:

    1. Use left and right pointers.
    2. Compare the characters.
    3. Move left forward.
    4. Move right backward.
    5. Stop when the pointers meet or cross.


Important:
The string should be normalized before calling the recursive
function if we want to ignore:
    - spaces
    - punctuation
    - capitalization
"""


def is_palindrome(s, left=0, right=None):

    if right is None:
        right = len(s) - 1

    # Base Case
    if left >= right:
        return True

    # If characters do not match
    if s[left] != s[right]:
        return False

    # Recursive Case
    return is_palindrome(s, left + 1, right - 1)


def normalize_string(s):

    return "".join(
        char.lower()
        for char in s
        if char.isalnum()
    )


text = "Madam, I'm Adam"

normalized = normalize_string(text)

print(is_palindrome(normalized))
# Output: True


# ============================= Palindrome with String Slicing =============================

"""
Another approach is to recursively create a smaller substring.

Example:

    "madam"
       |
       -> "ada"
              |
              -> "d"


However, s[1:-1] creates a new string each time.

Therefore, this approach requires additional copying work.
"""


def is_palindrome_slice(s):

    # Base Case
    if len(s) <= 1:
        return True

    # Check first and last characters
    if s[0] != s[-1]:
        return False

    # Recursive Case
    return is_palindrome_slice(s[1:-1])


print(is_palindrome_slice("madam"))
# Output: True


"""
Complexity:

Pointer version:
    Time  : O(n)
    Auxiliary Space: O(n) recursion stack

Slicing version:
    Time  : O(n^2) in Python
    Auxiliary Space: O(n^2) total allocation over the recursion
                     process, with O(n) maximum live recursion depth.

The exact space accounting can vary depending on what is counted,
but the key point is that slicing creates new strings repeatedly.
"""


# ============================= Reverse List Using Two Pointers =============================

"""
Efficient recursive list reversal.

Logic:

    1. Use left and right pointers.
    2. Swap elements.
    3. Move both pointers toward the center.
    4. Stop when left >= right.


Time Complexity:
    O(n)

Auxiliary Space:
    O(n) recursion stack
"""


def reverse_list(lst, left=0, right=None):

    if right is None:
        right = len(lst) - 1

    # Base Case
    if left >= right:
        return lst

    # Swap
    lst[left], lst[right] = lst[right], lst[left]

    # Recursive Case
    return reverse_list(lst, left + 1, right - 1)


numbers = [1, 2, 3, 4, 5]

print(reverse_list(numbers))
# Output:
# [5, 4, 3, 2, 1]


# ============================= Reverse List Using Slicing =============================

"""
Less efficient recursive approach.

Each call creates:
    lst[:-1]

and then creates another list through:

    [lst[-1]] + ...

"""


def reverse_list_slice(lst):

    # Base Case
    if len(lst) == 0:
        return []

    # Recursive Case
    return [lst[-1]] + reverse_list_slice(lst[:-1])


print(reverse_list_slice([1, 2, 3, 4, 5]))

# Output:
# [5, 4, 3, 2, 1]


"""
Complexity:

    Time  : O(n^2)
    Extra space: O(n^2) total allocation across calls

because slicing and list concatenation repeatedly create lists.
"""


# ============================= Tail Recursion =============================

"""
Tail Recursion occurs when the recursive call is the final operation
performed by the function.

Example:

    return tail_factorial(n - 1, acc * n)

There is no pending operation after the recursive call returns.
"""


def tail_factorial(n, acc=1):

    # Base Case
    if n == 0 or n == 1:
        return acc

    # Tail Recursive Case
    return tail_factorial(n - 1, acc * n)


print(tail_factorial(5))
# Output: 120


# ============================= Normal vs Tail Recursion =============================

"""
Normal Recursion:

    return n * factorial(n - 1)

There is still multiplication to perform after
factorial(n - 1) returns.


Tail Recursion:

    return tail_factorial(n - 1, acc * n)

All required information is passed through arguments.

No additional operation is required after the recursive call.
"""


# ============================= IMPORTANT: Python Tail Recursion =============================

"""
Python does NOT perform Tail Call Optimization (TCO).

Therefore:

    Tail recursion in Python does NOT automatically
    reduce recursion stack memory.

This means the following statement is NOT correct:

    "Tail recursion always uses less memory in Python."

In Python:

    Normal recursion -> uses call stack
    Tail recursion   -> also uses call stack

For very deep recursion, an iterative solution is often better.
"""


# ============================= Recursion Depth =============================

"""
Python limits the maximum recursion depth to prevent uncontrolled
stack growth.

The limit can be checked using:

    sys.getrecursionlimit()
"""


import sys

print("Python recursion limit:", sys.getrecursionlimit())


# ============================= Recursion Depth Example =============================

def depth_demo(n):

    if n == 0:
        return

    depth_demo(n - 1)


depth_demo(100)

print("Recursion completed.")


# ============================= Why Recursion Limit Exists =============================

"""
Without a recursion limit, a function that recursively calls itself
forever could continue creating stack frames until the program
runs out of stack memory.

Example:

    def infinite_recursion():
        infinite_recursion()

This will eventually raise:

    RecursionError
"""


# ============================= Recursion Error Example =============================

"""
DO NOT normally execute this example.

def infinite_recursion():
    infinite_recursion()

infinite_recursion()

Result:

    RecursionError:
    maximum recursion depth exceeded
"""


# ============================= Practical Use Cases =============================

"""
Recursion is especially useful for:

    1. Tree Traversal
    2. Graph DFS
    3. Backtracking
    4. Divide and Conquer
    5. Recursive Dynamic Programming
"""


# ============================= 1. Tree Traversal =============================

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(root):

    # Base Case
    if root is None:
        return

    # Recursive Case
    inorder(root.left)

    print(root.value, end=" ")

    inorder(root.right)


# Build Tree

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


print("\nInorder Traversal:")

inorder(root)

# Output:
# 4 2 5 1 3


# ============================= 2. Graph Traversal - DFS =============================

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}


visited = set()


def dfs(node):

    # Avoid visiting the same node repeatedly
    if node in visited:
        return

    print(node, end=" ")

    visited.add(node)

    for neighbor in graph[node]:
        dfs(neighbor)


print("\nDFS Traversal:")

dfs("A")

# Possible Output:
# A B D E F C


# ============================= 3. Backtracking =============================

"""
Backtracking explores possible choices and goes back when
a choice does not lead to the desired solution.

Example:
Generate all permutations.
"""


def backtrack(path, choices):

    # Base Case
    if not choices:
        print(path)
        return

    # Try every available choice
    for i in range(len(choices)):

        choice = choices[i]

        # Make choice
        new_path = path + [choice]

        # Remaining choices
        new_choices = choices[:i] + choices[i + 1:]

        # Recursive Case
        backtrack(new_path, new_choices)


print("\nPermutations:")

backtrack([], [1, 2, 3])


# ============================= Recursion and Stack =============================

"""
Every recursive call creates a new stack frame.

Example:

    fact(3)

Stack:

    fact(3)
       |
    fact(2)
       |
    fact(1)

Then:

    fact(1) returns
       ↓
    fact(2) returns
       ↓
    fact(3) returns


Important:

    More recursive calls
          ↓
    Deeper call stack
          ↓
    More stack memory
"""


# ============================= Recursion Complexity =============================

"""
Example 1: Factorial

    T(n) = T(n-1) + O(1)

Therefore:

    Time  = O(n)
    Space = O(n)


Example 2: Recursive Sum

    T(n) = T(n-1) + O(1)

Therefore:

    Time  = O(n)
    Space = O(n)


Example 3: Naive Fibonacci

    T(n) = T(n-1) + T(n-2) + O(1)

Therefore approximately:

    Time  = O(2^n)
    Space = O(n)


Example 4: Efficient palindrome

    Each character is checked once.

    Time  = O(n)
    Space = O(n)


Example 5: Two-pointer list reversal

    Each element participates in at most one swap.

    Time  = O(n)
    Space = O(n)
"""


# ============================= Recursion vs Iteration =============================

"""
Recursion:

    Function calls itself.
    Often easier for tree and divide-and-conquer problems.
    Uses call stack.

Iteration:

    Uses loops such as:
        for
        while

    Usually avoids recursive call-stack growth.

Example:

Recursive factorial:

    def fact(n):
        if n <= 1:
            return 1
        return n * fact(n - 1)


Iterative factorial:

    def fact_iterative(n):
        result = 1

        for i in range(2, n + 1):
            result *= i

        return result
"""


def fact_iterative(n):

    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


print(fact_iterative(5))
# Output: 120


# ============================= Final Summary =============================

"""
RECURSION
---------

Recursion means:

    A function calls itself.


Every recursive solution generally contains:

    1. Base Case
    2. Recursive Case


Base Case:
    Stops recursion.

Recursive Case:
    Calls the function again with a smaller/simpler problem.


Examples:

    Factorial
    Fibonacci
    Sum
    Palindrome
    Tree Traversal
    DFS
    Backtracking
    Divide and Conquer


Important Complexity:

    Factorial:
        Time  = O(n)
        Space = O(n)

    Sum:
        Time  = O(n)
        Space = O(n)

    Naive Fibonacci:
        Time  = O(2^n)
        Space = O(n)

    Two-pointer palindrome:
        Time  = O(n)
        Space = O(n)

    Two-pointer list reversal:
        Time  = O(n)
        Space = O(n)


Tail Recursion:

    Recursive call is the final operation.

Important:
    Python does NOT perform Tail Call Optimization.


Python Recursion Limit:

    sys.getrecursionlimit()

If recursion becomes too deep:

    RecursionError


Memory Trick:

    Recursion
        ↓
    Base Case
        +
    Recursive Case
        ↓
    Smaller Problem
        ↓
    Base Case
        ↓
    Return Back
"""