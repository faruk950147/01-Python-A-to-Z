class FindComplement:

    # efficient solution
    def find_complement(self, num):
        # first get num bit length
        bit_length = num.bit_length()

        # now get mask using bit_length
        mask = (1 << bit_length) - 1

        # now get complement using bitwise XOR
        return num ^ mask


    # less efficient solution or pythonic way
    def find_complement2(self, num):
        # convert binary string ('0b' remove)
        binary = bin(num)[2:]

        # using list comprehension complement create
        complement = ''.join(
            '1' if b == '0' else '0'
            for b in binary
        )

        # complement binary string to integer
        return int(complement, 2)


    # bad solution
    def find_complement3(self, num):
        binary = bin(num)[2:]
        complement = ''

        for b in binary:
            if b == '0':
                complement += '1'
            else:
                complement += '0'

        return int(complement, 2)


complement = FindComplement()

print(complement.find_complement(5))   # Output: 2

print(complement.find_complement2(5))  # Output: 2
print(complement.find_complement2(1))  # Output: 0
print(complement.find_complement2(10)) # Output: 5

print(complement.find_complement3(5))  # Output: 2

"""
    # Number Complement — Efficient Solution

    ## 1. Problem

    Given a positive integer `num`, find its **number complement**.

    To get the complement, flip every bit in its binary representation:

    ```text
    0 → 1
    1 → 0
    ```

    ### Example

    ```text
    num = 5

    Binary:
    5 = 101

    Complement:
    101 → 010

    010 = 2
    ```

    Therefore:

    ```text
    Answer = 2
    ```

    ---

    ## 2. Efficient Python Solution

    ```python
    def find_complement(self, num):
        # Get the number of bits
        bit_length = num.bit_length()

        # Create a mask containing all 1s
        mask = (1 << bit_length) - 1

        # Flip the bits using XOR
        return num ^ mask
    ```

    ---

    # 3. Step 1: Find Bit Length

    ```python
    bit_length = num.bit_length()
    ```

    `bit_length()` returns the number of bits required to represent an integer in binary, excluding leading zeros.

    ### Example

    ```python
    num = 5
    ```

    Binary representation:

    ```text
    5 = 101
    ```

    There are `3` bits.

    Therefore:

    ```python
    num.bit_length()
    ```

    returns:

    ```text
    3
    ```

    ---

    # 4. Step 2: Create the Mask

    ```python
    mask = (1 << bit_length) - 1
    ```

    Suppose:

    ```text
    bit_length = 3
    ```

    First:

    ```python
    1 << 3
    ```

    Binary:

    ```text
    0001 << 3
    ```

    Result:

    ```text
    1000
    ```

    Then subtract `1`:

    ```text
    1000
    -   1
    ----
    0111
    ```

    So:

    ```text
    mask = 111
    ```

    This mask contains `3` ones.

    ---

    # 5. Why Do We Need a Mask?

    Suppose:

    ```text
    num = 5
    binary = 101
    ```

    We need to flip every bit:

    ```text
    101 → 010
    ```

    For this, we create a mask containing all `1`s:

    ```text
    mask = 111
    ```

    Then use XOR:

    ```text
    101
    ^ 111
    -----
    010
    ```

    So the result is:

    ```text
    010 = 2
    ```

    ---

    # 6. XOR (`^`) Operator

    XOR compares two bits.

    | A | B | A ^ B |
    | - | - | ----- |
    | 0 | 0 | 0     |
    | 0 | 1 | 1     |
    | 1 | 0 | 1     |
    | 1 | 1 | 0     |

    The important rule is:

    ```text
    0 ^ 1 = 1
    1 ^ 1 = 0
    ```

    Therefore, XOR with `1` **flips a bit**.

    ```text
    0 → 1
    1 → 0
    ```

    That's why XOR with an all-`1` mask gives the complement.

    ---

    # 7. Complete Dry Run

    Suppose:

    ```python
    num = 5
    ```

    ### Step 1: Binary representation

    ```text
    5 = 101
    ```

    ### Step 2: Find bit length

    ```python
    bit_length = 5.bit_length()
    ```

    ```text
    bit_length = 3
    ```

    ### Step 3: Create mask

    ```python
    mask = (1 << 3) - 1
    ```

    ```text
    1 << 3 = 1000
    ```

    Therefore:

    ```text
    1000 - 1 = 0111
    ```

    So:

    ```text
    mask = 111
    ```

    ### Step 4: XOR

    ```text
    101
    ^ 111
    -----
    010
    ```

    ### Step 5: Convert to decimal

    ```text
    010 = 2
    ```

    Final answer:

    ```text
    2
    ```

    ---

    # 8. More Examples

    ## Example 1: `num = 10`

    Binary:

    ```text
    10 = 1010
    ```

    Mask:

    ```text
    1111
    ```

    XOR:

    ```text
    1010
    ^ 1111
    ------
    0101
    ```

    ```text
    0101 = 5
    ```

    Answer:

    ```text
    5
    ```

    ---

    ## Example 2: `num = 8`

    Binary:

    ```text
    8 = 1000
    ```

    Mask:

    ```text
    1111
    ```

    XOR:

    ```text
    1000
    ^ 1111
    ------
    0111
    ```

    ```text
    0111 = 7
    ```

    Answer:

    ```text
    7
    ```

    ---

    # 9. Understanding the Mask Formula

    The formula:

    ```python
    (1 << n) - 1
    ```

    creates a binary number containing exactly `n` ones.

    Examples:

    ```text
    (1 << 1) - 1 = 1      → 1
    (1 << 2) - 1 = 3      → 11
    (1 << 3) - 1 = 7      → 111
    (1 << 4) - 1 = 15     → 1111
    (1 << 5) - 1 = 31     → 11111
    ```

    Therefore:

    ```python
    mask = (1 << num.bit_length()) - 1
    ```

    creates the correct mask for `num`.

    ---

    # 10. Why Not Use `~num`?

    You might think:

    ```python
    ~num
    ```

    can directly flip all bits.

    However, Python uses an infinite-width two's-complement representation for integers.

    For example:

    ```python
    ~5
    ```

    returns:

    ```text
    -6
    ```

    But we need to flip only the bits belonging to the binary representation of `5`:

    ```text
    101 → 010
    ```

    which gives:

    ```text
    2
    ```

    Therefore, we use a mask:

    ```python
    num ^ mask
    ```

    ---

    # 11. Full Code

    ```python
    class Solution:
        def find_complement(self, num):
            # Find the number of bits
            bit_length = num.bit_length()

            # Create a mask of all 1s
            mask = (1 << bit_length) - 1

            # Flip the bits
            return num ^ mask
    ```

    ---

    # 12. Complexity

    Let `B` be the number of bits in `num`.

    ```text
    Time Complexity:  O(B)
    Space Complexity: O(1)
    ```

    The algorithm uses only a few integer variables and does not require extra data structures.

    ---

    # 13. Key Points to Remember

    ### Formula

    ```python
    mask = (1 << num.bit_length()) - 1
    ```

    ### Final operation

    ```python
    num ^ mask
    ```

    ### Overall idea

    ```text
    Number
    ↓
    Binary representation
    ↓
    Find bit length
    ↓
    Create all-1 mask
    ↓
    XOR
    ↓
    Number Complement
    ```

    ### One-line concept

    > **Number Complement = Number XOR All-1 Mask**

    ```python
    num ^ ((1 << num.bit_length()) - 1)
    ```

"""