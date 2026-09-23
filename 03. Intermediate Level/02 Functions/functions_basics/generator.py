# ============================= What is Generator =============================

"""
A Generator is a special type of iterator that produces values one at a time
instead of creating and storing all values in memory at once.

A generator function uses the `yield` keyword to produce values.

Main Benefits:
    1. Memory efficient
    2. Produces values lazily
    3. Useful for large data
    4. Can be iterated using next()
"""


# ============================= Generator Function =============================

"""
A Generator Function is a function that contains one or more `yield`
statements.

Unlike a normal function:
    - `return` ends the function completely.
    - `yield` pauses the function and saves its current state.
    - The next `next()` call resumes execution from where it stopped.
"""


def generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


# ============================= Generator Object =============================

"""
Calling a generator function does NOT execute the function immediately.

Instead, it creates a Generator Object.

The generator starts executing when we call next().
"""

generator_object = generator()

print(generator_object)

print(next(generator_object))  # 1
print(next(generator_object))  # 2
print(next(generator_object))  # 3
print(next(generator_object))  # 4
print(next(generator_object))  # 5

# If we call next() again:
# print(next(generator_object))
#
# It will raise:
# StopIteration


# ============================= Generator with Parameter =============================

def gen(num):
    for i in range(num):
        yield i


generator_object = gen(10)

print(generator_object)

print(next(generator_object))  # 0
print(next(generator_object))  # 1
print(next(generator_object))  # 2
print(next(generator_object))  # 3
print(next(generator_object))  # 4
print(next(generator_object))  # 5
print(next(generator_object))  # 6
print(next(generator_object))  # 7
print(next(generator_object))  # 8
print(next(generator_object))  # 9


# ============================= Generator Expression =============================

"""
A Generator Expression is similar to a list comprehension,
but it uses parentheses `()` instead of square brackets `[]`.

List Comprehension:
    [i for i in range(10)]

Generator Expression:
    (i for i in range(10))

The generator expression produces values lazily.
"""

generator_expression = (i for i in range(10))

print(generator_expression)

print(next(generator_expression))  # 0
print(next(generator_expression))  # 1
print(next(generator_expression))  # 2
print(next(generator_expression))  # 3
print(next(generator_expression))  # 4
print(next(generator_expression))  # 5
print(next(generator_expression))  # 6
print(next(generator_expression))  # 7
print(next(generator_expression))  # 8
print(next(generator_expression))  # 9


# ============================= Generator vs List =============================

"""
List:
    A list stores all values in memory immediately.

Generator:
    A generator produces values one at a time.

Example:

List:
    [0, 1, 2, 3, 4, ...]

Generator:
    Produces:
        0 -> 1 -> 2 -> 3 -> ...

Important:
    A list is iterable but is NOT an iterator.

Therefore:

    next(list_)

will raise TypeError.

To use next() with a list:

    iterator = iter(list_)
    next(iterator)
"""


# ----------------------------- List -----------------------------

list_ = [i for i in range(10)]

print(list_)

# print(next(list_))
# TypeError: 'list' object is not an iterator


# ----------------------------- Convert List to Iterator -----------------------------

list_iterator = iter(list_)

print(next(list_iterator))  # 0
print(next(list_iterator))  # 1
print(next(list_iterator))  # 2
print(next(list_iterator))  # 3
print(next(list_iterator))  # 4
print(next(list_iterator))  # 5
print(next(list_iterator))  # 6
print(next(list_iterator))  # 7
print(next(list_iterator))  # 8
print(next(list_iterator))  # 9


# ============================= Generator Sum =============================

"""
Generators can be passed to functions such as sum().

The values are generated one at a time and consumed by sum().
"""


def gen_sum(num):
    for i in range(num):
        yield i


print(sum(gen_sum(10)))
# 45
#
# Generated values:
# 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
# = 45


# ============================= Generator Subtraction =============================

def gen_sub(num):
    for i in range(num):
        yield -i


print(sum(gen_sub(10)))
# -45
#
# Generated values:
# 0 + (-1) + (-2) + (-3) + ... + (-9)
# = -45


# ============================= Generator Execution Flow =============================

def numbers():
    print("Start")
    yield 1

    print("After first yield")
    yield 2

    print("After second yield")
    yield 3

    print("End")


g = numbers()

print(next(g))
# Start
# 1

print(next(g))
# After first yield
# 2

print(next(g))
# After second yield
# 3


# ============================= Generator with for Loop =============================

def generate_numbers(num):
    for i in range(num):
        yield i


for value in generate_numbers(5):
    print(value)


# Output:
# 0
# 1
# 2
# 3
# 4


# ============================= Generator Memory Concept =============================

"""
List:

    numbers = [0, 1, 2, 3, 4, ..., 1000000]

    All values are created and stored in memory.

Generator:

    numbers = (i for i in range(1000000))

    Values are generated only when requested.

Conceptually:

List:
    Memory
    ┌─────────────────────────────┐
    │ 0 │ 1 │ 2 │ 3 │ 4 │ ...    │
    └─────────────────────────────┘

Generator:
    Memory
    ┌─────────────────────────────┐
    │ Generator State             │
    │ Current Position            │
    └─────────────────────────────┘
             │
             ▼
          next()
             │
             ▼
          next value
"""


# ============================= Generator vs Iterator =============================

"""
Iterable:
    An object that can return an iterator using iter().

Examples:
    list
    tuple
    string
    dictionary
    set

Iterator:
    An object that produces values using next().

Example:
    iterator = iter([1, 2, 3])

Generator:
    A special type of iterator created using:
        - generator function
        - generator expression


Relationship:

Iterable
   │
   └── iter()
         │
         ▼
      Iterator
         │
         └── next()

Generator
   │
   └── is an Iterator
"""


# ============================= Important Generator Keywords =============================

"""
yield
-----
Produces a value and pauses the generator.

next()
------
Requests the next value from the generator.

StopIteration
-------------
Raised automatically when the generator has no more values.

iter()
------
Converts an iterable into an iterator.
"""


# ============================= Generator vs List Summary =============================

"""
+----------------------+-----------------------------+
| List                 | Generator                  |
+----------------------+-----------------------------+
| Uses []              | Uses yield or ()           |
| Stores all values    | Produces values lazily     |
| More memory          | Memory efficient           |
| Reusable             | Usually one-time iteration |
| Iterable             | Iterator                   |
| next(list) -> Error  | next(generator) -> Works   |
+----------------------+-----------------------------+
"""


# ============================= Final Concept =============================

"""
Generator Function
        │
        │ call function
        ▼
Generator Object
        │
        │ next()
        ▼
Execute until yield
        │
        ▼
Return value
        │
        ▼
Pause and save state
        │
        │ next()
        ▼
Resume from previous position
        │
        ▼
Next yield
        │
        ▼
Continue...
        │
        ▼
No more yield
        │
        ▼
StopIteration
"""