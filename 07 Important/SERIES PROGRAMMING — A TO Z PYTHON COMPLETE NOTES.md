# SERIES PROGRAMMING — A TO Z PYTHON COMPLETE NOTES

---

# 1. What is a Series?

A **series** is a sequence of numbers arranged according to a specific pattern or rule.

### Examples

```text
1 + 2 + 3 + 4 + ... + n

2 + 4 + 6 + 8 + ... + 2n

1 + 3 + 5 + 7 + ... + (2n - 1)

1² + 2² + 3² + ... + n²

1³ + 2³ + 3³ + ... + n³
```

---

# 2. General Structure of Series Program

```text
START
   ↓
INPUT
   ↓
INITIALIZE VARIABLES
   ↓
LOOP
   ↓
CALCULATE / GENERATE TERM
   ↓
UPDATE VARIABLE
   ↓
CHECK CONDITION
   ↓
OUTPUT
   ↓
STOP
```

---

# 3. Natural Number Series

## Problem

Find:

```text
1 + 2 + 3 + ... + n
```

## Formula

```text
Sum = n(n + 1) / 2
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Set `sum = 0`

**Step 4:** Repeat from `1` to `n`

```text
sum = sum + i
```

**Step 5:** Print `sum`

**Step 6:** Stop

## Flowchart

```text
              ┌─────────────┐
              │    START    │
              └──────┬──────┘
                     ↓
              ┌─────────────┐
              │   Input n   │
              └──────┬──────┘
                     ↓
              ┌─────────────┐
              │ sum = 0     │
              └──────┬──────┘
                     ↓
                ┌──────────┐
             ┌─→│  i <= n? │
             │  └────┬─────┘
             │       │
          Yes│       │No
             ↓       ↓
      ┌────────────┐ ┌─────────────┐
      │ sum=sum+i  │ │  Print sum  │
      └─────┬──────┘ └──────┬──────┘
            ↓               ↓
      ┌────────────┐ ┌─────────────┐
      │    i += 1  │ │    STOP     │
      └─────┬──────┘ └─────────────┘
            │
            └──────────────→
```

## Python Program

```python
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)
```

### Example

```text
Enter n: 5
Sum = 15
```

---

# 4. Even Number Series

## Problem

Find:

```text
2 + 4 + 6 + 8 + ... + 2n
```

## Formula

```text
Sum = n(n + 1)
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Set `sum = 0`

**Step 4:** Repeat from `1` to `n`

```text
sum = sum + 2*i
```

**Step 5:** Print `sum`

**Step 6:** Stop

## Flowchart

```text
              ┌─────────────┐
              │    START    │
              └──────┬──────┘
                     ↓
              ┌─────────────┐
              │   Input n   │
              └──────┬──────┘
                     ↓
              ┌─────────────┐
              │ sum = 0     │
              └──────┬──────┘
                     ↓
                ┌──────────┐
             ┌─→│  i <= n? │
             │  └────┬─────┘
             │       │
          Yes│       │No
             ↓       ↓
      ┌─────────────┐ ┌─────────────┐
      │sum=sum+2*i  │ │  Print sum  │
      └──────┬──────┘ └──────┬──────┘
             ↓               ↓
      ┌─────────────┐ ┌─────────────┐
      │    i += 1   │ │    STOP     │
      └──────┬──────┘ └─────────────┘
             │
             └──────────────→
```

## Python Program

```python
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum += 2 * i

print("Sum =", sum)
```

### Dry Run

For `n = 5`:

```text
i = 1 → 2 × 1 = 2  → sum = 2
i = 2 → 2 × 2 = 4  → sum = 6
i = 3 → 2 × 3 = 6  → sum = 12
i = 4 → 2 × 4 = 8  → sum = 20
i = 5 → 2 × 5 = 10 → sum = 30
```

### Output

```text
Enter n: 5
Sum = 30
```

---

# 5. Odd Number Series

## Problem

Find:

```text
1 + 3 + 5 + 7 + ... + (2n - 1)
```

## Formula

```text
Sum = n²
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Set `sum = 0`

**Step 4:** Repeat from `1` to `n`

```text
term = 2*i - 1
sum = sum + term
```

**Step 5:** Print `sum`

**Step 6:** Stop

## Python Program

```python
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    term = 2 * i - 1
    sum += term

print("Sum =", sum)
```

### Example

```text
Enter n: 5
Sum = 25
```

Because:

```text
1 + 3 + 5 + 7 + 9 = 25
```

---

# 6. Square Series

## Problem

Find:

```text
1² + 2² + 3² + ... + n²
```

Equivalent:

```text
1 + 4 + 9 + 16 + ... + n²
```

## Formula

```text
Sum = n(n + 1)(2n + 1) / 6
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Set `sum = 0`

**Step 4:** Repeat from `1` to `n`

```text
sum = sum + i²
```

**Step 5:** Print `sum`

**Step 6:** Stop

## Python Program

```python
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum += i * i

print("Sum =", sum)
```

### Example

```text
Enter n: 5
Sum = 55
```

Because:

```text
1 + 4 + 9 + 16 + 25 = 55
```

---

# 7. Cube Series

## Problem

Find:

```text
1³ + 2³ + 3³ + ... + n³
```

Equivalent:

```text
1 + 8 + 27 + 64 + ... + n³
```

## Formula

```text
Sum = [n(n + 1) / 2]²
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Set `sum = 0`

**Step 4:** Repeat from `1` to `n`

```text
sum = sum + i³
```

**Step 5:** Print `sum`

**Step 6:** Stop

## Python Program

```python
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum += i * i * i

print("Sum =", sum)
```

### Example

```text
Enter n: 5
Sum = 225
```

Because:

```text
1 + 8 + 27 + 64 + 125 = 225
```

---

# 8. Factorial Series

## Problem

Find:

```text
1! + 2! + 3! + ... + n!
```

### Example

```text
1! + 2! + 3! + 4!

= 1 + 2 + 6 + 24

= 33
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Set `sum = 0`

**Step 4:** Set `fact = 1`

**Step 5:** Repeat from `1` to `n`

```text
fact = fact * i
sum = sum + fact
```

**Step 6:** Print `sum`

**Step 7:** Stop

## Python Program

```python
n = int(input("Enter n: "))

fact = 1
sum = 0

for i in range(1, n + 1):
    fact *= i
    sum += fact

print("Sum =", sum)
```

### Example

```text
Enter n: 4
Sum = 33
```

---

# 9. Fibonacci Series

## Problem

Print:

```text
0 1 1 2 3 5 8 13 21 ...
```

## Rule

```text
Next term = Previous two terms' sum
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Set:

```text
a = 0
b = 1
```

**Step 4:** Repeat `n` times

```text
Print a

c = a + b
a = b
b = c
```

**Step 5:** Stop

## Flowchart

```text
              ┌─────────────┐
              │    START    │
              └──────┬──────┘
                     ↓
              ┌─────────────┐
              │   Input n   │
              └──────┬──────┘
                     ↓
          ┌────────────────────┐
          │ a=0, b=1           │
          └─────────┬──────────┘
                    ↓
                ┌──────────┐
             ┌─→│  i <= n? │
             │  └────┬─────┘
             │       │
          Yes│       │No
             ↓       ↓
       ┌──────────┐  ┌─────────────┐
       │ Print a  │  │    STOP     │
       └────┬─────┘  └─────────────┘
            ↓
       ┌──────────┐
       │ c = a+b  │
       └────┬─────┘
            ↓
       ┌──────────┐
       │   a = b  │
       └────┬─────┘
            ↓
       ┌──────────┐
       │   b = c  │
       └────┬─────┘
            ↓
       ┌──────────┐
       │  i += 1  │
       └────┬─────┘
            │
            └──────────────→ i <= n?
```

## Python Program

```python
n = int(input("Enter n: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c
```

### Example

```text
Enter n: 8
0 1 1 2 3 5 8 13
```

---

# 10. Arithmetic Series

## Problem

Find:

```text
a + (a+d) + (a+2d) + ... + n terms
```

### Example

```text
2 + 5 + 8 + 11 + 14
```

Here:

```text
a = 2
d = 3
n = 5
```

## Formula

```text
Sum = n/2 [2a + (n - 1)d]
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `a`, `d`, `n`

**Step 3:** Set `sum = 0`

**Step 4:** Set `term = a`

**Step 5:** Repeat `n` times

```text
sum = sum + term
term = term + d
```

**Step 6:** Print `sum`

**Step 7:** Stop

## Python Program

```python
a = int(input("Enter first term: "))
d = int(input("Enter common difference: "))
n = int(input("Enter number of terms: "))

sum = 0
term = a

for i in range(n):
    sum += term
    term += d

print("Sum =", sum)
```

### Example

```text
Enter first term: 2
Enter common difference: 3
Enter number of terms: 5

Sum = 40
```

Because:

```text
2 + 5 + 8 + 11 + 14 = 40
```

---

# 11. Geometric Series

## Problem

Find:

```text
a + ar + ar² + ar³ + ... + n terms
```

### Example

```text
2 + 4 + 8 + 16 + 32
```

Here:

```text
a = 2
r = 2
n = 5
```

## Formula

For `r != 1`:

```text
Sum = a(rⁿ - 1) / (r - 1)
```

For `r = 1`:

```text
Sum = na
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `a`, `r`, `n`

**Step 3:** Set `sum = 0`

**Step 4:** Set `term = a`

**Step 5:** Repeat `n` times

```text
sum = sum + term
term = term * r
```

**Step 6:** Print `sum`

**Step 7:** Stop

## Python Program

```python
a = int(input("Enter first term: "))
r = int(input("Enter common ratio: "))
n = int(input("Enter number of terms: "))

sum = 0
term = a

for i in range(n):
    sum += term
    term *= r

print("Sum =", sum)
```

### Example

```text
Enter first term: 2
Enter common ratio: 2
Enter number of terms: 5

Sum = 62
```

Because:

```text
2 + 4 + 8 + 16 + 32 = 62
```

---

# 12. Harmonic Series

## Problem

Find:

```text
1 + 1/2 + 1/3 + ... + 1/n
```

## Important

Python 3 automatically performs floating-point division with `/`.

So:

```python
1 / i
```

is correct.

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Set `sum = 0.0`

**Step 4:** Repeat from `1` to `n`

```text
sum = sum + 1/i
```

**Step 5:** Print `sum`

**Step 6:** Stop

## Python Program

```python
n = int(input("Enter n: "))

sum = 0.0

for i in range(1, n + 1):
    sum += 1 / i

print("Sum =", round(sum, 4))
```

### Example

```text
Enter n: 5
Sum = 2.2833
```

---

# 13. Alternating Series

## Problem

Find:

```text
1 - 2 + 3 - 4 + 5 - 6 + ... ± n
```

## Logic

```text
Odd position  → Add
Even position → Subtract
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Set `sum = 0`

**Step 4:** Repeat from `1` to `n`

```text
If i % 2 == 0:
    sum = sum - i
Else:
    sum = sum + i
```

**Step 5:** Print `sum`

**Step 6:** Stop

## Python Program

```python
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i

print("Sum =", sum)
```

### Example

```text
Enter n: 6
Sum = -3
```

Because:

```text
1 - 2 + 3 - 4 + 5 - 6 = -3
```

---

# 14. Alternating Odd Series

## Problem

Find:

```text
1 - 3 + 5 - 7 + 9 - ...
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Set:

```text
sum = 0
term = 1
```

**Step 4:** Repeat `n` times

```text
If position is odd:
    sum = sum + term
Else:
    sum = sum - term

term = term + 2
```

**Step 5:** Print `sum`

**Step 6:** Stop

## Python Program

```python
n = int(input("Enter n: "))

sum = 0
term = 1

for i in range(1, n + 1):
    if i % 2 == 1:
        sum += term
    else:
        sum -= term

    term += 2

print("Sum =", sum)
```

### Example

```text
Enter n: 5
Sum = 5
```

Because:

```text
1 - 3 + 5 - 7 + 9 = 5
```

---

# 15. Alternating Even Series

## Problem

Find:

```text
2 - 4 + 6 - 8 + 10 - ...
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Set:

```text
sum = 0
term = 2
```

**Step 4:** Repeat `n` times

```text
If position is odd:
    sum = sum + term
Else:
    sum = sum - term

term = term + 2
```

**Step 5:** Print `sum`

**Step 6:** Stop

## Python Program

```python
n = int(input("Enter n: "))

sum = 0
term = 2

for i in range(1, n + 1):
    if i % 2 == 1:
        sum += term
    else:
        sum -= term

    term += 2

print("Sum =", sum)
```

### Example

```text
Enter n: 5
Sum = 6
```

Because:

```text
2 - 4 + 6 - 8 + 10 = 6
```

---

# 16. Series with Square Pattern

## Problem

Print:

```text
1, 4, 9, 16, 25, ... n²
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Repeat from `1` to `n`

```text
Print i * i
```

**Step 4:** Stop

## Python Program

```python
n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i * i, end=" ")
```

### Output

For `n = 5`:

```text
1 4 9 16 25
```

---

# 17. Series with Cube Pattern

## Problem

Print:

```text
1, 8, 27, 64, ... n³
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n`

**Step 3:** Repeat from `1` to `n`

```text
Print i * i * i
```

**Step 4:** Stop

## Python Program

```python
n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i * i * i, end=" ")
```

### Output

For `n = 5`:

```text
1 8 27 64 125
```

---

# 18. Power Series

## Problem

Find:

```text
1^p + 2^p + 3^p + ... + n^p
```

## Example

If:

```text
n = 5
p = 2
```

Then:

```text
1² + 2² + 3² + 4² + 5²
```

## Algorithm

**Step 1:** Start

**Step 2:** Input `n` and `p`

**Step 3:** Set `sum = 0`

**Step 4:** Repeat from `1` to `n`

```text
sum = sum + i^p
```

**Step 5:** Print `sum`

**Step 6:** Stop

## Python Program

```python
n = int(input("Enter n: "))
p = int(input("Enter power p: "))

sum = 0

for i in range(1, n + 1):
    sum += i ** p

print("Sum =", sum)
```

### Example

```text
Enter n: 5
Enter power p: 2
Sum = 55
```

---

# 19. Important Series Formulas

## Natural Number Series

```text
1 + 2 + 3 + ... + n

Sum = n(n + 1) / 2
```

## Even Number Series

```text
2 + 4 + 6 + ... + 2n

Sum = n(n + 1)
```

## Odd Number Series

```text
1 + 3 + 5 + ... + (2n - 1)

Sum = n²
```

## Square Series

```text
1² + 2² + 3² + ... + n²

Sum = n(n + 1)(2n + 1) / 6
```

## Cube Series

```text
1³ + 2³ + 3³ + ... + n³

Sum = [n(n + 1) / 2]²
```

## Arithmetic Series

```text
Sum = n/2 [2a + (n - 1)d]
```

## Geometric Series

For `r != 1`:

```text
Sum = a(rⁿ - 1) / (r - 1)
```

For `r = 1`:

```text
Sum = na
```

---

# 20. How to Identify a Series

## Pattern 1: Difference

```text
2, 5, 8, 11, 14
```

Difference:

```text
+3, +3, +3, +3
```

This is an **Arithmetic Series**.

---

## Pattern 2: Multiplication

```text
2, 4, 8, 16, 32
```

Ratio:

```text
×2, ×2, ×2, ×2
```

This is a **Geometric Series**.

---

## Pattern 3: Square

```text
1, 4, 9, 16, 25
```

These are:

```text
1², 2², 3², 4², 5²
```

This is a **Square Series**.

---

## Pattern 4: Cube

```text
1, 8, 27, 64
```

These are:

```text
1³, 2³, 3³, 4³
```

This is a **Cube Series**.

---

## Pattern 5: Factorial

```text
1, 2, 6, 24, 120
```

These are:

```text
1!, 2!, 3!, 4!, 5!
```

This is a **Factorial Series**.

---

## Pattern 6: Alternating Sign

```text
1, -2, 3, -4, 5, -6
```

The sign changes every term.

This is an **Alternating Series**.

---

# 21. Common Flowchart Structure

For most series problems:

```text
START
   ↓
INPUT
   ↓
INITIALIZATION
   ↓
LOOP CONDITION
   ↓
CALCULATE / GENERATE TERM
   ↓
UPDATE
   ↓
LOOP CONDITION
   ↓
OUTPUT
   ↓
STOP
```

---

# 22. Important Python Variables

| Variable  | Meaning             |
| --------- | ------------------- |
| `n`       | Number of terms     |
| `i`       | Loop counter        |
| `sum`     | Stores total sum    |
| `term`    | Stores current term |
| `fact`    | Stores factorial    |
| `a`       | First term          |
| `d`       | Common difference   |
| `r`       | Common ratio        |
| `a, b, c` | Fibonacci variables |

---

# 23. Important Python Operators

## Addition

```python
sum = sum + term
```

Short form:

```python
sum += term
```

## Subtraction

```python
sum = sum - term
```

Short form:

```python
sum -= term
```

## Multiplication

```python
term = term * r
```

Short form:

```python
term *= r
```

## Increment

Python does not have `i++`.

Use:

```python
i += 1
```

## Increment by 2

```python
i += 2
```

## Remainder

```python
i % 2
```

Used to check even/odd.

## Power

In Python:

```python
i ** 2
```

means:

```text
i²
```

And:

```python
i ** 3
```

means:

```text
i³
```

---

# 24. Python range() — Very Important

Python series programs commonly use:

```python
range(1, n + 1)
```

Why `n + 1`?

Because Python's `range()` excludes the ending value.

Example:

```python
range(1, 6)
```

produces:

```text
1 2 3 4 5
```

Therefore, for `1` to `n`:

```python
range(1, n + 1)
```

---

# 25. Common Mistakes in Python

## Mistake 1: Wrong range

Wrong:

```python
for i in range(1, n):
```

This stops at `n - 1`.

Correct:

```python
for i in range(1, n + 1):
```

---

## Mistake 2: Forgetting Initialization

Wrong:

```python
sum = 0
```

should be written before the loop.

Example:

```python
sum = 0

for i in range(1, n + 1):
    sum += i
```

---

## Mistake 3: Wrong Factorial Initialization

Wrong:

```python
fact = 0
```

Correct:

```python
fact = 1
```

---

## Mistake 4: Using `i++`

Wrong in Python:

```python
i++
```

Correct:

```python
i += 1
```

---

## Mistake 5: Using `^` for Power

Wrong:

```python
i ^ 2
```

In Python, `^` means **bitwise XOR**.

Correct:

```python
i ** 2
```

---

## Mistake 6: Wrong Fibonacci Initialization

Correct:

```python
a = 0
b = 1
```

---

# 26. Time Complexity

Most simple series programs use one loop.

Therefore:

```text
Time Complexity = O(n)
```

Examples:

```text
Natural Series     → O(n)
Even Series        → O(n)
Odd Series         → O(n)
Square Series      → O(n)
Cube Series        → O(n)
Factorial Series   → O(n)
Fibonacci Series   → O(n)
Arithmetic Series  → O(n)
Geometric Series   → O(n)
Harmonic Series    → O(n)
```

---

# 27. Quick Revision Sheet

### Natural Series

```text
1 + 2 + 3 + ... + n
```

### Even Series

```text
2 + 4 + 6 + ... + 2n
```

### Odd Series

```text
1 + 3 + 5 + ... + (2n - 1)
```

### Square Series

```text
1² + 2² + 3² + ... + n²
```

### Cube Series

```text
1³ + 2³ + 3³ + ... + n³
```

### Factorial Series

```text
1! + 2! + 3! + ... + n!
```

### Fibonacci

```text
0, 1, 1, 2, 3, 5, 8, ...
```

### Arithmetic

```text
a, a+d, a+2d, a+3d, ...
```

### Geometric

```text
a, ar, ar², ar³, ...
```

### Harmonic

```text
1, 1/2, 1/3, 1/4, ...
```

### Alternating

```text
1, -2, 3, -4, 5, -6, ...
```

---

# 28. Final Exam Strategy

When you get a Series problem in an exam:

**Step 1:** Identify the pattern.

**Step 2:** Determine the first term.

**Step 3:** Determine how the next term is generated.

**Step 4:** Select the required variables.

**Step 5:** Initialize `sum`, `term`, or `fact`.

**Step 6:** Write the `for` loop.

**Step 7:** Calculate or generate the term.

**Step 8:** Update the variable.

**Step 9:** Print the result.

**Step 10:** Check the output with a small example.

---

# 29. Master Pattern

Almost every Series program can be understood using this structure:

```text
START
   ↓
INPUT
   ↓
INITIALIZE
   ↓
LOOP
   ↓
GENERATE TERM
   ↓
ADD / SUBTRACT TERM
   ↓
UPDATE
   ↓
CHECK CONDITION
   ↓
OUTPUT
   ↓
STOP
```

---

# END OF SERIES PROGRAMMING — PYTHON NOTES
