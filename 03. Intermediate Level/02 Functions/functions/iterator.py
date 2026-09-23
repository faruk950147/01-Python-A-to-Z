# ============================= What is Iterator =============================

"""
An Iterator is an object that implements the Iterator Protocol.

The Iterator Protocol consists of two methods:

    1. __iter__()
    2. __next__()

__iter__()
----------
Returns the iterator object itself.

__next__()
----------
Returns the next value from the iterator.

When there are no more values, __next__() raises StopIteration.
"""


# ============================= Example: Iterator =============================

my_list = [1, 2, 3, 4, 5]

# A list is an Iterable.
# iter() converts the list into an Iterator.

my_iter = iter(my_list)

print(my_iter)

print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # 4
print(next(my_iter))  # 5

# There are no more values.
#
# print(next(my_iter))
#
# Output:
# StopIteration


# ============================= Iterable vs Iterator =============================

"""
Iterable
--------

An Iterable is an object that can return an iterator.

Examples:

    list
    tuple
    string
    set
    dictionary

Example:

    my_list = [1, 2, 3]

    my_iter = iter(my_list)


Iterator
--------

An Iterator is an object that produces values one at a time
using next().

Example:

    my_iter = iter([1, 2, 3])

    next(my_iter)  # 1
    next(my_iter)  # 2
    next(my_iter)  # 3
"""


# ============================= Iterator Protocol =============================

"""
The Iterator Protocol is a set of rules that defines how an object
behaves as an iterator.

It requires:

    __iter__()
    __next__()


Flow:

    Iterable
       |
       | iter()
       v
    Iterator
       |
       | next()
       v
    Next Value
       |
       | next()
       v
    Next Value
       |
       | next()
       v
    ...
       |
       v
    StopIteration
"""


# ============================= __iter__() Method =============================

"""
__iter__()
----------

The __iter__() method returns an iterator object.

For an iterator, __iter__() normally returns itself.
"""

my_list = [10, 20, 30]

my_iter = iter(my_list)

print(my_iter.__iter__() is my_iter)
# True


# ============================= __next__() Method =============================

"""
__next__()
----------

The __next__() method returns the next available value.

When there are no more values, it raises StopIteration.
"""

my_iter = iter([10, 20, 30])

print(my_iter.__next__())  # 10
print(my_iter.__next__())  # 20
print(my_iter.__next__())  # 30

# print(my_iter.__next__())
# StopIteration


# ============================= Iterator with for Loop =============================

"""
A for loop internally uses the Iterator Protocol.

Conceptually:

    for item in iterable:

is similar to:

    iterator = iter(iterable)

    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
"""

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)


# ============================= How for Loop Works Internally =============================

my_list = [1, 2, 3]

iterator = iter(my_list)

while True:
    try:
        value = next(iterator)
        print(value)
    except StopIteration:
        break


# ============================= Creating a Custom Iterator =============================

"""
We can create our own Iterator by implementing:

    __iter__()
    __next__()
"""


class Count:

    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


counter = Count(5)

print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4

# print(next(counter))
# StopIteration


# ============================= Custom Iterator with for Loop =============================

counter = Count(5)

for value in counter:
    print(value)

# Output:
# 0
# 1
# 2
# 3
# 4


# ============================= Iterator State =============================

"""
An iterator maintains its current state.

Example:

    numbers = [10, 20, 30]

    iterator = iter(numbers)

    next(iterator)  -> 10
    next(iterator)  -> 20
    next(iterator)  -> 30

The iterator remembers where it stopped.

It does NOT restart from the beginning automatically.
"""


# ============================= Iterator vs Iterable =============================

"""
+----------------------+----------------------------------+
| Iterable             | Iterator                        |
+----------------------+----------------------------------+
| Can be iterated      | Produces next value             |
| Has __iter__()       | Has __iter__() and __next__()   |
| May not have         | Must have __next__()            |
| __next__()           |                                 |
| Example: list        | Example: iter(list)             |
+----------------------+----------------------------------+
"""


# ============================= Generator and Iterator =============================

"""
A Generator is a special type of Iterator.

Generator Function:

    def numbers():
        yield 1
        yield 2
        yield 3


Calling:

    numbers()

returns a Generator Object.

The Generator Object supports:

    __iter__()
    __next__()

Therefore:

    Generator -> Iterator
"""


def numbers():
    yield 1
    yield 2
    yield 3


generator = numbers()

print(next(generator))  # 1
print(next(generator))  # 2
print(next(generator))  # 3


# ============================= Final Relationship =============================

"""
Iterable
    |
    | iter()
    v
Iterator
    |
    | next()
    v
Next Value
    |
    | next()
    v
Next Value
    |
    | ...
    v
StopIteration


Examples:

list       -> Iterable
tuple      -> Iterable
string     -> Iterable
set        -> Iterable

iter(list) -> Iterator
iter(tuple) -> Iterator

generator  -> Iterator
"""


# ============================= Important Points =============================

"""
1. Iterator implements the Iterator Protocol.

2. Iterator Protocol requires:
       __iter__()
       __next__()

3. __iter__() returns an iterator.

4. __next__() returns the next value.

5. When no values remain:
       __next__() raises StopIteration.

6. A list is Iterable, but a list itself is not an Iterator.

7. iter(list) creates an Iterator.

8. A Generator is a special type of Iterator.

9. A for loop internally uses iter() and next().

10. An Iterator maintains its current iteration state.
"""


# ============================= Memory Trick =============================

"""
Iterable
    ↓
iter()
    ↓
Iterator
    ↓
next()
    ↓
Value
    ↓
next()
    ↓
Value
    ↓
...
    ↓
StopIteration
"""