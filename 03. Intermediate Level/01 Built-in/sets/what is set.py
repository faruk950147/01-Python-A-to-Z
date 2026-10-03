"""
# Python Set

## 1. What is a Set?

A **set** is a collection of **unique and hashable elements** in Python.

Example:

```python
numbers = {1, 2, 3, 4}
```

### Main Characteristics

* Set does **not allow duplicate elements**.
* Set is **mutable**.
* Set is **iterable**.
* Set does **not support indexing or slicing**.
* Set elements must be **hashable**.
* Set is implemented using hash-table-based mechanisms, which generally provide fast membership testing.
* Sets are dynamically sized.
* Set does not provide sequence-style positional access.

### Important

```python
numbers = {1, 2, 3}

# numbers[0]   # TypeError
```

You cannot access a set using an index.

---

# 2. Basic Set

```python
set1 = {1, 2, 3}

print(set1)
```

Output:

```text
{1, 2, 3}
```

---

# 3. Creating a Set

## Using `{}`

```python
set1 = {1, 2, 3}
```

---

## Using `set()`

```python
set2 = set([1, 2, 3])

print(set2)
```

Output:

```text
{1, 2, 3}
```

---

## Creating Set from String

```python
set3 = set("abc")

print(set3)
```

Possible output:

```text
{'a', 'b', 'c'}
```

> Set display order should not be relied upon.

---

## Creating Set from Range

```python
set4 = set(range(1, 5))

print(set4)
```

Output contains:

```text
{1, 2, 3, 4}
```

---

# 4. Empty Set

This is an important Python concept.

```python
empty = {}
```

`{}` creates an **empty dictionary**, not an empty set.

To create an empty set:

```python
empty_set = set()
```

Check:

```python
print(type(empty_set))
```

Output:

```text
<class 'set'>
```

---

# 5. Duplicate Elements

Sets automatically remove duplicate values.

```python
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)
```

Output contains only:

```text
{1, 2, 3}
```

Therefore:

```python
{1, 2, 2, 3}
```

is effectively the same set as:

```python
{1, 2, 3}
```

---

# 6. Set is Unordered

A set does not provide sequence-style ordering that you can use for indexing.

```python
numbers = {10, 20, 30, 40}
```

You should **not depend on the displayed order** of a set.

Do not write logic like:

```python
numbers[0]
```

because sets are not indexable.

If you need a sequence:

```python
numbers = {10, 20, 30}

items = list(numbers)

print(items)
```

---

# 7. Set is Mutable

You can add or remove elements after creating a set.

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

Output contains:

```text
{1, 2, 3, 4}
```

---

# 8. Set Elements Must Be Hashable

Set elements must be **hashable**.

### Valid elements

```python
data = {
    10,
    3.14,
    "Python",
    (1, 2)
}
```

These types can generally be used as set elements.

### Invalid elements

Lists, dictionaries, and sets are mutable and therefore cannot be set elements:

```python
# data = {
#     [1, 2],
#     [3, 4]
# }
```

This raises:

```text
TypeError: unhashable type: 'list'
```

Similarly:

```python
# {{"name": "Faruk"}}
```

is invalid.

---

# 9. Set with Tuple

A tuple can be a set element if the tuple itself contains only hashable elements.

```python
data = {
    (1, 2),
    (3, 4)
}
```

Valid.

But:

```python
# data = {
#     ([1, 2], 3)
# }
```

is invalid because the tuple contains a list.

---

# 10. Adding Elements

## `add()`

Adds a single element.

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

---

## Adding an Existing Element

```python
numbers = {1, 2, 3}

numbers.add(2)

print(numbers)
```

Nothing changes because sets contain unique elements.

---

# 11. `update()`

Adds multiple elements from an iterable.

```python
numbers = {1, 2, 3}

numbers.update([4, 5, 6])

print(numbers)
```

Output contains:

```text
{1, 2, 3, 4, 5, 6}
```

You can use:

```python
numbers.update((7, 8))
numbers.update({9, 10})
numbers.update(range(11, 14))
```

---

# 12. Important Difference: `add()` vs `update()`

### `add()`

Adds **one object**:

```python
numbers.add(10)
```

### `update()`

Adds elements from an iterable:

```python
numbers.update([10, 20, 30])
```

Remember:

```text
add()    → one element
update() → multiple elements from an iterable
```

---

# 13. Removing Elements

## `remove()`

Removes a specified element.

```python
numbers = {1, 2, 3}

numbers.remove(2)

print(numbers)
```

If the element does not exist:

```python
numbers.remove(10)
```

Python raises:

```text
KeyError
```

---

# 14. `discard()`

Removes an element if it exists.

```python
numbers = {1, 2, 3}

numbers.discard(2)

print(numbers)
```

If the element does not exist:

```python
numbers.discard(10)
```

No error occurs.

### `remove()` vs `discard()`

```text
remove(x)   → KeyError if x doesn't exist
discard(x)  → No error if x doesn't exist
```

---

# 15. `pop()`

Removes and returns an **arbitrary element**.

```python
numbers = {1, 2, 3}

item = numbers.pop()

print(item)
print(numbers)
```

Do not assume which element `pop()` will remove.

### Empty Set

```python
empty = set()

empty.pop()
```

Raises:

```text
KeyError
```

---

# 16. `clear()`

Removes all elements.

```python
numbers = {1, 2, 3}

numbers.clear()

print(numbers)
```

Output:

```text
set()
```

---

# 17. `del`

You can delete the entire set variable:

```python
numbers = {1, 2, 3}

del numbers
```

After this:

```python
# print(numbers)
```

would raise:

```text
NameError
```

`del` deletes the variable/reference; it is not a set method for removing one element.

---

# 18. Looping Through a Set

A set is iterable.

```python
numbers = {1, 2, 3}

for item in numbers:
    print(item)
```

The iteration order should not be relied upon.

---

# 19. Membership Testing

One of the most important uses of a set is fast membership testing.

```python
numbers = {1, 2, 3, 4}

print(3 in numbers)
```

Output:

```text
True
```

Check absence:

```python
print(10 not in numbers)
```

Output:

```text
True
```

---

# 20. Set Union

Union contains all unique elements from both sets.

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
```

Output:

```text
{1, 2, 3, 4, 5}
```

### Method

```python
print(A.union(B))
```

Both mean union:

```python
A | B
A.union(B)
```

---

# 21. Set Intersection

Intersection contains elements common to both sets.

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A & B)
```

Output:

```text
{3}
```

### Method

```python
print(A.intersection(B))
```

---

# 22. Set Difference

`A - B` contains elements that are in `A` but not in `B`.

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A - B)
```

Output:

```text
{1, 2}
```

Reverse:

```python
print(B - A)
```

Output:

```text
{4, 5}
```

### Method

```python
A.difference(B)
```

---

# 23. Symmetric Difference

Contains elements that are in either set, but **not in both**.

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A ^ B)
```

Output:

```text
{1, 2, 4, 5}
```

### Method

```python
A.symmetric_difference(B)
```

---

# 24. Set Operation Cheat Sheet

```text
A | B → Union
A & B → Intersection
A - B → Difference
A ^ B → Symmetric Difference
```

Remember:

```text
| → OR → Union
& → AND → Intersection
- → Difference
^ → XOR → Symmetric Difference
```

---

# 25. Union with Methods

```python
A.union(B)
```

Multiple sets can also be supplied:

```python
A.union(B, C)
```

---

# 26. Intersection with Methods

```python
A.intersection(B)
```

Multiple sets:

```python
A.intersection(B, C)
```

---

# 27. Difference with Methods

```python
A.difference(B)
```

Multiple sets:

```python
A.difference(B, C)
```

Meaning:

```text
Elements in A
that are not in B or C
```

---

# 28. Symmetric Difference

```python
A.symmetric_difference(B)
```

Only works between two sets at a time.

---

# 29. Disjoint Sets

Two sets are **disjoint** if they have no common elements.

```python
A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))
```

Output:

```text
True
```

If they share an element:

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.isdisjoint(B))
```

Output:

```text
False
```

---

# 30. Subset

A set `B` is a subset of `A` if every element of `B` exists in `A`.

```python
A = {1, 2, 3, 4, 5}
B = {1, 2}

print(B.issubset(A))
```

Output:

```text
True
```

### Operator

```python
B <= A
```

Both mean subset-or-equal.

---

# 31. Proper Subset

A is a **proper superset** of B when B is contained in A and the two sets are not equal.

```python
A = {1, 2, 3, 4}
B = {1, 2}

print(B < A)
```

Output:

```text
True
```

### Important

```text
B <= A → subset
B < A  → proper subset
```

---

# 32. Superset

A set `A` is a superset of `B` if every element of `B` exists in `A`.

```python
A = {1, 2, 3, 4}
B = {1, 2}

print(A.issuperset(B))
```

Output:

```text
True
```

### Operator

```python
A >= B
```

---

# 33. Proper Superset

```python
A = {1, 2, 3, 4}
B = {1, 2}

print(A > B)
```

Output:

```text
True
```

Remember:

```text
A >= B → superset
A > B  → proper superset
```

---

# 34. Number of Subsets

If a set contains `n` elements:

```text
Total number of subsets = 2^n
```

Example:

```python
A = {1, 2, 3}

n = len(A)

print(2 ** n)
```

Output:

```text
8
```

For 6 elements:

```text
2^6 = 64
```

---

# 35. Empty Set and Subsets

Every set has at least one subset:

```text
∅
```

For:

```python
A = {1, 2}
```

The subsets are:

```text
∅
{1}
{2}
{1, 2}
```

Total:

```text
2^2 = 4
```

---

# 36. Universal Set

In set theory, a **universal set** contains all elements relevant to a particular problem.

Example:

```python
U = {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

---

# 37. Complement Set

The complement of `A` relative to universal set `U` contains elements that are in `U` but not in `A`.

```python
U = {1, 2, 3, 4, 5, 6, 7, 8, 9}

A = {1, 2, 3}

complement = U - A

print(complement)
```

Output:

```text
{4, 5, 6, 7, 8, 9}
```

Formula:

```text
A' = U - A
```

---

# 38. Set Comprehension

Set comprehension provides a concise way to create a set.

```python
numbers = {x for x in range(1, 6)}

print(numbers)
```

Output contains:

```text
{1, 2, 3, 4, 5}
```

### Syntax

```python
{expression for item in iterable}
```

---

# 39. Set Comprehension with Condition

```python
even_numbers = {
    x
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_numbers)
```

Output:

```text
{2, 4, 6, 8, 10}
```

---

# 40. Set Comprehension Automatically Removes Duplicates

```python
numbers = [1, 2, 2, 3, 3, 4]

unique = {
    x
    for x in numbers
}

print(unique)
```

Output contains:

```text
{1, 2, 3, 4}
```

---

# 41. Removing Duplicates from a List

One of the most common practical uses of sets:

```python
numbers = [1, 2, 2, 3, 3, 4, 4]

unique_numbers = list(set(numbers))

print(unique_numbers)
```

This removes duplicates.

### Important

The resulting order should not be relied upon.

If you need to preserve the original order while removing duplicates, a different approach is preferable, such as:

```python
unique_numbers = list(dict.fromkeys(numbers))
```

---

# 42. Copying a Set

Use `copy()`:

```python
A = {1, 2, 3}

B = A.copy()

B.add(4)

print(A)
print(B)
```

Output:

```text
{1, 2, 3}
{1, 2, 3, 4}
```

`A` and `B` are separate set objects.

---

# 43. Assignment vs Copy

This:

```python
A = {1, 2, 3}
B = A
```

does not create a separate set.

Both variables refer to the same set object.

```python
B.add(4)

print(A)
```

Output:

```text
{1, 2, 3, 4}
```

But:

```python
B = A.copy()
```

creates a separate set.

---

# 44. In-Place Set Operations

Some methods modify the original set.

## `update()`

```python
A = {1, 2}

A.update({2, 3, 4})

print(A)
```

Output:

```text
{1, 2, 3, 4}
```

---

## `intersection_update()`

Keeps only common elements.

```python
A = {1, 2, 3}
B = {2, 3, 4}

A.intersection_update(B)

print(A)
```

Output:

```text
{2, 3}
```

---

## `difference_update()`

Removes elements found in another set.

```python
A = {1, 2, 3}
B = {2, 3, 4}

A.difference_update(B)

print(A)
```

Output:

```text
{1}
```

---

## `symmetric_difference_update()`

Keeps elements present in either set, but not both.

```python
A = {1, 2, 3}
B = {3, 4, 5}

A.symmetric_difference_update(B)

print(A)
```

Output:

```text
{1, 2, 4, 5}
```

---

# 45. Non-Modifying vs Modifying Operations

### Returns a new set

```python
A.union(B)
A.intersection(B)
A.difference(B)
A.symmetric_difference(B)
```

### Modifies the original set

```python
A.update(B)
A.intersection_update(B)
A.difference_update(B)
A.symmetric_difference_update(B)
```

This distinction is important in Python programming.

---

# 46. Set Methods Cheat Sheet

| Method                          | Description                                 |
| ------------------------------- | ------------------------------------------- |
| `add()`                         | Adds one element                            |
| `update()`                      | Adds elements from an iterable              |
| `remove()`                      | Removes an element; `KeyError` if absent    |
| `discard()`                     | Removes an element; no error if absent      |
| `pop()`                         | Removes and returns an arbitrary element    |
| `clear()`                       | Removes all elements                        |
| `copy()`                        | Returns a shallow copy                      |
| `union()`                       | Returns all unique elements                 |
| `intersection()`                | Returns common elements                     |
| `difference()`                  | Returns elements only in the first set      |
| `symmetric_difference()`        | Returns elements in either set but not both |
| `difference_update()`           | Updates set by removing common elements     |
| `intersection_update()`         | Updates set to keep common elements         |
| `symmetric_difference_update()` | Updates set with symmetric difference       |
| `issubset()`                    | Checks subset relationship                  |
| `issuperset()`                  | Checks superset relationship                |
| `isdisjoint()`                  | Checks whether sets have no common elements |

---

# 47. Set Operators Cheat Sheet

```python
A | B
```

→ Union

```python
A & B
```

→ Intersection

```python
A - B
```

→ Difference

```python
A ^ B
```

→ Symmetric Difference

```python
A <= B
```

→ Subset

```python
A < B
```

→ Proper Subset

```python
A >= B
```

→ Superset

```python
A > B
```

→ Proper Superset

---

# 48. Set vs List

| Feature                    | Set            | List             |
| -------------------------- | -------------- | ---------------- |
| Ordered sequence           | No             | Yes              |
| Indexed                    | No             | Yes              |
| Mutable                    | Yes            | Yes              |
| Duplicates                 | No             | Yes              |
| Iterable                   | Yes            | Yes              |
| Hashable elements required | Yes            | No               |
| Membership testing         | Generally fast | Generally linear |
| Syntax                     | `{1, 2}`       | `[1, 2]`         |

### Use List when:

* Order matters.
* You need indexing.
* Duplicates are meaningful.
* You need sequence operations.

### Use Set when:

* You need unique elements.
* Fast membership testing is important.
* You need union/intersection/difference operations.

---

# 49. Set vs Dictionary

| Feature          | Set           | Dictionary           |
| ---------------- | ------------- | -------------------- |
| Stores           | Unique values | Key-value pairs      |
| Duplicate values | No            | Values can duplicate |
| Indexed          | No            | No                   |
| Mutable          | Yes           | Yes                  |
| Empty `{}`       | No            | Yes                  |
| Syntax           | `{1, 2, 3}`   | `{"a": 1}`           |

Important:

```python
{}
```

→ Empty dictionary

```python
set()
```

→ Empty set

---

# 50. Set vs Tuple

| Feature          | Set | Tuple                                   |
| ---------------- | --- | --------------------------------------- |
| Ordered sequence | No  | Yes                                     |
| Indexed          | No  | Yes                                     |
| Mutable          | Yes | No                                      |
| Duplicates       | No  | Yes                                     |
| Hashable itself  | No  | Often yes, if all elements are hashable |

---

# 51. Time Complexity

For a Python set, membership operations are generally **O(1) average case**.

| Operation        |                                                           Average Complexity |
| ---------------- | ---------------------------------------------------------------------------: |
| `x in set`       |                                                                       `O(1)` |
| `x not in set`   |                                                                       `O(1)` |
| `add()`          |                                                                       `O(1)` |
| `remove()`       |                                                                       `O(1)` |
| `discard()`      |                                                                       `O(1)` |
| `pop()`          |                                                               `O(1)` average |
| `union()`        |                                                                   `O(n + m)` |
| `intersection()` | Depends on operand sizes; generally proportional to the relevant smaller set |
| `difference()`   |                                                     Depends on operand sizes |
| `clear()`        |                                                                       `O(n)` |

> These are average-case expectations; hash-table operations can have different worst-case behavior.

---

# 52. Why is Set Membership Fast?

Sets use hash-based lookup.

For example:

```python
numbers = {10, 20, 30, 40, 50}

print(30 in numbers)
```

Python can generally locate the element through hashing rather than scanning every element one by one.

Compare:

```text
List search → O(n) average
Set search  → O(1) average
```

This is why sets are very useful in DSA problems.

---

# 53. Common Set Errors

## TypeError: 'set' object is not subscriptable

Wrong:

```python
numbers = {10, 20, 30}

print(numbers[0])
```

Sets do not support indexing.

---

## TypeError: unhashable type: 'list'

Wrong:

```python
data = {[1, 2], [3, 4]}
```

Lists cannot be set elements.

---

## KeyError from `remove()`

```python
numbers = {1, 2, 3}

numbers.remove(10)
```

Because `10` doesn't exist.

Use:

```python
numbers.discard(10)
```

if you do not want an error.

---

# 54. Important Interview Questions

## Q1. What is a set?

A set is a mutable collection of unique, hashable elements.

---

## Q2. Does a set allow duplicate elements?

No.

```python
{1, 2, 2, 3}
```

becomes a set containing only unique elements.

---

## Q3. Is a set indexed?

No.

```python
numbers[0]
```

raises `TypeError`.

---

## Q4. Can a set contain a list?

No.

Lists are unhashable.

---

## Q5. Can a set contain a tuple?

Yes, if the tuple contains only hashable elements.

---

## Q6. Difference between `remove()` and `discard()`?

```text
remove()  → raises KeyError if element doesn't exist
discard() → does nothing if element doesn't exist
```

---

## Q7. Difference between `add()` and `update()`?

```text
add()    → adds one element
update() → adds elements from an iterable
```

---

## Q8. What does `pop()` do?

It removes and returns an arbitrary element.

It does not mean "remove the last element" as it does for lists.

---

## Q9. How do you create an empty set?

```python
set()
```

Not:

```python
{}
```

because `{}` creates an empty dictionary.

---

## Q10. What is the average time complexity of set membership?

```text
O(1)
```

on average.

---

## Q11. What is the difference between `A | B` and `A.union(B)`?

Both perform union and return a set containing elements from both sets.

```python
A | B
A.union(B)
```

---

## Q12. What is symmetric difference?

Elements present in either set but not in both.

```python
A ^ B
```

---

# 55. Practical Example

```python
students_python = {
    "Faruk",
    "Ahmed",
    "Karim",
    "Rahim"
}

students_django = {
    "Faruk",
    "Karim",
    "Hasan"
}

# Students who know both
both = students_python & students_django

# Students who know Python only
python_only = students_python - students_django

# Students who know Django only
django_only = students_django - students_python

# Students who know either Python or Django, but not both
only_one = students_python ^ students_django

print("Both:", both)
print("Python only:", python_only)
print("Django only:", django_only)
print("Only one:", only_one)
```

This is a practical example of using set operations for data analysis.

---

# 56. DSA Example: Duplicate Detection

A set can be used to detect duplicates.

```python
numbers = [1, 2, 3, 4, 2, 5]

seen = set()

for number in numbers:
    if number in seen:
        print("Duplicate:", number)
        break

    seen.add(number)
```

Output:

```text
Duplicate: 2
```

Average complexity:

```text
Time  → O(n)
Space → O(n)
```

---

# 57. DSA Example: Remove Duplicates

```python
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = set(numbers)

print(unique)
```

Output contains:

```text
{1, 2, 3, 4, 5}
```

If a list is required:

```python
unique = list(set(numbers))
```

Remember that this does not preserve the original list order.

---

# 58. Final Quick Cheat Sheet

```python
# Create
A = {1, 2, 3}

# Empty set
A = set()

# Add
A.add(4)

# Add multiple
A.update([5, 6])

# Remove
A.remove(6)

# Safe remove
A.discard(10)

# Remove arbitrary element
A.pop()

# Clear
A.clear()

# Membership
3 in A

# Union
A | B

# Intersection
A & B

# Difference
A - B

# Symmetric difference
A ^ B

# Subset
A <= B

# Proper subset
A < B

# Superset
A >= B

# Proper superset
A > B

# Disjoint
A.isdisjoint(B)

# Copy
B = A.copy()

# Set comprehension
squares = {x * x for x in range(1, 6)}
```

---

# 59. Final Summary

```text
Python Set
    ↓
Unique Elements
    ↓
Hashable Elements Required
    ↓
Mutable
    ↓
Iterable
    ↓
No Indexing / Slicing
    ↓
Fast Membership Testing
    ↓
add() / update()
    ↓
remove() / discard() / pop() / clear()
    ↓
Union
    ↓
Intersection
    ↓
Difference
    ↓
Symmetric Difference
    ↓
Subset / Superset
    ↓
Disjoint
    ↓
Set Comprehension
```

# One-Line Definition

> **A set is a mutable collection of unique, hashable elements that supports efficient membership testing and mathematical set operations such as union, intersection, difference, and symmetric difference.**

"""