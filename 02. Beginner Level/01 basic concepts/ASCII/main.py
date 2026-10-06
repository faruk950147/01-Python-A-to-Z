"""
# ASCII Code, Unicode, Encoding and Decoding in Python

---

# 1. What is ASCII?

**ASCII** stands for:

> **American Standard Code for Information Interchange**

ASCII is a character encoding standard that assigns a number to characters.

For example:

```text
A → 65
B → 66
C → 67

a → 97
b → 98
c → 99

0 → 48
1 → 49
2 → 50
```

In Python:

```python
print(ord("A"))
```

Output:

```text
65
```

---

# 2. Why is ASCII Used?

Computers work with numbers and bytes.

ASCII provides a standard way to represent common characters using numbers.

For example:

```text
Character
    ↓
ASCII number
    ↓
Computer processes the data
```

ASCII can represent:

* English uppercase letters
* English lowercase letters
* Digits
* Common symbols
* Control characters

---

# 3. Important ASCII Facts

ASCII is:

* A character encoding standard
* A **7-bit** code
* Able to represent **128 values**
* Uses values from **0 to 127**

Because:

```text
2⁷ = 128
```

Therefore:

```text
ASCII range = 0 to 127
```

---

# 4. ASCII and Python

Python provides two important functions:

## `ord()`

`ord()` converts a single character into its Unicode code point.

For ASCII characters, this value is the same as the ASCII value.

```python
print(ord("A"))
```

Output:

```text
65
```

---

## `chr()`

`chr()` converts an integer Unicode code point into a character.

```python
print(chr(65))
```

Output:

```text
A
```

### Easy Formula

```text
Character → ord() → Number

Number → chr() → Character
```

Example:

```python
print(ord("A"))   # 65
print(chr(65))    # A
```

---

# 5. ASCII Table

ASCII values range from:

```text
0 → 127
```

They are divided into:

```text
0–31       → Control characters
32–126     → Printable characters
127        → DEL
```

---

# 6. ASCII Control Characters

ASCII values `0–31` are mostly control characters.

`127` is also a control character called `DEL`.

| Decimal | Name | Meaning                   |
| ------: | ---- | ------------------------- |
|       0 | NUL  | Null                      |
|       1 | SOH  | Start of Heading          |
|       2 | STX  | Start of Text             |
|       3 | ETX  | End of Text               |
|       4 | EOT  | End of Transmission       |
|       5 | ENQ  | Enquiry                   |
|       6 | ACK  | Acknowledge               |
|       7 | BEL  | Bell                      |
|       8 | BS   | Backspace                 |
|       9 | TAB  | Horizontal Tab            |
|      10 | LF   | Line Feed                 |
|      11 | VT   | Vertical Tab              |
|      12 | FF   | Form Feed                 |
|      13 | CR   | Carriage Return           |
|      14 | SO   | Shift Out                 |
|      15 | SI   | Shift In                  |
|      16 | DLE  | Data Link Escape          |
|      17 | DC1  | Device Control 1          |
|      18 | DC2  | Device Control 2          |
|      19 | DC3  | Device Control 3          |
|      20 | DC4  | Device Control 4          |
|      21 | NAK  | Negative Acknowledge      |
|      22 | SYN  | Synchronous Idle          |
|      23 | ETB  | End of Transmission Block |
|      24 | CAN  | Cancel                    |
|      25 | EM   | End of Medium             |
|      26 | SUB  | Substitute                |
|      27 | ESC  | Escape                    |
|      28 | FS   | File Separator            |
|      29 | GS   | Group Separator           |
|      30 | RS   | Record Separator          |
|      31 | US   | Unit Separator            |
|     127 | DEL  | Delete                    |

### Common Control Characters

The most commonly encountered are:

```text
9  → Tab
10 → New Line (\n)
13 → Carriage Return (\r)
27 → Escape
```

---

# 7. Printable ASCII Characters

Printable ASCII characters range from:

```text
32 → 126
```

---

## Space and Symbols

```text
32   Space
33   !
34   "
35   #
36   $
37   %
38   &
39   '
40   (
41   )
42   *
43   +
44   ,
45   -
46   .
47   /
```

---

# 8. ASCII Digits

ASCII values for digits are:

```text
48 → 0
49 → 1
50 → 2
51 → 3
52 → 4
53 → 5
54 → 6
55 → 7
56 → 8
57 → 9
```

### Important

The character:

```text
"0"
```

is not the same as the integer:

```text
0
```

The ASCII value of the character `"0"` is:

```python
print(ord("0"))
```

Output:

```text
48
```

---

# 9. More ASCII Symbols

```text
58   :
59   ;
60   <
61   =
62   >
63   ?
64   @
```

---

# 10. Uppercase ASCII Letters

Uppercase English letters range from:

```text
65 → 90
```

| Character | ASCII |
| --------- | ----: |
| A         |    65 |
| B         |    66 |
| C         |    67 |
| D         |    68 |
| E         |    69 |
| F         |    70 |
| G         |    71 |
| H         |    72 |
| I         |    73 |
| J         |    74 |
| K         |    75 |
| L         |    76 |
| M         |    77 |
| N         |    78 |
| O         |    79 |
| P         |    80 |
| Q         |    81 |
| R         |    82 |
| S         |    83 |
| T         |    84 |
| U         |    85 |
| V         |    86 |
| W         |    87 |
| X         |    88 |
| Y         |    89 |
| Z         |    90 |

### Easy Trick

```text
A = 65
Z = 90
```

---

# 11. ASCII Symbols Between Uppercase and Lowercase

Values `91–96` are symbols:

```text
91 → [
92 → \
93 → ]
94 → ^
95 → _
96 → `
```

---

# 12. Lowercase ASCII Letters

Lowercase English letters range from:

```text
97 → 122
```

| Character | ASCII |
| --------- | ----: |
| a         |    97 |
| b         |    98 |
| c         |    99 |
| d         |   100 |
| e         |   101 |
| f         |   102 |
| g         |   103 |
| h         |   104 |
| i         |   105 |
| j         |   106 |
| k         |   107 |
| l         |   108 |
| m         |   109 |
| n         |   110 |
| o         |   111 |
| p         |   112 |
| q         |   113 |
| r         |   114 |
| s         |   115 |
| t         |   116 |
| u         |   117 |
| v         |   118 |
| w         |   119 |
| x         |   120 |
| y         |   121 |
| z         |   122 |

### Easy Trick

```text
a = 97
z = 122
```

---

# 13. Final ASCII Symbols

Values `123–126`:

```text
123 → {
124 → |
125 → }
126 → ~
```

---

# 14. Complete ASCII Structure

Remember these important ranges:

```text
ASCII

0–31      → Control characters
32–47     → Space + symbols
48–57     → Digits
58–64     → Symbols
65–90     → Uppercase letters
91–96     → Symbols
97–122    → Lowercase letters
123–126   → Symbols
127       → DEL
```

This is very useful for programming and interview questions.

---

# 15. Python ASCII Examples

## Uppercase Letters

```python
print("================ UPPERCASE LETTERS ================")

print(ord("A"))
print(ord("Z"))

print(chr(65))
print(chr(90))
```

Output:

```text
65
90
A
Z
```

---

# 16. Lowercase Letters

```python
print("================ LOWERCASE LETTERS ================")

print(ord("a"))
print(ord("z"))

print(chr(97))
print(chr(122))
```

Output:

```text
97
122
a
z
```

---

# 17. Numbers

Remember that ASCII represents the **characters** `0–9`.

```python
print("================ NUMBERS ================")

print(ord("0"))
print(ord("9"))

print(chr(48))
print(chr(57))
```

Output:

```text
48
57
0
9
```

---

# 18. Special Characters

```python
print("================ SPECIAL CHARACTERS ================")

print(ord("!"))
print(ord("~"))

print(chr(33))
print(chr(126))
```

Output:

```text
33
126
!
~
```

---

# 19. Whitespace Characters

Some common whitespace/control characters:

```python
print("================ WHITESPACE CHARACTERS ================")

print(ord(" "))
print(ord("\t"))
print(ord("\n"))

print(chr(32))
print(chr(9))
print(chr(10))
```

Values:

```text
Space → 32
Tab   → 9
Newline → 10
```

---

# 20. Important ASCII Patterns

There are some useful relationships.

## Uppercase

```text
A = 65
B = 66
C = 67
...
Z = 90
```

## Lowercase

```text
a = 97
b = 98
c = 99
...
z = 122
```

## Difference Between Uppercase and Lowercase

For the same English letter:

```text
a - A = 97 - 65 = 32
```

Therefore:

```text
'a' = 'A' + 32
```

For example:

```python
print(ord("A"))
print(ord("a"))
```

Output:

```text
65
97
```

Difference:

```text
32
```

---

# 21. ASCII vs Unicode

ASCII is limited.

ASCII can represent only:

```text
128 values
0–127
```

It mainly covers English letters, digits, symbols, and control characters.

But the world has many languages:

```text
English
বাংলা
中文
العربية
日本語
한국어
...
```

ASCII cannot represent all of these characters.

This is why **Unicode** is important.

---

# 22. What is Unicode?

**Unicode** is a universal character system designed to represent characters from many writing systems.

For example:

```text
A
বাংলা
中
😀
Ω
```

Unicode assigns each character a **code point**.

Example:

```text
A → U+0041
a → U+0061
```

In Python:

```python
print(ord("A"))
```

Output:

```text
65
```

Because:

```text
U+0041
```

is hexadecimal for decimal `65`.

---

# 23. `\u` Unicode Escape in Python

Python supports Unicode escape sequences using:

```text
\uXXXX
```

where `XXXX` is **4 hexadecimal digits**.

Example:

```python
print("\u0041")
```

Output:

```text
A
```

Another example:

```python
print("\u005A")
```

Output:

```text
Z
```

### Remember

```text
\u + 4 hexadecimal digits
```

Example:

```text
\u0041
```

---

# 24. `\U` Unicode Escape in Python

Python also supports:

```text
\UXXXXXXXX
```

where `XXXXXXXX` contains **8 hexadecimal digits**.

For example:

```python
print("\U00000041")
```

Output:

```text
A
```

And:

```python
print("\U0000005A")
```

Output:

```text
Z
```

### Important Correction

The format is:

```text
\UXXXXXXXX
```

not:

```text
\UXXXXXX
```

It uses **8 hexadecimal digits**.

---

# 25. Unicode Examples

```python
print("\U00000041")
print("\U0000005A")
```

Output:

```text
A
Z
```

You can also represent characters outside ASCII.

For example:

```python
print("\U0001F600")
```

Output:

```text
😀
```

---

# 26. Decimal and Hexadecimal Unicode Values

Unicode code points are commonly written in hexadecimal.

For example:

```text
Character    Decimal    Hexadecimal

A            65         U+0041
Z            90         U+005A
a            97         U+0061
z            122        U+007A
```

Example:

```text
A
↓
Decimal = 65
↓
Hexadecimal = 41
↓
Unicode = U+0041
```

---

# 27. Understanding Hexadecimal

Hexadecimal is a base-16 number system.

It uses:

```text
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

Values:

```text
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15
```

---

# 28. Convert Hexadecimal to Decimal

For example:

```text
41
```

Hexadecimal means:

```text
4 × 16¹ + 1 × 16⁰
```

So:

```text
4 × 16 + 1
= 64 + 1
= 65
```

Therefore:

```text
0x41 = 65
```

And:

```text
U+0041 = A
```

---

# 29. `ord()` and Unicode

An important Python concept:

> `ord()` is not only for ASCII.

It returns the Unicode code point of a character.

Example:

```python
print(ord("A"))
print(ord("a"))
```

Output:

```text
65
97
```

For a non-ASCII character:

```python
print(ord("😀"))
```

Python returns its Unicode code point as a decimal integer.

So:

```text
ASCII character
      ↓
Unicode code point
      ↓
For ASCII characters, it is the same number as ASCII
```

---

# 30. `chr()` and Unicode

`chr()` does the reverse:

```python
print(chr(65))
```

Output:

```text
A
```

It can also create Unicode characters:

```python
print(chr(128512))
```

Output:

```text
😀
```

Therefore:

```text
ord()
Character → Unicode code point

chr()
Unicode code point → Character
```

---

# 31. What is Encoding?

**Encoding** is the process of converting text into bytes using a particular character encoding such as UTF-8.

For example:

```python
text = "Hello"

encoded = text.encode("utf-8")

print(encoded)
```

Output:

```text
b'Hello'
```

Here:

```text
String
  ↓
UTF-8 encoding
  ↓
Bytes
```

---

# 32. What is Decoding?

**Decoding** is the reverse process.

It converts bytes back into a string using the correct encoding.

Example:

```python
encoded = b"Hello"

decoded = encoded.decode("utf-8")

print(decoded)
```

Output:

```text
Hello
```

Flow:

```text
Bytes
  ↓
UTF-8 decoding
  ↓
String
```

---

# 33. Encoding Example

```python
text = "Hello"

encoded = text.encode("utf-8")

print(encoded)
print(type(encoded))
```

Output:

```text
b'Hello'
<class 'bytes'>
```

So:

```text
str → bytes
```

---

# 34. Decoding Example

```python
encoded = b"Hello"

decoded = encoded.decode("utf-8")

print(decoded)
print(type(decoded))
```

Output:

```text
Hello
<class 'str'>
```

So:

```text
bytes → str
```

---

# 35. Encoding with Non-English Text

UTF-8 can represent many languages.

Example:

```python
text = "বাংলা"

encoded = text.encode("utf-8")

print(encoded)

decoded = encoded.decode("utf-8")

print(decoded)
```

Flow:

```text
বাংলা
  ↓
UTF-8 encode
  ↓
bytes
  ↓
UTF-8 decode
  ↓
বাংলা
```

This is one reason UTF-8 is widely used.

---

# 36. ASCII vs Unicode vs UTF-8

These concepts are related but different.

| Concept | Meaning                                       |
| ------- | --------------------------------------------- |
| ASCII   | Older 7-bit character encoding standard       |
| Unicode | Universal character/code-point system         |
| UTF-8   | A way to encode Unicode characters into bytes |

### Simple Mental Model

```text
Unicode
   ↓
Characters get code points
   ↓
UTF-8
   ↓
Code points are encoded as bytes
```

ASCII is a smaller character set/encoding standard.

UTF-8 is designed so that ASCII characters use the same byte values in UTF-8.

---

# 37. Very Important Difference

Do not think:

```text
Encoding = character → number
Decoding = number → character
```

This is an oversimplification.

More accurately:

```text
Unicode code point
        ↓
UTF-8 encoding
        ↓
Bytes
```

And:

```text
Bytes
        ↓
UTF-8 decoding
        ↓
Unicode text
```

For learning basic ASCII:

```text
Character ↔ Number
```

is a useful mental model.

But for real Python text processing:

```text
str ↔ bytes
```

is the more important encoding/decoding concept.

---

# 38. Complete Relationship

```text
Character
    ↓
Unicode Code Point
    ↓
Encoding
    ↓
Bytes
    ↓
Storage / Network
    ↓
Decoding
    ↓
Unicode Text
    ↓
Character
```

Example:

```text
A
↓
U+0041
↓
UTF-8
↓
0x41
↓
Byte
↓
UTF-8 decoding
↓
A
```

---

# 39. Python String vs Bytes

## String

Python text is represented by `str`.

```python
text = "Hello"

print(type(text))
```

Output:

```text
<class 'str'>
```

## Bytes

Encoded data is represented by `bytes`.

```python
data = b"Hello"

print(type(data))
```

Output:

```text
<class 'bytes'>
```

---

# 40. Useful Python Examples

## Character to Number

```python
char = "A"

value = ord(char)

print(value)
```

Output:

```text
65
```

---

## Number to Character

```python
value = 65

char = chr(value)

print(char)
```

Output:

```text
A
```

---

## String to Bytes

```python
text = "Hello"

data = text.encode("utf-8")

print(data)
```

Output:

```text
b'Hello'
```

---

## Bytes to String

```python
data = b"Hello"

text = data.decode("utf-8")

print(text)
```

Output:

```text
Hello
```

---

# 41. Useful ASCII Program

Print ASCII values of uppercase letters:

```python
for value in range(65, 91):
    print(value, chr(value))
```

Output starts with:

```text
65 A
66 B
67 C
...
90 Z
```

---

# 42. Print ASCII Values of Lowercase Letters

```python
for value in range(97, 123):
    print(value, chr(value))
```

Output:

```text
97 a
98 b
99 c
...
122 z
```

---

# 43. Print ASCII Values of Digits

```python
for value in range(48, 58):
    print(value, chr(value))
```

Output:

```text
48 0
49 1
50 2
...
57 9
```

---

# 44. Convert a Word to ASCII Values

```python
text = "Hello"

for char in text:
    print(char, ord(char))
```

Output:

```text
H 72
e 101
l 108
l 108
o 111
```

---

# 45. Convert ASCII Values Back to Characters

```python
values = [72, 101, 108, 108, 111]

text = ""

for value in values:
    text += chr(value)

print(text)
```

Output:

```text
Hello
```

---

# 46. ASCII Character Check

You can check whether a character belongs to the ASCII range:

```python
char = "A"

if ord(char) <= 127:
    print("ASCII character")
```

A more direct method is:

```python
char = "A"

if ord(char) < 128:
    print("ASCII")
else:
    print("Non-ASCII")
```

---

# 47. Important ASCII Ranges to Memorize

For programming and interviews, remember these:

```text
Space       = 32

0           = 48
9           = 57

A           = 65
Z           = 90

a           = 97
z           = 122
```

The most important ranges:

```text
0–9   → 48–57
A–Z   → 65–90
a–z   → 97–122
```

---

# 48. ASCII Quick Revision

```text
ASCII
 ↓
American Standard Code for Information Interchange
 ↓
7-bit
 ↓
128 values
 ↓
0–127
```

Important functions:

```text
ord()
Character → Unicode code point

chr()
Unicode code point → Character
```

Important ranges:

```text
0–31       → Control characters
32–126     → Printable characters
127        → DEL

48–57      → 0–9
65–90      → A–Z
97–122     → a–z
```

---

# 49. Unicode Quick Revision

```text
Unicode
 ↓
Represents characters from many writing systems
 ↓
Each character has a code point
```

Python Unicode escapes:

```text
\uXXXX
```

4 hexadecimal digits.

Example:

```python
print("\u0041")
```

Output:

```text
A
```

Long form:

```text
\UXXXXXXXX
```

8 hexadecimal digits.

Example:

```python
print("\U00000041")
```

Output:

```text
A
```

---

# 50. Encoding / Decoding Quick Revision

### Encoding

```text
str
 ↓
encode()
 ↓
bytes
```

Example:

```python
"Hello".encode("utf-8")
```

### Decoding

```text
bytes
 ↓
decode()
 ↓
str
```

Example:

```python
b"Hello".decode("utf-8")
```

---

# 51. Interview Questions

### Q1. What is ASCII?

**Answer:**

ASCII stands for American Standard Code for Information Interchange. It is a 7-bit character encoding standard that represents 128 values from 0 to 127.

---

### Q2. How many characters can ASCII represent?

**Answer:**

ASCII uses 7 bits, so it can represent:

```text
2⁷ = 128
```

values.

---

### Q3. What is the ASCII value of `A`?

**Answer:**

```text
65
```

---

### Q4. What is the ASCII value of `a`?

**Answer:**

```text
97
```

---

### Q5. What is the ASCII value of `0`?

**Answer:**

The character `"0"` has ASCII value:

```text
48
```

---

### Q6. What does `ord()` do?

**Answer:**

`ord()` returns the Unicode code point of a character. For ASCII characters, this is the same as the ASCII value.

Example:

```python
ord("A")
```

Output:

```text
65
```

---

### Q7. What does `chr()` do?

**Answer:**

`chr()` converts a Unicode code point integer into a character.

Example:

```python
chr(65)
```

Output:

```text
A
```

---

### Q8. What is Unicode?

**Answer:**

Unicode is a universal character system designed to represent characters from many languages and writing systems.

---

### Q9. What is the difference between ASCII and Unicode?

**Answer:**

ASCII is limited to 128 values and mainly represents basic English characters and control characters.

Unicode is designed to represent characters from many languages and symbol systems.

---

### Q10. What is UTF-8?

**Answer:**

UTF-8 is a variable-length encoding that represents Unicode text as bytes.

---

### Q11. What is encoding?

**Answer:**

Encoding converts text (`str`) into bytes using an encoding such as UTF-8.

```python
text.encode("utf-8")
```

---

### Q12. What is decoding?

**Answer:**

Decoding converts bytes back into text.

```python
data.decode("utf-8")
```

---

### Q13. What is the difference between `str` and `bytes`?

**Answer:**

`str` represents text, while `bytes` represents binary data.

```python
text = "Hello"
data = b"Hello"
```

---

### Q14. What is the ASCII range?

**Answer:**

```text
0–127
```

---

### Q15. What are the ASCII ranges for letters?

**Answer:**

```text
A–Z → 65–90
a–z → 97–122
```

---

# 52. Final Mental Model

Remember this:

```text
                 ASCII
                   ↓
        Basic character encoding
                   ↓
              0 – 127
                   ↓
       English + digits + symbols
```

For modern text:

```text
                Unicode
                   ↓
          Character code points
                   ↓
                 UTF-8
                   ↓
                Bytes
                   ↓
         Storage / Network
                   ↓
               Decoding
                   ↓
                Text
```

And in Python:

```text
ord()
Character → Number

chr()
Number → Character

encode()
str → bytes

decode()
bytes → str
```

## Most Important Values

```text
Space = 32

0 = 48
9 = 57

A = 65
Z = 90

a = 97
z = 122
```

## One-Line Summary

> **ASCII gives basic characters numeric values, Unicode provides code points for a much larger set of characters, and UTF-8 encodes Unicode text into bytes for storage and communication.**

"""