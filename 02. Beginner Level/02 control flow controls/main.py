"""
# Python Control Flow — Interview Questions & Answers

## 01. break, continue, pass

### Q1. What is `break`?

**Answer:**
`break` statement is used to immediately terminate a loop.

Example:

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

Output:

```text
1
2
```

### Q2. What is `continue`?

**Answer:**
`continue` skips the current iteration and moves to the next iteration of the loop.

Example:

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```text
1
2
4
5
```

### Q3. What is `pass`?

**Answer:**
`pass` is a null statement. It does nothing when executed. It is commonly used as a placeholder.

Example:

```python
for i in range(5):
    pass
```

### Q4. Difference between `break`, `continue`, and `pass`.

| Statement  | Purpose                             |
| ---------- | ----------------------------------- |
| `break`    | Terminates the loop                 |
| `continue` | Skips current iteration             |
| `pass`     | Does nothing; acts as a placeholder |

---

# 02. if, elif, else

Conditional statements are used to execute different blocks of code based on conditions.

### Q1. What is an `if` statement?

**Answer:**
The `if` statement executes a block of code when a specified condition is true.

```python
age = 20

if age >= 18:
    print("Adult")
```

### Q2. What is `else`?

**Answer:**
`else` executes when the `if` condition is false.

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Q3. What is `elif`?

**Answer:**
`elif` means "else if". It is used to check multiple conditions.

```python
marks = 75

if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("A-")
else:
    print("Below A-")
```

### Q4. Can we use multiple `elif` statements?

**Answer:**
Yes, we can use multiple `elif` statements.

### Q5. Can an `if` statement exist without `else`?

**Answer:**
Yes.

```python
age = 20

if age >= 18:
    print("Adult")
```

### Q6. Can we use `else` without `if`?

**Answer:**
No. `else` must be associated with an `if` statement.

---

# 03. Loops

A loop is used to execute a block of code repeatedly.

Python mainly has:

1. `for` loop
2. `while` loop

---

## for Loop

### Q1. What is a `for` loop?

**Answer:**
A `for` loop is used to iterate over a sequence or iterable.

Example:

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

### Q2. What is `range()`?

**Answer:**
`range()` generates a sequence of numbers that can be used commonly with `for` loops.

```python
range(5)
```

Produces values:

```text
0 1 2 3 4
```

### Q3. What does `range(start, stop, step)` mean?

```python
range(1, 10, 2)
```

* `start` = 1
* `stop` = 10
* `step` = 2

Output:

```text
1 3 5 7 9
```

The `stop` value is excluded.

---

## while Loop

### Q4. What is a `while` loop?

**Answer:**
A `while` loop repeatedly executes a block of code as long as its condition is true.

Example:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output:

```text
1
2
3
4
5
```

### Q5. Difference between `for` and `while` loop?

**Answer:**

`for` loop is generally used when iterating over a sequence or when the number of iterations is known.

`while` loop is generally used when repetition depends on a condition.

---

# 04. Problems / Problem Solving

Python interviews often include small programming problems.

## Problem 1: Check Even or Odd

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Interview Concept

The `%` operator returns the remainder.

If:

```text
number % 2 == 0
```

then the number is even.

---

## Problem 2: Find the Largest of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a)
else:
    print(b)
```

---

## Problem 3: Find the Largest of Three Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
```

---

## Problem 4: Check Positive, Negative, or Zero

```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

---

## Problem 5: Print 1 to 10

```python
for i in range(1, 11):
    print(i)
```

---

## Problem 6: Print Even Numbers from 1 to 20

```python
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
```

---

## Problem 7: Calculate Sum from 1 to N

```python
n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total += i

print(total)
```

---

## Problem 8: Find Factorial

```python
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)
```

---

## Problem 9: Check Prime Number

```python
n = int(input("Enter a number: "))

if n < 2:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
```

---

# 05. Religion

> **Note:** `Religion` is not a Python programming concept. If this was meant to be **"Recursion"**, **"Relation"**, or another Python topic, replace this section with the intended topic.

---

# 06. Switch Case

Python does not traditionally have the C/C++/Java-style `switch` statement.

Modern Python provides **`match-case`** for structural pattern matching.

## Q1. What is `match-case`?

**Answer:**
`match-case` is Python's pattern-matching construct, introduced in Python 3.10. It can be used for cases where multiple possible patterns or values need to be handled.

Example:

```python
day = 2

match day:
    case 1:
        print("Saturday")
    case 2:
        print("Sunday")
    case 3:
        print("Monday")
    case _:
        print("Invalid day")
```

Output:

```text
Sunday
```

### Q2. What is `case _`?

**Answer:**
`case _` acts as a wildcard pattern and can handle values that did not match the previous cases.

### Q3. Does Python have a traditional `switch` statement?

**Answer:**
No. Python does not have the traditional `switch` statement found in languages such as C/C++ or Java. Python 3.10+ provides `match-case`.

---

# 🔥 Important Interview Questions

## Control Flow

1. What is `break`?
2. What is `continue`?
3. What is `pass`?
4. Difference between `break`, `continue`, and `pass`.
5. What is an `if` statement?
6. What is `elif`?
7. What is `else`?
8. Can we use multiple `elif` statements?
9. Can we use `if` without `else`?
10. What is a nested `if`?

## Loops

11. What is a loop?
12. What are the types of loops in Python?
13. What is a `for` loop?
14. What is a `while` loop?
15. Difference between `for` and `while`.
16. What is `range()`?
17. What does `range(5)` produce?
18. What is an infinite loop?
19. How can you stop a loop?
20. How does `break` work inside a loop?
21. How does `continue` work inside a loop?
22. Can we use `else` with a loop?

## Problem Solving

23. Write a program to check even/odd.
24. Find the largest of two numbers.
25. Find the largest of three numbers.
26. Check positive/negative/zero.
27. Print numbers from 1 to N.
28. Print even numbers.
29. Print odd numbers.
30. Calculate the sum from 1 to N.
31. Find factorial.
32. Check prime number.
33. Print multiplication table.
34. Reverse a number.
35. Check palindrome number.
36. Find Fibonacci series.

## Switch Case

37. Does Python have a traditional switch statement?
38. What is `match-case`?
39. In which Python version was `match-case` introduced?
40. What is `case _`?
41. Difference between `if-elif-else` and `match-case`.

---

# ⭐ Quick Revision

```text
break
    → Stops the loop

continue
    → Skips current iteration

pass
    → Does nothing

if
    → Checks a condition

elif
    → Checks another condition

else
    → Executes when previous conditions are false

for
    → Iterates over an iterable

while
    → Runs while condition is True

range()
    → Generates a sequence of numbers

match-case
    → Pattern matching in Python 3.10+

case _
    → Wildcard/default-like case
```

"""
