"""
# Python Regular Expression (RegEx)

## 1. What is Regular Expression?

**Regular Expression (RegEx)** is a sequence of characters that defines a **search pattern**.

It is used to:

* Search for text
* Match patterns
* Validate data
* Extract information
* Replace text
* Split strings

Python provides the `re` module for working with regular expressions.

```python
import re
```

---

# 2. Important Regex Symbols

| Symbol  | Meaning                         |    |
| ------- | ------------------------------- | -- |
| `.`     | Any single character            |    |
| `^`     | Start of the string             |    |
| `$`     | End of the string               |    |
| `*`     | Zero or more occurrences        |    |
| `+`     | One or more occurrences         |    |
| `?`     | Zero or one occurrence          |    |
| `       | `                               | OR |
| `\w`    | Word character                  |    |
| `\W`    | Non-word character              |    |
| `\d`    | Digit                           |    |
| `\D`    | Non-digit                       |    |
| `\s`    | Whitespace                      |    |
| `\S`    | Non-whitespace                  |    |
| `[]`    | Character class                 |    |
| `()`    | Group                           |    |
| `{n}`   | Exactly `n` occurrences         |    |
| `{n,}`  | At least `n` occurrences        |    |
| `{n,m}` | Between `n` and `m` occurrences |    |

---

# 3. `.` — Dot

`.` matches **any single character** except a newline by default.

```python
import re

text = "Bangladesh"

match = re.search(r".", text)

if match:
    print(match.group())
```

Output:

```text
B
```

### Example

```python
text = "Bangladesh"

match = re.search(r"B.n", text)

if match:
    print(match.group())
```

The pattern:

```text
B.n
```

means:

```text
B + any one character + n
```

---

# 4. `^` — Start of String

`^` matches the **start of the string**.

```python
import re

text = "Bangladesh"

match = re.search(r"^B", text)

if match:
    print(match.group())
```

Output:

```text
B
```

### Example

```python
text = "Bangladesh India"

match = re.search(r"^\w+", text)

print(match.group())
```

Output:

```text
Bangladesh
```

---

# 5. `$` — End of String

`$` matches the **end of the string**.

```python
import re

text = "Bangladesh"

match = re.search(r"d$", text)

if match:
    print(match.group())
```

Output:

```text
d
```

### Example

```python
text = "Bangladesh India Iceland"

match = re.search(r"\w+$", text)

print(match.group())
```

Output:

```text
Iceland
```

---

# 6. `*` — Zero or More

`*` means **zero or more occurrences** of the preceding pattern.

```python
import re

text = "Bdddd"

match = re.search(r"Bd*", text)

if match:
    print(match.group())
```

Output:

```text
Bdddd
```

Here:

```text
d*
```

means:

```text
zero or more d characters
```

For example:

```text
B
Bd
Bdd
Bddd
Bdddd
```

can all match `Bd*`.

---

# 7. `+` — One or More

`+` means **one or more occurrences**.

```python
import re

text = "12345"

match = re.search(r"\d+", text)

print(match.group())
```

Output:

```text
12345
```

### Difference

```text
\d*   → zero or more digits
\d+   → one or more digits
```

---

# 8. `?` — Zero or One

`?` normally means **zero or one occurrence** of the preceding pattern.

Example:

```python
import re

text = "color"

match = re.search(r"colou?r", text)

print(match.group())
```

This pattern can match:

```text
color
colour
```

because:

```text
u?
```

means the `u` may appear **zero or one time**.

---

# 9. `|` — OR

`|` means **OR**.

```python
import re

pattern = r"(abc|def)"
text = "abc def ghi"

match = re.findall(pattern, text)

print(match)
```

Output:

```text
['abc', 'def']
```

---

# 10. `\w` — Word Character

`\w` matches a word character.

In Python, it generally includes:

```text
Letters
Digits
Underscore (_)
```

Example:

```python
import re

text = "Bangladesh"

match = re.search(r"\w+", text)

print(match.group())
```

Output:

```text
Bangladesh
```

### `\w+`

```text
\w+ → one or more word characters
```

---

# 11. `\W` — Non-Word Character

`\W` is the opposite of `\w`.

It matches characters that are not word characters.

Examples:

```text
space
@
#
$
%
!
```

Example:

```python
import re

text = "Hello World"

match = re.search(r"\W+", text)

print(repr(match.group()))
```

Output:

```text
' '
```

---

# 12. `\d` — Digit

`\d` matches a digit.

```text
0-9
```

Example:

```python
import re

text = "My age is 25"

match = re.search(r"\d+", text)

print(match.group())
```

Output:

```text
25
```

---

# 13. `\D` — Non-Digit

`\D` matches any character that is **not a digit**.

```python
import re

text = "abc123"

match = re.search(r"\D+", text)

print(match.group())
```

Output:

```text
abc
```

---

# 14. `\s` — Whitespace

`\s` matches whitespace characters.

Examples:

```text
Space
Tab
Newline
```

Example:

```python
import re

text = "Hello World"

match = re.search(r"\s", text)

print(repr(match.group()))
```

Output:

```text
' '
```

---

# 15. `\S` — Non-Whitespace

`\S` matches any character that is **not whitespace**.

```python
import re

text = "Hello World"

match = re.search(r"\S+", text)

print(match.group())
```

Output:

```text
Hello
```

---

# 16. Character Class `[]`

A **character class** is a set of characters that you want to match.

It is written using square brackets:

```text
[]
```

---

## `[0-9]`

Matches any one digit.

```python
import re

text = "abc 123"

match = re.findall(r"[0-9]", text)

print(match)
```

Output:

```text
['1', '2', '3']
```

---

## `[a-z]`

Matches lowercase letters.

```python
import re

text = "abc DEF 123"

match = re.findall(r"[a-z]", text)

print(match)
```

Output:

```text
['a', 'b', 'c']
```

---

## `[A-Z]`

Matches uppercase letters.

```python
import re

text = "abc DEF 123"

match = re.findall(r"[A-Z]", text)

print(match)
```

Output:

```text
['D', 'E', 'F']
```

---

## `[a-zA-Z0-9]`

Matches letters or digits.

```python
import re

text = "abc DEF 123"

match = re.findall(r"[a-zA-Z0-9]", text)

print(match)
```

Output:

```text
['a', 'b', 'c', 'D', 'E', 'F', '1', '2', '3']
```

---

# 17. Group `()`

Parentheses `()` are used to create a **group**.

Example:

```python
import re

pattern = r"(abc|def)"
text = "abc def ghi"

match = re.findall(pattern, text)

print(match)
```

Output:

```text
['abc', 'def']
```

Groups are useful when you want to treat multiple characters or patterns as a single unit.

Examples:

```text
(abc)
(def)
(abc|def)
```

---

# 18. Quantifier `{}`

Curly braces specify how many times a pattern should occur.

## `{n}` — Exactly n times

```python
import re

text = "123456"

match = re.findall(r"\d{2}", text)

print(match)
```

Output:

```text
['12', '34', '56']
```

---

## `{n,}` — At Least n Times

```python
import re

text = "123456"

match = re.findall(r"\d{3,}", text)

print(match)
```

Output:

```text
['123456']
```

---

## `{n,m}` — Between n and m Times

```python
import re

text = "123456"

match = re.findall(r"\d{2,4}", text)

print(match)
```

Output:

```text
['1234', '56']
```

---

# 19. `re.findall()`

`re.findall()` returns **all non-overlapping matches** as a list.

```python
import re

text = "Bangladesh India New Zealand Netherlands Iceland"

matches = re.findall(r"\w+", text)

print(matches)
```

Output:

```text
['Bangladesh', 'India', 'New', 'Zealand', 'Netherlands', 'Iceland']
```

### Example: Extract Dates

```python
import re

text = "2025-10-21 the conference will be held on 2025-10-21"

matches = re.findall(r"\d{4}-\d{2}-\d{2}", text)

print(matches)
```

Output:

```text
['2025-10-21', '2025-10-21']
```

---

# 20. `re.search()`

`re.search()` searches the **entire string** and returns the **first match**.

```python
import re

text = "Bangladesh India New Zealand"

match = re.search(r"\w+", text)

if match:
    print(match.group())
else:
    print("Not found")
```

Output:

```text
Bangladesh
```

### Important

```text
re.search()
    ↓
Search the entire string
    ↓
Return the first match
```

---

# 21. `re.match()`

`re.match()` checks for a match **only at the beginning of the string**.

```python
import re

text = "America Bangladesh"

match = re.match(r"America", text)

if match:
    print(match.group())
else:
    print("Not found")
```

Output:

```text
America
```

But:

```python
text = "Bangladesh America"

match = re.match(r"America", text)
```

returns:

```text
None
```

because `America` is not at the beginning.

---

# 22. `re.fullmatch()`

`re.fullmatch()` requires the **entire string** to match the pattern.

```python
import re

pattern = r"\d+"
text = "12345"

match = re.fullmatch(pattern, text)

if match:
    print("Valid")
else:
    print("Invalid")
```

Output:

```text
Valid
```

But:

```text
12345abc
```

would be:

```text
Invalid
```

---

# 23. `match.group()`

`group()` returns the text that was matched.

```python
import re

text = "My age is 25"

match = re.search(r"\d+", text)

if match:
    print(match.group())
```

Output:

```text
25
```

---

# 24. `re.IGNORECASE`

`re.IGNORECASE` or `re.I` makes matching **case-insensitive**.

```python
import re

pattern = r"america"
text = "America Bangladesh"

match = re.search(pattern, text, re.IGNORECASE)

if match:
    print(match.group())
```

Output:

```text
America
```

Without `re.IGNORECASE`, lowercase `america` would not match uppercase `America`.

---

# 25. Raw String `r""`

When writing regex patterns in Python, raw strings are generally recommended.

Examples:

```python
r"\d+"
r"\w+"
r"\s+"
r"\."
```

Example:

```python
pattern = r"\d+"
```

The `r` tells Python to treat the string as a **raw string**, which makes backslashes easier to use in regex patterns.

---

# 26. `*` vs `\*`

This is very important.

## `*`

`*` is a regex quantifier:

```text
0 or more
```

Example:

```python
r"\d*"
```

means:

```text
Zero or more digits
```

---

## `\*`

`\*` matches the actual `*` character.

```python
r"\*"
```

means:

```text
Match a literal *
```

### Therefore:

```text
\d*   → zero or more digits

\d\*  → one digit followed by a literal *
```

---

# 27. `\.` — Literal Dot

In regex:

```text
. → any character
```

If you want to match an actual dot:

```text
\.
```

Example:

```python
import re

text = "Hello World .1235"

match = re.findall(r"\.", text)

print(match)
```

Output:

```text
['.']
```

---

# 28. `re.compile()`

`re.compile()` creates a reusable regex pattern.

It is useful when the same pattern is used multiple times.

```python
import re

pattern = re.compile(r"\d+")

text = "My numbers are 123 and 456"

matches = pattern.findall(text)

print(matches)
```

Output:

```text
['123', '456']
```

---

# 29. Bangladesh Phone Number Validation

A common Bangladeshi mobile number format is:

```text
01XXXXXXXXX
```

The pattern is:

```python
r"^01[3-9]\d{8}$"
```

Example:

```python
import re

phone = "01712345678"

pattern = r"^01[3-9]\d{8}$"

if re.fullmatch(pattern, phone):
    print("Valid Bangladeshi phone number")
else:
    print("Invalid phone number")
```

Output:

```text
Valid Bangladeshi phone number
```

### Pattern Breakdown

```text
^
→ Start

01
→ Literal 01

[3-9]
→ One digit from 3 to 9

\d{8}
→ Exactly 8 more digits

$
→ End
```

---

# 30. Bangladesh Phone Number with `+880`

International format:

```text
+8801712345678
```

Pattern:

```python
r"^\+8801[3-9]\d{8}$"
```

Example:

```python
import re

phone = "+8801712345678"

pattern = r"^\+8801[3-9]\d{8}$"

if re.fullmatch(pattern, phone):
    print("Valid Bangladeshi phone number")
else:
    print("Invalid phone number")
```

---

# 31. Indian Phone Number Validation

A common Indian mobile number pattern is:

```text
10 digits
First digit: 6-9
```

Regex:

```python
r"^[6-9]\d{9}$"
```

Example:

```python
import re

phone = "9876543210"

pattern = r"^[6-9]\d{9}$"

if re.fullmatch(pattern, phone):
    print("Valid Indian phone number")
else:
    print("Invalid phone number")
```

---

# 32. Bangladesh / India Phone Detection

```python
import re

text = "+8801712345678"

bd_pattern = r"^\+8801[3-9]\d{8}$"
in_pattern = r"^\+91[6-9]\d{9}$"

if re.fullmatch(bd_pattern, text):
    print("Valid Bangladeshi phone number")

elif re.fullmatch(in_pattern, text):
    print("Valid Indian phone number")

else:
    print("Invalid phone number")
```

---

# 33. Date Extraction

For the format:

```text
YYYY-MM-DD
```

we can use:

```python
r"\d{4}-\d{2}-\d{2}"
```

Example:

```python
import re

text = "2025-10-21 and 2026-01-15"

dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)

print(dates)
```

Output:

```text
['2025-10-21', '2026-01-15']
```

> Note: This regex checks the format only. It can match values such as `2025-99-99`. For actual calendar-date validation, use Python's `datetime` module.

---

# 34. Email Validation

A commonly used basic email pattern is:

```python
r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
```

Example:

```python
import re

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

email = "faruk950147@gmail.com"

if re.fullmatch(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")
```

Output:

```text
Valid email address
```

### Pattern Breakdown

```text
[A-Za-z0-9._%+-]+
        ↓
Username

@
        ↓
At symbol

[A-Za-z0-9.-]+
        ↓
Domain

\.
        ↓
Literal dot

[A-Za-z]{2,}
        ↓
Domain extension
```

Example:

```text
faruk950147@gmail.com
│          │     │
│          │     └── com
│          └──────── gmail
└─────────────────── username
```

---

# 35. Password Validation

Suppose we want:

* Letters
* Digits
* `$`
* `@`
* Minimum 6 characters

Pattern:

```python
r"^[0-9a-zA-Z$@]{6,}$"
```

Example:

```python
import re

password = input("Enter a password: ")

pattern = r"^[0-9a-zA-Z$@]{6,}$"

if re.fullmatch(pattern, password):
    print("Password is valid")
else:
    print("Password is not valid")
```

### Pattern Breakdown

```text
^
→ Start

[0-9a-zA-Z$@]
→ Allowed characters

{6,}
→ Minimum 6 characters

$
→ End
```

> This pattern only checks allowed characters and minimum length. It does not require a specific combination of uppercase letters, lowercase letters, digits, and special characters.

---

# 36. Extract Numbers from Text

```python
import re

phone = "phone number: 08801712345678"

match = re.search(r"\d+", phone)

if match:
    print(match.group())
else:
    print("Not found")
```

Output:

```text
08801712345678
```

---

# 37. `\d`, `\D`, `\s`, `\S`, `\w`, `\W` with `+`

These combinations are very common.

```text
\d+   → one or more digits

\D+   → one or more non-digits

\s+   → one or more whitespace characters

\S+   → one or more non-whitespace characters

\w+   → one or more word characters

\W+   → one or more non-word characters
```

Example:

```python
import re

text = "Hello World .1235"

print(re.findall(r"\d+", text))
print(re.findall(r"\D+", text))
print(re.findall(r"\s+", text))
print(re.findall(r"\S+", text))
print(re.findall(r"\w+", text))
print(re.findall(r"\W+", text))
```

---

# 38. `re.sub()` — Replace Text

`re.sub()` replaces text that matches a pattern.

Example:

```python
import re

text = "Hello    World"

result = re.sub(r"\s+", " ", text)

print(result)
```

Output:

```text
Hello World
```

### Remove separators from a phone number

```python
import re

phone = "+880-1712-345678"

clean_phone = re.sub(r"[-.\s]", "", phone)

print(clean_phone)
```

Output:

```text
+8801712345678
```

---

# 39. `re.split()` — Split Using Regex

`re.split()` splits a string based on a regex pattern.

```python
import re

text = "apple,banana;orange apple"

result = re.split(r"[,; ]+", text)

print(result)
```

Output:

```text
['apple', 'banana', 'orange', 'apple']
```

---

# 40. `re.finditer()`

`re.finditer()` returns an iterator containing match objects.

```python
import re

text = "There are 12 apples and 25 oranges."

matches = re.finditer(r"\d+", text)

for match in matches:
    print(match.group())
```

Output:

```text
12
25
```

---

# 41. Greedy vs Non-Greedy

This is an important advanced concept.

## Greedy

```text
.*
```

tries to match as much as possible.

Example:

```python
import re

text = "Bangladesh India"

match = re.search(r"B.*a", text)

print(match.group())
```

---

## Non-Greedy

```text
.*?
```

tries to match as little as possible while still allowing the complete pattern to match.

Example:

```python
match = re.search(r"B.*?a", text)

print(match.group())
```

### Important

The meaning of `?` depends on its position.

```text
u?    → u is optional (zero or one)

+?    → non-greedy version of +

*?    → non-greedy version of *

??    → non-greedy version of ?
```

So `?` does **not always independently mean "zero or one"**.

---

# 42. Common Regex Examples

### Only digits

```python
r"^\d+$"
```

### Only letters

```python
r"^[A-Za-z]+$"
```

### Letters and digits

```python
r"^[A-Za-z0-9]+$"
```

### Bangladesh mobile number

```python
r"^01[3-9]\d{8}$"
```

### Bangladesh international mobile number

```python
r"^\+8801[3-9]\d{8}$"
```

### Indian mobile number

```python
r"^[6-9]\d{9}$"
```

### Date: `YYYY-MM-DD`

```python
r"^\d{4}-\d{2}-\d{2}$"
```

### Basic email

```python
r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
```

### Minimum 8 characters

```python
r".{8,}"
```

---

# 43. Common Regex Methods

| Method           | Purpose                                      |
| ---------------- | -------------------------------------------- |
| `re.search()`    | Finds the first match anywhere in the string |
| `re.match()`     | Matches only at the beginning                |
| `re.fullmatch()` | Matches the entire string                    |
| `re.findall()`   | Returns all matches as a list                |
| `re.finditer()`  | Returns all matches as match objects         |
| `re.sub()`       | Replaces matched text                        |
| `re.split()`     | Splits a string using a regex                |
| `re.compile()`   | Creates a reusable regex pattern             |

---

# 44. Regex Cheat Sheet

```text
CHARACTERS
────────────────────────────
.       → Any single character
\d      → Digit
\D      → Non-digit
\w      → Word character
\W      → Non-word character
\s      → Whitespace
\S      → Non-whitespace


QUANTIFIERS
────────────────────────────
*       → 0 or more
+       → 1 or more
?       → 0 or 1
{n}     → Exactly n
{n,}    → At least n
{n,m}   → n to m


POSITION
────────────────────────────
^       → Start of string
$       → End of string


GROUPING / CHOICE
────────────────────────────
[]      → Character class
()      → Group
|       → OR


ESCAPING
────────────────────────────
\.      → Literal dot
\*      → Literal *
\+      → Literal +
\?      → Literal ?
```

---

# 45. The Most Important Concepts to Remember

```text
.       → Any character

^       → Start

$       → End

*       → 0 or more

+       → 1 or more

?       → 0 or 1

\d      → Digit

\w      → Word character

\s      → Whitespace

[]      → Character class

()      → Group

|       → OR

{}      → Specific number of repetitions
```

---

# 46. Final Mental Model

Think about Regex using four main concepts:

```text
Character
    +
Quantity
    +
Position
    +
Grouping
```

For example:

```python
r"^01[3-9]\d{8}$"
```

Breakdown:

```text
^
↓
Start

01
↓
Literal "01"

[3-9]
↓
One digit from 3 to 9

\d{8}
↓
Exactly 8 more digits

$
↓
End
```

Therefore:

```text
01 + one digit from 3-9 + eight digits
```

which gives an 11-digit Bangladeshi mobile-number pattern.

---

# 47. Quick Revision

```text
re.search()
    → Search the entire string
    → Return the first match

re.match()
    → Check only from the beginning

re.fullmatch()
    → Entire string must match

re.findall()
    → Return all matches as a list

re.finditer()
    → Return all matches as match objects

re.sub()
    → Replace matches

re.split()
    → Split using a regex

re.compile()
    → Create a reusable pattern
```

### Core Regex Pattern

```text
^        Start
[ ]      Allowed characters
()       Group
|        OR
\d       Digit
\w       Word
\s       Whitespace
*        0+
+        1+
?        0/1
{n}      Exactly n
{n,}     Minimum n
{n,m}    n to m
$        End
```

"""