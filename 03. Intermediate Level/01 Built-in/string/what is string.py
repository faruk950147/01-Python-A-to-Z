'''
# Python String

## 1. What is a String?

A **string** is an **ordered, indexed, immutable sequence of characters** used to represent text in Python.

Example:

```python
name = "Python"
```

A string can contain:

```text
Letters
Numbers
Symbols
Spaces
Unicode characters
```

Example:

```python
text = "Python 3.14!"
```

---

# 2. Creating a String

Strings can be created using:

### Double Quotes

```python
text = "Hello"
```

### Single Quotes

```python
text = 'Hello'
```

Both are equivalent:

```python
name1 = "Faruk"
name2 = 'Faruk'
```

---

# 3. Triple Quotes

Triple quotes are commonly used for **multiline strings** and docstrings.

```python
text = """
Hello
Welcome to Python
Learning String
"""
```

You can also use:

```python
text = '''
Hello
Welcome to Python
'''
```

---

# 4. String is a Sequence

A string contains a sequence of characters.

```python
text = "Python"
```

Characters:

```text
P   y   t   h   o   n
```

Each character has a position.

---

# 5. String is Ordered

Strings preserve the order of their characters.

```python
text = "Python"

print(text)
```

Output:

```text
Python
```

The order is:

```text
P → y → t → h → o → n
```

---

# 6. String Indexing

String indexing starts from `0`.

```python
text = "Python"

print(text[0])
print(text[1])
print(text[2])
```

Output:

```text
P
y
t
```

Index table:

```text
Character:  P   y   t   h   o   n
Positive:   0   1   2   3   4   5
Negative:  -6  -5  -4  -3  -2  -1
```

---

# 7. Positive Indexing

```python
text = "Python"

print(text[0])   # P
print(text[3])   # h
print(text[5])   # n
```

---

# 8. Negative Indexing

Negative indexing starts from the end.

```python
text = "Python"

print(text[-1])  # n
print(text[-2])  # o
print(text[-3])  # h
```

Remember:

```text
-1 → last character
-2 → second-last character
```

---

# 9. String is Immutable

Strings are **immutable**.

That means you cannot change an individual character after the string is created.

```python
text = "Python"

# text[0] = "J"
```

This raises:

```text
TypeError
```

---

# 10. How to Modify a String

Although strings are immutable, you can create a **new string**.

```python
text = "Python"

text = "J" + text[1:]

print(text)
```

Output:

```text
Jython
```

The original string was not modified.

A new string was created.

---

# 11. String Slicing

Strings support slicing.

Syntax:

```python
string[start:stop:step]
```

Example:

```python
text = "Python"

print(text[0:3])
```

Output:

```text
Pyt
```

Important:

```text
start → included
stop  → excluded
```

---

# 12. Basic Slicing

```python
text = "Python"

print(text[0:2])
```

Output:

```text
Py
```

```python
print(text[2:5])
```

Output:

```text
tho
```

---

# 13. Omitting Start

```python
text = "Python"

print(text[:3])
```

Output:

```text
Pyt
```

This means:

```text
start = beginning
```

---

# 14. Omitting Stop

```python
text = "Python"

print(text[3:])
```

Output:

```text
hon
```

This means:

```text
stop = end
```

---

# 15. Copying a String with Slicing

```python
text = "Python"

copy = text[:]

print(copy)
```

Output:

```text
Python
```

---

# 16. Slicing with Step

```python
text = "Python"

print(text[0:6:2])
```

Output:

```text
Pto
```

Characters selected:

```text
P → index 0
t → index 2
o → index 4
```

---

# 17. Reverse a String

One of the most important Python string techniques:

```python
text = "Python"

reverse = text[::-1]

print(reverse)
```

Output:

```text
nohtyP
```

---

# 18. String Length

Use `len()`:

```python
text = "Python"

print(len(text))
```

Output:

```text
6
```

Spaces are also counted.

```python
text = "Hello World"

print(len(text))
```

Output:

```text
11
```

---

# 19. Iterating Through a String

A string is iterable.

```python
text = "Python"

for char in text:
    print(char)
```

Output:

```text
P
y
t
h
o
n
```

---

# 20. Membership Testing

Use `in` and `not in`.

```python
text = "Python"

print("P" in text)
```

Output:

```text
True
```

Example:

```python
print("Java" in text)
```

Output:

```text
False
```

Using `not in`:

```python
print("Java" not in text)
```

Output:

```text
True
```

---

# 21. String Concatenation

Concatenation means joining strings.

Use `+`.

```python
first = "Hello"
second = "World"

result = first + " " + second

print(result)
```

Output:

```text
Hello World
```

---

# 22. String Repetition

Use `*`.

```python
text = "Python "

print(text * 3)
```

Output:

```text
Python Python Python
```

Another example:

```python
print("-" * 20)
```

Output:

```text
--------------------
```

---

# 23. Comparing Strings

Strings can be compared.

```python
a = "apple"
b = "banana"

print(a == b)
print(a != b)
```

Output:

```text
False
True
```

Other comparison operators:

```python
==
!=
<
>
<=
>=
```

String comparison is based on lexicographical ordering.

---

# 24. Lexicographical Comparison

```python
print("apple" < "banana")
```

Output:

```text
True
```

Python compares characters according to their Unicode values.

Example:

```python
print("A" < "a")
```

The result is:

```text
True
```

because uppercase and lowercase letters have different Unicode code points.

---

# 25. String Methods

Python provides many built-in string methods.

Important methods include:

```text
lower()
upper()
capitalize()
title()
swapcase()
casefold()

strip()
lstrip()
rstrip()

replace()
split()
rsplit()
join()

find()
rfind()
index()
rindex()

count()
startswith()
endswith()

isalpha()
isdigit()
isalnum()
isspace()
islower()
isupper()
istitle()
```

---

# 26. `lower()`

Converts characters to lowercase.

```python
text = "PYTHON"

print(text.lower())
```

Output:

```text
python
```

---

# 27. `upper()`

Converts characters to uppercase.

```python
text = "python"

print(text.upper())
```

Output:

```text
PYTHON
```

---

# 28. `capitalize()`

Capitalizes the first character and lowercases the remaining characters.

```python
text = "python programming"

print(text.capitalize())
```

Output:

```text
Python programming
```

---

# 29. `title()`

Capitalizes the first letter of each word.

```python
text = "python programming language"

print(text.title())
```

Output:

```text
Python Programming Language
```

---

# 30. `swapcase()`

Swaps uppercase and lowercase characters.

```python
text = "Python PROGRAMMING"

print(text.swapcase())
```

Output:

```text
pYTHON programming
```

---

# 31. `casefold()`

Used for case-insensitive comparisons and is generally more aggressive than `lower()` for Unicode text.

```python
a = "Python"
b = "PYTHON"

print(a.casefold() == b.casefold())
```

Output:

```text
True
```

---

# 32. Removing Spaces

## `strip()`

Removes whitespace from both ends.

```python
text = "   Python   "

print(text.strip())
```

Output:

```text
Python
```

---

# 33. `lstrip()`

Removes whitespace from the left side.

```python
text = "   Python"

print(text.lstrip())
```

Output:

```text
Python
```

---

# 34. `rstrip()`

Removes whitespace from the right side.

```python
text = "Python   "

print(text.rstrip())
```

Output:

```text
Python
```

---

# 35. `replace()`

Replaces part of a string.

```python
text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)
```

Output:

```text
I like Python
```

Important:

`replace()` does not modify the original string because strings are immutable.

---

# 36. `split()`

Splits a string into a list.

```python
text = "Python Java C++"

languages = text.split()

print(languages)
```

Output:

```text
['Python', 'Java', 'C++']
```

---

# 37. Split Using a Separator

```python
text = "apple,banana,mango"

fruits = text.split(",")

print(fruits)
```

Output:

```text
['apple', 'banana', 'mango']
```

---

# 38. `join()`

`join()` combines elements into a string.

```python
words = ["Python", "is", "easy"]

text = " ".join(words)

print(text)
```

Output:

```text
Python is easy
```

Another example:

```python
words = ["Python", "Java", "C"]

result = ", ".join(words)

print(result)
```

Output:

```text
Python, Java, C
```

---

# 39. `split()` vs `join()`

Remember:

```text
split() → String → List

join()  → Iterable of strings → String
```

Example:

```python
text = "Python Java C"

words = text.split()

result = "-".join(words)

print(result)
```

Output:

```text
Python-Java-C
```

---

# 40. `find()`

Finds the first occurrence of a substring.

```python
text = "Python Programming"

print(text.find("Python"))
```

Output:

```text
0
```

If not found:

```python
print(text.find("Java"))
```

Output:

```text
-1
```

---

# 41. `rfind()`

Searches from the right and returns the position of the last occurrence.

```python
text = "banana"

print(text.rfind("a"))
```

Output:

```text
5
```

---

# 42. `index()`

Similar to `find()`.

```python
text = "Python"

print(text.index("t"))
```

Output:

```text
2
```

But if the substring does not exist:

```python
text.index("z")
```

raises:

```text
ValueError
```

### Difference

```text
find()  → returns -1 if not found
index() → raises ValueError if not found
```

---

# 43. `count()`

Counts occurrences.

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

Example:

```python
print(text.count("na"))
```

Output:

```text
2
```

---

# 44. `startswith()`

Checks whether a string starts with a particular substring.

```python
text = "Python Programming"

print(text.startswith("Python"))
```

Output:

```text
True
```

---

# 45. `endswith()`

Checks whether a string ends with a particular substring.

```python
text = "Python.py"

print(text.endswith(".py"))
```

Output:

```text
True
```

Useful for checking file extensions.

---

# 46. Character Checking Methods

## `isalpha()`

Checks whether all characters are alphabetic.

```python
print("Python".isalpha())
```

Output:

```text
True
```

But:

```python
print("Python3".isalpha())
```

Output:

```text
False
```

---

# 47. `isdigit()`

Checks whether all characters are digits.

```python
print("12345".isdigit())
```

Output:

```text
True
```

```python
print("123a".isdigit())
```

Output:

```text
False
```

---

# 48. `isalnum()`

Checks whether all characters are alphanumeric.

```python
print("Python123".isalnum())
```

Output:

```text
True
```

Space and special characters make it false:

```python
print("Python 123".isalnum())
```

Output:

```text
False
```

---

# 49. `isspace()`

Checks whether all characters are whitespace.

```python
print("   ".isspace())
```

Output:

```text
True
```

---

# 50. `islower()`

```python
print("python".islower())
```

Output:

```text
True
```

---

# 51. `isupper()`

```python
print("PYTHON".isupper())
```

Output:

```text
True
```

---

# 52. `istitle()`

```python
text = "Python Programming"

print(text.istitle())
```

Output:

```text
True
```

---

# 53. String Formatting

Python provides several ways to format strings.

### 1. `%` formatting

```python
name = "Faruk"
age = 22

print("My name is %s and I am %d years old." % (name, age))
```

---

### 2. `format()`

```python
name = "Faruk"
age = 22

print("My name is {} and I am {} years old.".format(name, age))
```

---

### 3. f-string

Modern Python code commonly uses f-strings.

```python
name = "Faruk"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

---

# 54. f-string Expressions

You can put expressions inside `{}`.

```python
a = 10
b = 20

print(f"Sum = {a + b}")
```

Output:

```text
Sum = 30
```

---

# 55. Formatting Numbers

```python
price = 1234.5678

print(f"{price:.2f}")
```

Output:

```text
1234.57
```

---

# 56. Escape Characters

Escape sequences allow special characters inside strings.

### New Line

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

### Tab

```python
print("Hello\tWorld")
```

### Backslash

```python
print("C:\\Users\\Faruk")
```

### Double Quote

```python
print("He said \"Hello\"")
```

### Single Quote

```python
print('It\'s Python')
```

---

# 57. Common Escape Sequences

| Escape | Meaning         |
| ------ | --------------- |
| `\n`   | New line        |
| `\t`   | Tab             |
| `\\`   | Backslash       |
| `\'`   | Single quote    |
| `\"`   | Double quote    |
| `\r`   | Carriage return |
| `\b`   | Backspace       |
| `\f`   | Form feed       |

---

# 58. Raw String

Prefix a string with `r` to create a raw string.

```python
path = r"C:\Users\Faruk\Documents"
```

Raw strings are useful for paths and regular expressions.

Example:

```python
pattern = r"\d+\.\d+"
```

---

# 59. Unicode Strings

Python 3 strings are Unicode text.

```python
text = "বাংলাদেশ"

print(text)
```

You can also use emoji:

```python
text = "Python 🐍"

print(text)
```

---

# 60. `ord()`

Returns the Unicode code point of a character.

```python
print(ord("A"))
```

Output:

```text
65
```

Example:

```python
print(ord("a"))
```

Output:

```text
97
```

---

# 61. `chr()`

Converts a Unicode code point into a character.

```python
print(chr(65))
```

Output:

```text
A
```

Example:

```python
print(chr(97))
```

Output:

```text
a
```

---

# 62. `ord()` and `chr()` Relationship

```python
char = "A"

number = ord(char)

print(number)
print(chr(number))
```

Output:

```text
65
A
```

---

# 63. String Formatting with `repr()`

`repr()` returns a representation of an object.

```python
text = "Hello\nWorld"

print(text)
print(repr(text))
```

The second output shows the escape sequence representation.

---

# 64. Multiline String

```python
text = """
Python is easy.
Python is powerful.
Python is popular.
"""

print(text)
```

Triple-quoted strings can span multiple lines.

---

# 65. Empty String

An empty string contains zero characters.

```python
text = ""

print(len(text))
```

Output:

```text
0
```

Check:

```python
if text:
    print("Not empty")
else:
    print("Empty")
```

Output:

```text
Empty
```

---

# 66. String Truthiness

An empty string is considered `False`.

```python
text = ""

print(bool(text))
```

Output:

```text
False
```

A non-empty string is considered `True`.

```python
text = "Python"

print(bool(text))
```

Output:

```text
True
```

---

# 67. String Concatenation with Numbers

This is invalid:

```python
age = 22

# print("Age: " + age)
```

It raises:

```text
TypeError
```

Convert the number:

```python
print("Age: " + str(age))
```

Or use an f-string:

```python
print(f"Age: {age}")
```

---

# 68. `str()`

Converts an object to a string.

```python
age = 22

text = str(age)

print(text)
print(type(text))
```

Output:

```text
22
<class 'str'>
```

---

# 69. String and List Conversion

Convert string to list:

```python
text = "Python"

characters = list(text)

print(characters)
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

Convert list of characters back to string:

```python
characters = ['P', 'y', 't', 'h', 'o', 'n']

text = "".join(characters)

print(text)
```

Output:

```text
Python
```

---

# 70. String Unpacking

A string can be unpacked into variables.

```python
text = "ABC"

a, b, c = text

print(a)
print(b)
print(c)
```

Output:

```text
A
B
C
```

The number of variables must match the number of characters unless extended unpacking is used.

---

# 71. Extended Unpacking

```python
text = "Python"

first, *middle, last = text

print(first)
print(middle)
print(last)
```

Output:

```text
P
['y', 't', 'h', 'o']
n
```

---

# 72. String Methods Do Not Modify the Original String

Because strings are immutable:

```python
text = "python"

text.upper()

print(text)
```

Output:

```text
python
```

To keep the result:

```python
text = text.upper()

print(text)
```

Output:

```text
PYTHON
```

---

# 73. `splitlines()`

Splits a multiline string into a list of lines.

```python
text = """Python
Java
C"""

lines = text.splitlines()

print(lines)
```

Output:

```text
['Python', 'Java', 'C']
```

---

# 74. `partition()`

Splits a string into three parts:

```text
before separator
separator
after separator
```

Example:

```python
text = "name=Faruk"

result = text.partition("=")

print(result)
```

Output:

```text
('name', '=', 'Faruk')
```

---

# 75. `removeprefix()`

Removes a prefix if present.

```python
text = "Python Programming"

print(text.removeprefix("Python "))
```

Output:

```text
Programming
```

---

# 76. `removesuffix()`

Removes a suffix if present.

```python
filename = "program.py"

print(filename.removesuffix(".py"))
```

Output:

```text
program
```

---

# 77. String Translation

Python provides `translate()` and `maketrans()` for character-level translation.

```python
table = str.maketrans("abc", "123")

text = "abc"

print(text.translate(table))
```

Output:

```text
123
```

This can be useful for character substitutions.

---

# 78. Important String Methods Table

| Method           | Purpose                                             |
| ---------------- | --------------------------------------------------- |
| `lower()`        | Converts to lowercase                               |
| `upper()`        | Converts to uppercase                               |
| `capitalize()`   | Capitalizes first character                         |
| `title()`        | Capitalizes each word                               |
| `swapcase()`     | Swaps upper/lower case                              |
| `casefold()`     | Strong case normalization                           |
| `strip()`        | Removes surrounding whitespace                      |
| `lstrip()`       | Removes left whitespace                             |
| `rstrip()`       | Removes right whitespace                            |
| `replace()`      | Replaces substring                                  |
| `split()`        | Converts string into list                           |
| `join()`         | Combines strings                                    |
| `find()`         | Finds substring, returns `-1` if absent             |
| `rfind()`        | Finds from the right                                |
| `index()`        | Finds substring, raises `ValueError` if absent      |
| `rindex()`       | Finds from the right, raises `ValueError` if absent |
| `count()`        | Counts occurrences                                  |
| `startswith()`   | Checks prefix                                       |
| `endswith()`     | Checks suffix                                       |
| `isalpha()`      | Checks alphabetic characters                        |
| `isdigit()`      | Checks digits                                       |
| `isalnum()`      | Checks alphanumeric characters                      |
| `isspace()`      | Checks whitespace                                   |
| `islower()`      | Checks lowercase                                    |
| `isupper()`      | Checks uppercase                                    |
| `istitle()`      | Checks title case                                   |
| `splitlines()`   | Splits lines                                        |
| `partition()`    | Splits into 3 parts                                 |
| `removeprefix()` | Removes prefix                                      |
| `removesuffix()` | Removes suffix                                      |

---

# 79. String Operators

| Operator | Meaning               |
| -------- | --------------------- |
| `+`      | Concatenation         |
| `*`      | Repetition            |
| `[]`     | Indexing              |
| `[:]`    | Slicing               |
| `in`     | Membership            |
| `not in` | Negative membership   |
| `==`     | Equality              |
| `!=`     | Not equal             |
| `<`      | Less than             |
| `>`      | Greater than          |
| `<=`     | Less than or equal    |
| `>=`     | Greater than or equal |

---

# 80. String vs List

| Feature    | String          | List               |
| ---------- | --------------- | ------------------ |
| Ordered    | Yes             | Yes                |
| Indexed    | Yes             | Yes                |
| Mutable    | No              | Yes                |
| Iterable   | Yes             | Yes                |
| Duplicates | Yes             | Yes                |
| Slicing    | Yes             | Yes                |
| Stores     | Characters/text | Any Python objects |

Example:

```python
text = "Python"
```

Cannot modify:

```python
# text[0] = "J"
```

But list can be modified:

```python
items = ["P", "y", "t"]

items[0] = "J"

print(items)
```

---

# 81. String vs Tuple

Both strings and tuples are immutable sequences.

| Feature  | String     | Tuple                |
| -------- | ---------- | -------------------- |
| Ordered  | Yes        | Yes                  |
| Indexed  | Yes        | Yes                  |
| Mutable  | No         | No                   |
| Iterable | Yes        | Yes                  |
| Slicing  | Yes        | Yes                  |
| Elements | Characters | Any hashable objects |

---

# 82. String Time Complexity

For a string of length `n`:

| Operation             |                         Typical Complexity |
| --------------------- | -----------------------------------------: |
| Indexing              |                                     `O(1)` |
| `len()`               |                                     `O(1)` |
| Slicing               |                                     `O(k)` |
| Concatenation         |          Depends on implementation/context |
| `in` substring search |          Generally `O(n)` for simple cases |
| `find()`              |             Generally linear-time behavior |
| `replace()`           |                             `O(n)` typical |
| `split()`             |                             `O(n)` typical |
| `join()`              | `O(n)` relative to total output/input size |
| `lower()`             |                                     `O(n)` |
| `upper()`             |                                     `O(n)` |
| `strip()`             |                          `O(n)` worst-case |

Here `k` represents the size of the resulting slice.

---

# 83. Important Performance Tip

Avoid repeatedly concatenating strings inside a large loop when building a large result.

Instead of:

```python
result = ""

for word in words:
    result += word
```

Prefer:

```python
result = "".join(words)
```

For example:

```python
words = ["Python", "is", "powerful"]

result = " ".join(words)

print(result)
```

Output:

```text
Python is powerful
```

---

# 84. DSA Example: Count Characters

```python
text = "banana"

count = {}

for char in text:
    count[char] = count.get(char, 0) + 1

print(count)
```

Output:

```text
{'b': 1, 'a': 3, 'n': 2}
```

This pattern is extremely common in DSA.

---

# 85. DSA Example: Check Palindrome

A palindrome reads the same forward and backward.

```python
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

Output:

```text
Palindrome
```

---

# 86. DSA Example: Reverse String

```python
text = "Python"

reverse = text[::-1]

print(reverse)
```

Output:

```text
nohtyP
```

---

# 87. DSA Example: Count Vowels

```python
text = "programming"

vowels = "aeiou"

count = 0

for char in text:
    if char in vowels:
        count += 1

print(count)
```

Output:

```text
3
```

---

# 88. DSA Example: Remove Duplicate Characters

```python
text = "banana"

result = ""

for char in text:
    if char not in result:
        result += char

print(result)
```

Output:

```text
ban
```

For large inputs, using a set for membership can improve the algorithm:

```python
text = "banana"

seen = set()
result = []

for char in text:
    if char not in seen:
        seen.add(char)
        result.append(char)

print("".join(result))
```

---

# 89. Common String Errors

## Error 1: Modifying a string

Wrong:

```python
text = "Python"

text[0] = "J"
```

Reason:

```text
Strings are immutable.
```

---

## Error 2: Concatenating string and integer

Wrong:

```python
age = 22

# print("Age: " + age)
```

Correct:

```python
print("Age: " + str(age))
```

or:

```python
print(f"Age: {age}")
```

---

## Error 3: Index Out of Range

```python
text = "Python"

# print(text[10])
```

Raises:

```text
IndexError
```

Valid indexes are:

```text
0 to len(text)-1
```

---

## Error 4: Confusing `find()` and `index()`

```text
find()  → -1 if not found
index() → ValueError if not found
```

---

# 90. Important Interview Questions

### Q1. What is a string?

A string is an ordered, indexed, iterable, immutable sequence of characters.

### Q2. Are strings mutable?

No.

### Q3. Can strings contain duplicate characters?

Yes.

### Q4. Can strings be indexed?

Yes.

```python
text[0]
```

### Q5. Can strings be sliced?

Yes.

```python
text[1:4]
```

### Q6. How do you reverse a string?

```python
text[::-1]
```

### Q7. Difference between `find()` and `index()`?

```text
find()  → -1
index() → ValueError
```

when the substring is not found.

### Q8. Difference between `split()` and `join()`?

```text
split() → String → List
join()  → Iterable of strings → String
```

### Q9. How do you check if a substring exists?

```python
"Python" in text
```

### Q10. How do you remove surrounding whitespace?

```python
text.strip()
```

### Q11. How do you convert a string to lowercase?

```python
text.lower()
```

### Q12. How do you create an f-string?

```python
name = "Faruk"

print(f"Hello {name}")
```

---

# 91. Quick Cheat Sheet

```python
# Create
text = "Python"

# Length
len(text)

# Index
text[0]

# Negative index
text[-1]

# Slice
text[0:3]

# Reverse
text[::-1]

# Loop
for char in text:
    print(char)

# Membership
"P" in text

# Concatenation
"Hello " + "World"

# Repetition
"Python " * 3

# Lowercase
text.lower()

# Uppercase
text.upper()

# Capitalize
text.capitalize()

# Title
text.title()

# Remove whitespace
text.strip()

# Replace
text.replace("Python", "Java")

# Split
text.split()

# Join
" ".join(["Python", "Java"])

# Find
text.find("Py")

# Count
text.count("a")

# Starts with
text.startswith("Py")

# Ends with
text.endswith("on")

# Character check
text.isalpha()
text.isdigit()
text.isalnum()
text.isspace()

# Unicode
ord("A")
chr(65)

# Convert
str(123)

# f-string
f"Hello {text}"
```

---

# 92. Final Summary

```text
Python String
      ↓
Ordered
      ↓
Indexed
      ↓
Iterable
      ↓
Immutable
      ↓
Supports Duplicate Characters
      ↓
Supports Slicing
      ↓
Supports Concatenation
      ↓
Supports Membership Testing
      ↓
String Methods
      ↓
split() / join()
      ↓
find() / index() / count()
      ↓
replace()
      ↓
lower() / upper() / title()
      ↓
strip()
      ↓
f-string Formatting
      ↓
Unicode
      ↓
DSA String Problems
```

# One-Line Definition

> **A string is an ordered, indexed, iterable, and immutable sequence of Unicode characters used to represent text in Python.**

'''
