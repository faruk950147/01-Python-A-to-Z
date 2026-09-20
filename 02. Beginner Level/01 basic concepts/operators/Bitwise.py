"""
    # Python Bitwise Operators

    Your examples are correct. Here’s a clean explanation of **Python Bitwise Operators** in Bangla, including why `~12` becomes `-13`.

    ---

    ## 1. Right Shift `>>`

    Right shift moves all bits to the right.

    For positive integers:

    ```text
    a >> n = a / 2^n
    ```

    (integer division)

    ```python
    print(8 >> 1)   # 4
    print(8 >> 2)   # 2
    print(8 >> 3)   # 1
    ```

    ### Example

    ```text
    8 = 1000

    1000 >> 1 = 0100 = 4
    1000 >> 2 = 0010 = 2
    1000 >> 3 = 0001 = 1
    ```

    So:

    ```text
    8 >> 1 → 8 / 2¹ = 4
    8 >> 2 → 8 / 2² = 2
    8 >> 3 → 8 / 2³ = 1
    ```

    ---

    ## 2. Left Shift `<<`

    Left shift moves all bits to the left.

    For positive integers:

    ```text
    a << n = a × 2^n
    ```

    ```python
    print(4 << 1)   # 8
    print(4 << 2)   # 16
    print(4 << 3)   # 32
    ```

    ### Binary

    ```text
    4 = 0100

    0100 << 1 = 1000   = 8
    0100 << 2 = 10000  = 16
    0100 << 3 = 100000 = 32
    ```

    Therefore:

    ```text
    4 << 1 → 4 × 2¹ = 8
    4 << 2 → 4 × 2² = 16
    4 << 3 → 4 × 2³ = 32
    ```

    ---

    # 3. Bitwise AND `&`

    AND compares corresponding bits.

    ### Rule

    | A | B | A & B |
    | - | - | ----- |
    | 0 | 0 | 0     |
    | 0 | 1 | 0     |
    | 1 | 0 | 0     |
    | 1 | 1 | 1     |

    Only `1 & 1` gives `1`.

    ### Example

    ```python
    print(12 & 10)   # 8
    ```

    ```text
    12 = 1100
    10 = 1010
        ----
        1000 = 8
    ```

    Another:

    ```python
    print(15 & 7)    # 7
    ```

    ```text
    15 = 1111
    7 = 0111
        ----
        0111 = 7
    ```

    ---

    # 4. Bitwise OR `|`

    OR compares corresponding bits.

    ### Rule

    | A | B | A | B |
    | - | - | ----- |
    | 0 | 0 | 0     |
    | 0 | 1 | 1     |
    | 1 | 0 | 1     |
    | 1 | 1 | 1     |

    Only `0 | 0` gives `0`.

    ### Example

    ```python
    print(12 | 10)   # 14
    ```

    ```text
    12 = 1100
    10 = 1010
        ----
        1110 = 14
    ```

    Another:

    ```python
    print(15 | 7)    # 15
    ```

    ```text
    15 = 1111
    7 = 0111
        ----
        1111 = 15
    ```

    ---

    # 5. Bitwise XOR `^`

    XOR means **Exclusive OR**.

    ### Rule

    | A | B | A ^ B |
    | - | - | ----- |
    | 0 | 0 | 0     |
    | 0 | 1 | 1     |
    | 1 | 0 | 1     |
    | 1 | 1 | 0     |

    👉 **Different → 1**

    👉 **Same → 0**

    ### Example

    ```python
    print(12 ^ 10)   # 6
    ```

    ```text
    12 = 1100
    10 = 1010
        ----
        0110 = 6
    ```

    Another:

    ```python
    print(15 ^ 7)    # 8
    ```

    ```text
    15 = 1111
    7 = 0111
        ----
        1000 = 8
    ```

    ---

    # 6. Bitwise NOT `~`

    This one is slightly different.

    ```python
    print(~12)   # -13
    print(~10)   # -11
    ```

    The important Python rule is:

    ```text
    ~n = -(n + 1)
    ```

    Therefore:

    ```text
    ~12 = -(12 + 1) = -13
    ~10 = -(10 + 1) = -11
    ```

    So:

    ```python
    ~12   # -13
    ~10   # -11
    ```

    ### Why?

    Python represents negative integers using **two's complement** conceptually.

    For example, for `12`:

    ```text
    12 = 00001100
    ```

    Invert every bit:

    ```text
    ~12

    00001100
    11110011
    ```

    Interpreting that as a signed two's-complement integer gives:

    ```text
    -13
    ```

    That's why `~12` becomes `-13`.

    ---

    # Quick Cheat Sheet

    | Operator | Name        | Main Idea                              |
    | -------- | ----------- | -------------------------------------- |
    | `&`      | AND         | Both bits must be `1`                  |
    | `\|`     | OR          | At least one bit is `1`                |
    | `^`      | XOR         | Bits must be different                 |
    | `~`      | NOT         | Inverts every bit                      |
    | `<<`     | Left Shift  | Multiply by `2ⁿ` for positive integers |
    | `>>`     | Right Shift | Divide by `2ⁿ` for positive integers   |

    ---

    ## Complete Examples

    ```python
    # Right Shift
    print(8 >> 1)   # 4
    print(8 >> 2)   # 2
    print(8 >> 3)   # 1

    # Left Shift
    print(4 << 1)   # 8
    print(4 << 2)   # 16
    print(4 << 3)   # 32

    # AND
    print(12 & 10)  # 8
    print(15 & 7)   # 7

    # OR
    print(12 | 10)  # 14
    print(15 | 7)   # 15

    # XOR
    print(12 ^ 10)  # 6
    print(15 ^ 7)   # 8

    # NOT
    print(~12)      # -13
    print(~10)      # -11
    ```

    ---
    ## Easy Way to Remember

    ```text
    &  → 1 if both are 1
    |  → 1 if at least one is 1
    ^  → 1 if they are different
    ~  → Inverts the bits

    << → Shifts left  → × 2ⁿ
    >> → Shifts right → ÷ 2ⁿ
    ```


```

"""
print(8 >> 1)   # 4 (8 divided by 2^1 = 4)
print(8 >> 2)   # 2 (8 divided by 2^2 = 2)
print(8 >> 3)   # 1 (8 divided by 2^3 = 1)

# Left shift examples
print(4 << 1)   # 8 (4 multiplied by 2^1 = 8)
print(4 << 2)   # 16 (4 multiplied by 2^2 = 16)
print(4 << 3)   # 32 (4 multiplied by 2^3 = 32)

# Bitwise AND examples
print(12 & 10)  # 8 (1100 & 1010 = 1000)
print(15 & 7)   # 7 (1111 & 0111 = 0111)

# Bitwise OR examples
print(12 | 10)  # 14 (1100 | 1010 = 1110)
print(15 | 7)   # 15 (1111 | 0111 = 1111)

# Bitwise XOR examples
print(12 ^ 10)  # 6 (1100 ^ 1010 = 0110)
print(15 ^ 7)   # 8 (1111 ^ 0111 = 1000)

# Bitwise NOT examples
print(~12)      # -13 (bitwise NOT of 12)
print(~10)      # -11 (bitwise NOT of 10)