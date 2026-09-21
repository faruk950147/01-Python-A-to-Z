"""

    # Python String

    ## What is a String?

    A **string** is a sequence (collection) of characters used to represent text in Python.

    ### Basic Syntax

    ```python
    name = "Python"
    ```

    Strings can be written using:

    ```python
    "Hello"
    'Hello'
    '''Hello'''
    ```

    ---

    ## Main Characteristics of String

    ### 1. Collection of Characters

    A string is a sequence of characters.

    ```python
    text = "Python"
    ```

    It contains:

    ```text
    P  y  t  h  o  n
    ```

    Each character has an index.

    ---

    ### 2. Ordered

    Strings are **ordered sequences**.

    The order of characters is preserved.

    ```python
    text = "Python"

    print(text[0])  # P
    print(text[1])  # y
    ```

    ---

    ### 3. Indexed

    Each character has an index starting from `0`.

    ```python
    text = "Python"

    print(text[0])   # P
    print(text[2])   # t
    print(text[-1])  # n
    ```

    ---

    ### 4. Immutable

    Strings are **immutable**, which means they cannot be changed after creation.

    ```python
    text = "Python"

    # text[0] = "J"   # TypeError
    ```

    You cannot directly modify an individual character.

    Instead, you create a **new string**:

    ```python
    text = "Python"

    text = "J" + text[1:]

    print(text)
    ```

    Output:

    ```text
    Jython
    ```

    ---

    ### 5. Duplicate Values Allowed

    A string can contain the same character multiple times.

    ```python
    text = "banana"
    ```

    Here, `a` and `n` appear multiple times.

    ---

    ### 6. Iterable

    A string can be traversed using a loop.

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

    ### 7. Supports Slicing

    Strings support slicing.

    ```python
    text = "Python"

    print(text[0:3])
    ```

    Output:

    ```text
    Pyt
    ```

    General syntax:

    ```python
    string[start:stop:step]
    ```

    ---

    ## Important Note

    The statement:

    > "Its items are always immutable"

    is better understood as follows:

    > A string itself is immutable, and its individual elements are characters represented as immutable string objects.

    For example:

    ```python
    text = "Python"

    # text[0] = "J"   # Not allowed
    ```

    ---

    ## One-Line Definition

    > **A string is an ordered, indexed, iterable, and immutable sequence of characters that allows duplicate characters.**

"""