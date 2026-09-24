# ================================================================================
# 1 map()
# ================================================================================

def square(x):

    return x * x


numbers = [1, 2, 3, 4, 5]

squared_numbers = list(
    map(square, numbers)
)

print(squared_numbers)

# Output:
# [1, 4, 9, 16, 25]


"""
map(function, iterable)

map() applies the function to every element.

Here:

map()
    -> Higher-Order Function

square()
    -> Callback Function


Flow:

1 -> square(1) -> 1
2 -> square(2) -> 4
3 -> square(3) -> 9
4 -> square(4) -> 16
5 -> square(5) -> 25
"""


# ================================================================================
# 2 filter()
# ================================================================================

def is_even(x):

    return x % 2 == 0


numbers = [1, 2, 3, 4, 5]

even_numbers = list(
    filter(is_even, numbers)
)

print(even_numbers)

# Output:
# [2, 4]


"""
filter(function, iterable)

filter() keeps only the elements
for which the callback returns True.


Here:

filter()
    -> Higher-Order Function

is_even()
    -> Callback Function


is_even() is also called a:

Predicate Function


Predicate Function:

A predicate function is a function that returns
a Boolean value:

True
OR
False


Example:

is_even(2)
    -> True

is_even(3)
    -> False
"""


# ================================================================================
# 3 reduce()
# ================================================================================

from functools import reduce


def add(x, y):

    return x + y


numbers = [1, 2, 3, 4, 5]

total = reduce(add, numbers)

print(total)

# Output:
# 15


"""
reduce(function, iterable)

reduce() repeatedly applies a function
and reduces multiple values into a single result.


Flow:

1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15


Here:

reduce()
    -> Higher-Order Function

add()
    -> Callback Function
"""


# ================================================================================
# 4 sorted()
# ================================================================================

numbers = [5, 2, 9, 1, 5, 6]

sorted_numbers = sorted(numbers)

print(sorted_numbers)

# Output:
# [1, 2, 5, 5, 6, 9]


"""
sorted() can also accept a key function.

Example:
"""


words = ["Python", "C", "Java"]

result = sorted(words, key=len)

print(result)

# Output:
# ['C', 'Java', 'Python']


"""
Here:

len
    -> key function


sorted()
    -> uses the callable 'len'
       to determine the sorting key.
"""


# ================================================================================
# 5 any()
# ================================================================================

def is_positive(x):

    return x > 0


numbers = [1, 2, 3, 4, 5]

result = any(
    map(is_positive, numbers)
)

print(result)

# Output:
# True


"""
any() returns True if at least one element is truthy.


Flow:

numbers
    |
    v
map(is_positive, numbers)
    |
    v
[True, True, True, True, True]
    |
    v
any()
    |
    v
True
"""


# ================================================================================
# 6 all()
# ================================================================================

def is_positive(x):

    return x > 0


numbers = [1, 2, 3, 4, 5]

result = all(
    map(is_positive, numbers)
)

print(result)

# Output:
# True


"""
all() returns True only when every element is truthy.


Example:

[True, True, True]
        |
        v
      all()
        |
        v
      True
"""
