"""
    # ======================= What is Collision in Python ========================

    A **collision** occurs when **two different objects or keys produce the same hash value**.

    Python uses **hashing** internally in data structures such as:

    * `dict`
    * `set`

    ## Simple Example

    Suppose:

    ```text
    hash("apple")  → 100
    hash("orange") → 100
    ```

    Here, `"apple"` and `"orange"` are different values, but they have the same hash value.

    This is called a **hash collision**.

    ## How it happens

    ```text
    Different Objects
        ↓
    Hash Function
        ↓
    Same Hash Value
        ↓
        Collision
    ```

    ## Important Point

    A collision **does not mean the two objects are equal**.

    ```python
    a == b
    ```

    and

    ```python
    hash(a) == hash(b)
    ```

    are different concepts.

    Python requires:

    ```text
    If a == b
        ↓
    hash(a) == hash(b)
    ```

    But the reverse is not necessarily true:

    ```text
    hash(a) == hash(b)
        ↓
    a may NOT be equal to b
    ```

    ## In Python Dictionary

    ```python
    data = {
        "name": "Faruk",
        "age": 25
    }
    ```

    Python uses the hash of the keys to efficiently find where the values are stored.

    If two keys have the same hash, Python has mechanisms to **handle the collision internally**.

    ## Short Definition

    > **Hash collision occurs when two different objects produce the same hash value.**

"""