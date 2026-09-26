"""
# 8. What is List Comprehension?

## 1. What is List Comprehension?

**List Comprehension** is a concise and readable way to create a new list from an 
existing iterable such as a `list`, `range`, or `string`.

It often allows us to replace a traditional `for` loop with a single line of code.

### Example

Using a normal `for` loop:

```python
squares = []

for x in range(10):
    squares.append(x ** 2)

print(squares)
```

Output:

```text
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Using List Comprehension:

```python
squares = [x ** 2 for x in range(10)]

print(squares)
```

Output:

```text
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

# 2. Basic Syntax

The basic syntax of List Comprehension is:

```python
[expression for item in iterable]
```

### Parts

```text
[expression for item in iterable]
     │          │        │
     │          │        └── Source of data
     │          └─────────── Each element
     └────────────────────── Value to create
```

### Example

```python
squares = [x ** 2 for x in range(5)]
```

Here:

* `x ** 2` → expression
* `x` → item
* `range(5)` → iterable

Result:

```python
[0, 1, 4, 9, 16]
```

---

# 3. Simple Example

```python
numbers = [1, 2, 3, 4, 5]

result = [x * 2 for x in numbers]

print(result)
```

Output:

```text
[2, 4, 6, 8, 10]
```

Each number is multiplied by `2`.

---

# 4. List Comprehension with range()

```python
numbers = [x for x in range(10)]

print(numbers)
```

Output:

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

This can also be written as:

```python
numbers = list(range(10))
```

---

# 5. Square of Numbers

```python
squares = [x ** 2 for x in range(10)]

print(squares)
```

Output:

```text
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

# 6. Cube of Numbers

```python
cubes = [x ** 3 for x in range(1, 6)]

print(cubes)
```

Output:

```text
[1, 8, 27, 64, 125]
```

---

# 7. List Comprehension with String

We can create a list of characters from a string.

```python
chars = [c for c in "python"]

print(chars)
```

Output:

```text
['p', 'y', 't', 'h', 'o', 'n']
```

---

# 8. Convert Characters to Uppercase

```python
chars = [c.upper() for c in "python"]

print(chars)
```

Output:

```text
['P', 'Y', 'T', 'H', 'O', 'N']
```

---

# 9. List Comprehension with Condition

We can use a condition in List Comprehension.

### Syntax

```python
[expression for item in iterable if condition]
```

Example:

```python
even = [x for x in range(10) if x % 2 == 0]

print(even)
```

Output:

```text
[0, 2, 4, 6, 8]
```

The condition:

```python
x % 2 == 0
```

selects only even numbers.

---

# 10. Odd Numbers

```python
odd = [x for x in range(10) if x % 2 != 0]

print(odd)
```

Output:

```text
[1, 3, 5, 7, 9]
```

---

# 11. Numbers Greater Than 5

```python
numbers = [1, 3, 5, 7, 9, 10]

result = [x for x in numbers if x > 5]

print(result)
```

Output:

```text
[7, 9, 10]
```

---

# 12. Multiple Conditions

We can use multiple conditions.

```python
numbers = range(20)

result = [
    x for x in numbers
    if x % 2 == 0 and x > 10
]

print(result)
```

Output:

```text
[12, 14, 16, 18]
```

---

# 13. if-else in List Comprehension

When using `if-else`, the syntax is different.

### Syntax

```python
[expression_if_true if condition else expression_if_false
 for item in iterable]
```

Example:

```python
numbers = range(10)

result = [
    "Even" if x % 2 == 0 else "Odd"
    for x in numbers
]

print(result)
```

Output:

```text
['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
```

### Important

Filtering:

```python
[expression for item in iterable if condition]
```

Here the `if` comes at the end.

But with `if-else`:

```python
[value_if_true if condition else value_if_false for item in iterable]
```

The `if-else` is part of the expression.

---

# 14. Nested List Comprehension

We can use more than one `for` loop inside a List Comprehension.

### Example

```python
result = [
    (x, y)
    for x in [1, 2, 3]
    for y in [4, 5]
]

print(result)
```

Output:

```text
[
    (1, 4),
    (1, 5),
    (2, 4),
    (2, 5),
    (3, 4),
    (3, 5)
]
```

This works like nested `for` loops.

---

# 15. Flatten a Nested List

Suppose we have:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

We can convert it into a single list:

```python
result = [x for row in matrix for x in row]

print(result)
```

Output:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Equivalent normal loop:

```python
result = []

for row in matrix:
    for x in row:
        result.append(x)
```

---

# 16. Get String Lengths

```python
words = ["Python", "Django", "Java"]

lengths = [len(word) for word in words]

print(lengths)
```

Output:

```text
[6, 6, 4]
```

---

# 17. Convert Strings to Lowercase

```python
names = ["FARUK", "AHMED", "PYTHON"]

result = [name.lower() for name in names]

print(result)
```

Output:

```text
['faruk', 'ahmed', 'python']
```

---

# 18. Convert Strings to Uppercase

```python
names = ["faruk", "ahmed", "python"]

result = [name.upper() for name in names]

print(result)
```

Output:

```text
['FARUK', 'AHMED', 'PYTHON']
```

---

# 19. Remove Empty Strings

```python
data = ["Python", "", "Django", "", "Java"]

result = [x for x in data if x]

print(result)
```

Output:

```text
['Python', 'Django', 'Java']
```

---

# 20. Extract Positive Numbers

```python
numbers = [-5, 3, -2, 8, -1, 10]

positive = [x for x in numbers if x > 0]

print(positive)
```

Output:

```text
[3, 8, 10]
```

---

# 21. Extract Negative Numbers

```python
numbers = [-5, 3, -2, 8, -1, 10]

negative = [x for x in numbers if x < 0]

print(negative)
```

Output:

```text
[-5, -2, -1]
```

---

# 22. Replace Negative Numbers with 0

```python
numbers = [-5, 3, -2, 8, -1, 10]

result = [x if x >= 0 else 0 for x in numbers]

print(result)
```

Output:

```text
[0, 3, 0, 8, 0, 10]
```

---

# 23. Dictionary Comprehension

Dictionary Comprehension has a similar concept.

### Syntax

```python
{key: value for item in iterable}
```

Example:

```python
squares = {x: x ** 2 for x in range(5)}

print(squares)
```

Output:

```text
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

# 24. Set Comprehension

Set Comprehension uses:

```python
{expression for item in iterable}
```

Example:

```python
numbers = [1, 2, 2, 3, 3, 4]

result = {x for x in numbers}

print(result)
```

Output:

```text
{1, 2, 3, 4}
```

A set automatically removes duplicate values.

---

# 25. Generator Expression

List Comprehension:

```python
[x ** 2 for x in range(10)]
```

This creates the entire list.

Generator Expression:

```python
(x ** 2 for x in range(10))
```

A generator produces values when they are needed instead of creating the entire list immediately.

This can be more memory-efficient when working with large data.

---

# 26. List Comprehension vs for Loop

### Normal Loop

```python
squares = []

for x in range(5):
    squares.append(x ** 2)
```

### List Comprehension

```python
squares = [x ** 2 for x in range(5)]
```

Both produce:

```text
[0, 1, 4, 9, 16]
```

---

# 27. Common Mistake

Incorrect:

```python
[x for x in range(10) if x % 2 == 0 else x]
```

The `if-else` syntax is incorrect.

Correct:

```python
[x if x % 2 == 0 else 0 for x in range(10)]
```

---

# 28. When Should You Use List Comprehension?

Use List Comprehension when:

* You need to create a new list.
* You need to transform elements.
* You need to filter elements.
* The logic is simple.
* The resulting code remains readable.

Example:

```python
even_squares = [
    x ** 2
    for x in range(10)
    if x % 2 == 0
]
```

Output:

```text
[0, 4, 16, 36, 64]
```

---

# 29. When Should You Avoid List Comprehension?

Avoid very complex List Comprehensions.

For example, if the logic contains many nested loops and conditions, a normal `for` loop may be easier to understand.

Readable code:

```python
result = []

for user in users:
    if user.is_active:
        if user.age >= 18:
            result.append(user.name)
```

Trying to put complicated logic into one line can make the code difficult to maintain.

---

# 30. Advantages

1. Shorter code
2. Often more readable for simple operations
3. Easy to create new lists
4. Easy filtering
5. Easy transformation
6. A common Pythonic programming style

---

# 31. Disadvantages

1. Complex comprehensions can reduce readability.
2. Beginners may find the syntax confusing at first.
3. Very complex operations are often clearer with normal loops.
4. A List Comprehension creates the entire list in memory.

---

# 32. Complete Example

```python
numbers = range(1, 11)

squares = [x ** 2 for x in numbers]

even = [x for x in numbers if x % 2 == 0]

odd = [x for x in numbers if x % 2 != 0]

even_squares = [
    x ** 2
    for x in numbers
    if x % 2 == 0
]

print("Squares:", squares)
print("Even:", even)
print("Odd:", odd)
print("Even Squares:", even_squares)
```

Output:

```text
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Even: [2, 4, 6, 8, 10]

Odd: [1, 3, 5, 7, 9]

Even Squares: [4, 16, 36, 64, 100]
```

---

# 33. Quick Revision

```text
List Comprehension
        │
        ├── Basic
        │   [expression for item in iterable]
        │
        ├── Condition
        │   [expression for item in iterable if condition]
        │
        ├── if-else
        │   [A if condition else B for item in iterable]
        │
        ├── Nested
        │   [expression for x in iterable for y in iterable]
        │
        ├── Dictionary Comprehension
        │   {key: value for item in iterable}
        │
        └── Set Comprehension
            {expression for item in iterable}
```

# Most Important Syntax

### Basic

```python
[expression for item in iterable]
```

### With Condition

```python
[expression for item in iterable if condition]
```

### With if-else

```python
[value_if_true if condition else value_if_false
 for item in iterable]
```

### Nested

```python
[expression for x in iterable for y in iterable]
```

# Easy Shortcut to Remember

**List Comprehension = Expression + For Loop + Optional Condition**

```python
[expression for item in iterable if condition]
```


"""