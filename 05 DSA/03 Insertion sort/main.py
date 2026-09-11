"""
    # Insertion Sort

    ## 1. What is Insertion Sort?

    **Insertion Sort** is a simple comparison-based sorting algorithm.

    It works similarly to the way we arrange **playing cards in our hand**.

    The array is divided into two parts:

    * **Sorted portion** → left side
    * **Unsorted portion** → right side

    At each step, we take one element from the unsorted portion and insert it into its correct position in the sorted portion.

    ---

    ## 2. Basic Idea

    Suppose we have:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    Initially:

    ```text
    Sorted:   [3]
    Unsorted: [44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    Take `44`.

    Since `44 > 3`, it stays after `3`.

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    Now take `38`.

    `38 < 44`, so shift `44` to the right and insert `38` before it:

    ```text
    [3, 38, 44, 5, 15, 26, 27, 2, 46, 4]
    ```

    This process continues until the entire array is sorted.

    ---

    ## 3. How Insertion Sort Works

    For every element:

    1. Select the current element as `key` is first element in array.
    2. Compare `key` with elements on its left.
    3. Shift larger elements one position to the right.
    4. Insert `key` into its correct position.
    5. Repeat until the array is sorted.

    ### Important terms

    ```text
    key
    ```

    The element currently being inserted.

    ```text
    j
    ```

    The index used to compare elements to the left of the key.

    ---

    # 4. Step-by-Step Example

    Given:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    ### Pass 1

    Key:

    ```text
    44
    ```

    Compare with `3`.

    ```text
    44 > 3
    ```

    No shifting is required.

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    ---

    ### Pass 2

    Key:

    ```text
    38
    ```

    Compare:

    ```text
    38 < 44
    ```

    Shift `44` right:

    ```text
    [3, 44, 44, 5, 15, 26, 27, 2, 46, 4]
    ```

    Now compare with `3`:

    ```text
    38 > 3
    ```

    Insert `38`:

    ```text
    [3, 38, 44, 5, 15, 26, 27, 2, 46, 4]
    ```

    ---

    ### Pass 3

    Key:

    ```text
    5
    ```

    Compare with `44`:

    ```text
    5 < 44
    ```

    Shift `44`.

    Compare with `38`:

    ```text
    5 < 38
    ```

    Shift `38`.

    Compare with `3`:

    ```text
    5 > 3
    ```

    Insert `5`:

    ```text
    [3, 5, 38, 44, 15, 26, 27, 2, 46, 4]
    ```

    ---

    ### Pass 4

    Key:

    ```text
    15
    ```

    Shift:

    ```text
    44 → right
    38 → right
    ```

    `15 > 5`, so insert after `5`.

    ```text
    [3, 5, 15, 38, 44, 26, 27, 2, 46, 4]
    ```

    ---

    ### Pass 5

    Key:

    ```text
    26
    ```

    `26 < 44` → shift

    `26 < 38` → shift

    `26 > 15` → stop

    Result:

    ```text
    [3, 5, 15, 26, 38, 44, 27, 2, 46, 4]
    ```

    ---

    ### Pass 6

    Key:

    ```text
    27
    ```

    `27 < 44` → shift

    `27 < 38` → shift

    `27 > 26` → stop

    Result:

    ```text
    [3, 5, 15, 26, 27, 38, 44, 2, 46, 4]
    ```

    ---

    ### Pass 7

    Key:

    ```text
    2
    ```

    `2 < 44` → shift

    `2 < 38` → shift

    `2 < 27` → shift

    `2 < 26` → shift

    `2 < 15` → shift

    `2 < 5` → shift

    `2 < 3` → shift

    Insert `2` at the beginning:

    ```text
    [2, 3, 5, 15, 26, 27, 38, 44, 46, 4]
    ```

    ---

    ### Pass 8

    Key:

    ```text
    46
    ```

    `46 > 44`

    So no shifting is required.

    ```text
    [2, 3, 5, 15, 26, 27, 38, 44, 46, 4]
    ```

    ---

    ### Pass 9

    Key:

    ```text
    4
    ```

    `4 < 46` → shift

    `4 < 44` → shift

    `4 < 38` → shift

    `4 < 27` → shift

    `4 < 26` → shift

    `4 < 15` → shift

    `4 < 5` → shift

    `4 > 3` → stop

    Insert `4`:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ### Final Sorted Array

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    # 5. Pseudocode

    ```text
    InsertionSort(arr):

        for i = 1 to n - 1:

            key = arr[i]
            j = i - 1

            while j >= 0 and arr[j] > key:

                arr[j + 1] = arr[j]
                j = j - 1

            arr[j + 1] = key
    ```

    ---

    # 6. Python Implementation

    ```python
    class InsertionSort:

        def insertion_sort(self, arr):
            n = len(arr)

            for i in range(1, n):
                key = arr[i]
                j = i - 1

                # Shift larger elements to the right
                while j >= 0 and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1

                # Insert key into its correct position
                arr[j + 1] = key

                print(f"After pass {i}: {arr}")

            return arr


    if __name__ == "__main__":
        insertion_sort = InsertionSort()

        arr = [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

        print(f"Original array: {arr}")
        print(f"Insertion Sort result: {insertion_sort.insertion_sort(arr)}")
    ```

    ---

    # 7. Output

    ```text
    Original array:
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

    After pass 1:
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

    After pass 2:
    [3, 38, 44, 5, 15, 26, 27, 2, 46, 4]

    After pass 3:
    [3, 5, 38, 44, 15, 26, 27, 2, 46, 4]

    After pass 4:
    [3, 5, 15, 38, 44, 26, 27, 2, 46, 4]

    After pass 5:
    [3, 5, 15, 26, 38, 44, 27, 2, 46, 4]

    After pass 6:
    [3, 5, 15, 26, 27, 38, 44, 2, 46, 4]

    After pass 7:
    [2, 3, 5, 15, 26, 27, 38, 44, 46, 4]

    After pass 8:
    [2, 3, 5, 15, 26, 27, 38, 44, 46, 4]

    After pass 9:
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]

    Insertion Sort result:
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 8. Time Complexity

    | Case         | Time Complexity |
    | ------------ | --------------- |
    | Best Case    | **O(n)**        |
    | Average Case | **O(n²)**       |
    | Worst Case   | **O(n²)**       |

    ### Best Case

    If the array is already sorted:

    ```text
    [1, 2, 3, 4, 5]
    ```

    Each element only needs one comparison.

    Therefore:

    ```text
    O(n)
    ```

    ### Worst Case

    If the array is reverse sorted:

    ```text
    [5, 4, 3, 2, 1]
    ```

    Almost every element must be shifted.

    Therefore:

    ```text
    O(n²)
    ```

    ---

    # 9. Space Complexity

    Insertion Sort requires only a few extra variables such as:

    ```python
    key
    j
    i
    ```

    Therefore:

    ```text
    Space Complexity = O(1)
    ```

    It is an **in-place sorting algorithm**.

    ---

    # 10. Is Insertion Sort Stable?

    Yes.

    **Insertion Sort is a stable sorting algorithm.**

    Equal elements maintain their original relative order because the condition normally uses:

    ```python
    arr[j] > key
    ```

    rather than:

    ```python
    arr[j] >= key
    ```

    ---

    # 11. Is Insertion Sort In-Place?

    Yes.

    Insertion Sort modifies the original array and does not require another array.

    ```text
    Space = O(1)
    ```

    ---

    # 12. Advantages

    * Simple to understand.
    * Easy to implement.
    * Requires **O(1)** extra space.
    * Stable sorting algorithm.
    * In-place algorithm.
    * Very efficient for small arrays.
    * Very efficient when data is already or almost sorted.
    * Can sort data while receiving elements one at a time.

    ---

    # 13. Disadvantages

    * Slow for large unsorted arrays.
    * Worst-case time complexity is **O(n²)**.
    * Not suitable for large datasets compared with efficient algorithms such as Merge Sort or Quick Sort.

    ---

    # 14. When Should You Use Insertion Sort?

    Insertion Sort is useful when:

    * The array is small.
    * The array is almost sorted.
    * You need a simple implementation.
    * Stability is important.
    * You want an in-place algorithm.
    * Data arrives gradually and needs to remain sorted.

    Example:

    ```text
    [1, 2, 3, 4, 5, 7, 6]
    ```

    Only a small amount of work is required to insert `6` into the correct position.

    ---

    # 15. When Should You NOT Use It?

    Avoid Insertion Sort when:

    * The dataset is very large.
    * The data is highly unsorted.
    * You need guaranteed efficient performance for large inputs.

    For those situations, consider:

    ```text
    Merge Sort
    Quick Sort
    Heap Sort
    ```

    ---

    # 16. Ascending Order

    The standard condition is:

    ```python
    while j >= 0 and arr[j] > key:
    ```

    This produces:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 17. Descending Order

    For descending order, change:

    ```python
    arr[j] > key
    ```

    to:

    ```python
    arr[j] < key
    ```

    Example:

    ```python
    class InsertionSort:

        def insertion_sort_descending(self, arr):
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1

                while j >= 0 and arr[j] < key:
                    arr[j + 1] = arr[j]
                    j -= 1

                arr[j + 1] = key

            return arr
    ```

    Output:

    ```text
    [46, 44, 38, 27, 26, 15, 5, 4, 3, 2]
    ```

    ---

    # 18. Insertion Sort vs Selection Sort vs Bubble Sort

    | Feature       | Insertion Sort | Selection Sort | Bubble Sort    |
    | ------------- | -------------- | -------------- | -------------- |
    | Best Case     | O(n)           | O(n²)          | O(n) optimized |
    | Average       | O(n²)          | O(n²)          | O(n²)          |
    | Worst         | O(n²)          | O(n²)          | O(n²)          |
    | Space         | O(1)           | O(1)           | O(1)           |
    | Stable        | Yes            | No*            | Yes            |
    | In-place      | Yes            | Yes            | Yes            |
    | Adaptive      | Yes            | No             | Yes*           |
    | Small Data    | Good           | Good           | Good           |
    | Nearly Sorted | Excellent      | Poor           | Good           |

    `*` Standard Selection Sort is not stable, and optimized Bubble Sort is adaptive.

    ---

    # 19. Key Difference: Insertion vs Selection

    ### Selection Sort

    Selection Sort searches for the minimum:

    ```text
    Find minimum → Swap
    ```

    ### Insertion Sort

    Insertion Sort takes the current element and places it correctly:

    ```text
    Take key → Shift → Insert
    ```

    For example:

    ```text
    Selection Sort:
    [3, 44, 38, 5]
    ↓
    Find minimum
    ↓
    Swap
    ```

    ```text
    Insertion Sort:
    [3, 44, 38, 5]
        ↓
        key
        ↓
    Shift larger elements
        ↓
    Insert key
    ```

    ---

    # 20. Key Difference: Insertion vs Bubble

    ### Bubble Sort

    Moves larger elements toward the end:

    ```text
    Compare → Swap → Compare → Swap
    ```

    ### Insertion Sort

    Moves larger elements to the right and inserts the key:

    ```text
    Select key → Shift → Insert
    ```

    Insertion Sort usually performs very well on **nearly sorted data**.

    ---

    # 21. Interview Questions

    ### Q1. What is Insertion Sort?

    Insertion Sort is a comparison-based sorting algorithm that builds the sorted array one element at a time.

    ### Q2. What is its best-case complexity?

    ```text
    O(n)
    ```

    When the array is already sorted.

    ### Q3. What is its worst-case complexity?

    ```text
    O(n²)
    ```

    When the array is reverse sorted.

    ### Q4. Is Insertion Sort stable?

    Yes.

    ### Q5. Is Insertion Sort in-place?

    Yes.

    ### Q6. What is its space complexity?

    ```text
    O(1)
    ```

    ### Q7. Why is Insertion Sort good for nearly sorted arrays?

    Because elements that are already close to their correct positions require very few shifts.

    ### Q8. Does Insertion Sort use swapping?

    The standard implementation does **not need swapping**.

    Instead, it uses:

    ```text
    Shifting + Insertion
    ```

    ### Q9. How many passes are required for n elements?

    ```text
    n - 1
    ```

    Because the first element is considered already sorted.

    ### Q10. What is the main idea of Insertion Sort?

    > Take one element at a time and insert it into the correct position in the already sorted portion.

    ---

    # 22. Important Code Pattern

    Remember this pattern for interviews:

    ```python
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    ```

    The most important three steps are:

    ```text
    1. key = arr[i]
    2. Shift larger elements
    3. arr[j + 1] = key
    ```

    ---

    # 23. Final Summary

    ```text
    Insertion Sort
    │
    ├── Comparison-based
    ├── In-place
    ├── Stable
    ├── Adaptive
    │
    ├── Best Case      → O(n)
    ├── Average Case   → O(n²)
    ├── Worst Case     → O(n²)
    │
    └── Space          → O(1)
    ```

    ### One-line definition

    **Insertion Sort builds the sorted portion of an array one element at a time by shifting larger elements and inserting the current element into its correct position.**

    ### Main formula to remember

    ```text
    Key → Compare → Shift → Insert
    ```

"""





