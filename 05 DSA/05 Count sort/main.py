"""
    # Counting Sort

    ## 1. What is Counting Sort?

    **Counting Sort** is a **non-comparison-based sorting algorithm**.

    Instead of comparing elements like:

    ```text
    3 < 44
    38 > 5
    ```

    Counting Sort counts how many times each value occurs and uses those counts to build the sorted array.

    ### Main idea

    ```text
    Count → Calculate Positions → Place Elements
    ```

    ---

    # 2. Basic Idea

    Given:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    Minimum value:

    ```text
    2
    ```

    Maximum value:

    ```text
    46
    ```

    So we create a count array covering the range:

    ```text
    2 → 46
    ```

    Then count how many times each number appears.

    For this array, every value appears once:

    ```text
    2  → 1
    3  → 1
    4  → 1
    5  → 1
    15 → 1
    26 → 1
    27 → 1
    38 → 1
    44 → 1
    46 → 1
    ```

    Finally, reconstruct the array in increasing order:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 3. How Counting Sort Works

    Counting Sort generally follows these steps:

    ### Step 1 — Find minimum and maximum

    ```python
    minimum = min(arr)
    maximum = max(arr)
    ```

    ### Step 2 — Create a count array

    The size is based on the value range:

    ```text
    maximum - minimum + 1
    ```

    ### Step 3 — Count occurrences

    For every element:

    ```text
    count[value] += 1
    ```

    ### Step 4 — Reconstruct the sorted array

    Visit the count array from left to right and write each value according to its frequency.

    ---

    # 4. Example

    Given:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    Minimum:

    ```text
    2
    ```

    Maximum:

    ```text
    46
    ```

    Range:

    ```text
    46 - 2 + 1 = 45
    ```

    So we need a count array of size `45`.

    Conceptually:

    ```text
    Value:  2  3  4  5  6  7 ... 15 ... 26 27 ... 38 ... 44 ... 46
    Count:  1  1  1  1  0  0 ...  1 ...  1  1 ...  1 ...  1 ...  1
    ```

    Then read the count array:

    ```text
    2
    3
    4
    5
    15
    26
    27
    38
    44
    46
    ```

    Final:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 5. Simple Counting Sort

    For non-negative integers, the basic version is:

    ```python
    def counting_sort(arr):
        maximum = max(arr)

        count = [0] * (maximum + 1)

        # Count each value
        for num in arr:
            count[num] += 1

        # Reconstruct sorted array
        result = []

        for value in range(len(count)):
            for _ in range(count[value]):
                result.append(value)

        return result


    arr = [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

    print("Original array:", arr)
    print("Sorted array:", counting_sort(arr))
    ```

    Output:

    ```text
    Original array:
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

    Sorted array:
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 6. Counting Array Example

    Take a smaller array:

    ```text
    [4, 2, 2, 8, 3, 3, 1]
    ```

    Maximum:

    ```text
    8
    ```

    Count array:

    ```text
    Index:  0 1 2 3 4 5 6 7 8
    Count:  0 1 2 2 1 0 0 0 1
    ```

    Meaning:

    ```text
    1 appears 1 time
    2 appears 2 times
    3 appears 2 times
    4 appears 1 time
    8 appears 1 time
    ```

    So:

    ```text
    [1, 2, 2, 3, 3, 4, 8]
    ```

    ---

    # 7. Counting Sort with Negative Numbers

    The simple implementation does not directly handle negative values.

    For example:

    ```text
    [-5, -2, 0, 3, -1, 2]
    ```

    We can solve this using the minimum value as an offset.

    The key formula is:

    ```text
    index = value - minimum
    ```

    Example:

    ```text
    minimum = -5
    ```

    For value `-5`:

    ```text
    -5 - (-5) = 0
    ```

    For value `-2`:

    ```text
    -2 - (-5) = 3
    ```

    For value `3`:

    ```text
    3 - (-5) = 8
    ```

    ---

    # 8. Python Counting Sort — Supports Negative Numbers

    ```python
    class CountingSort:

        def counting_sort(self, arr):
            if not arr:
                return arr

            minimum = min(arr)
            maximum = max(arr)

            # Create count array
            count = [0] * (maximum - minimum + 1)

            # Count occurrences
            for num in arr:
                count[num - minimum] += 1

            # Reconstruct sorted array
            result = []

            for i in range(len(count)):
                for _ in range(count[i]):
                    result.append(i + minimum)

            return result


    if __name__ == "__main__":
        counting_sort = CountingSort()

        arr = [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

        print("Original array:", arr)
        print("Counting Sort result:", counting_sort.counting_sort(arr))
    ```

    Output:

    ```text
    Original array:
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

    Counting Sort result:
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 9. Time Complexity

    Counting Sort has a different complexity from comparison-based sorting algorithms.

    Let:

    ```text
    n = number of elements
    k = range of values
    ```

    Then:

    ```text
    Time Complexity = O(n + k)
    ```

    ### Best Case

    ```text
    O(n + k)
    ```

    ### Average Case

    ```text
    O(n + k)
    ```

    ### Worst Case

    ```text
    O(n + k)
    ```

    This is one of the major advantages of Counting Sort.

    ---

    # 10. Space Complexity

    Counting Sort needs a count array.

    Therefore:

    ```text
    Space Complexity = O(n + k)
    ```

    Depending on the implementation, the output array may contribute `O(n)` additional space.

    ---

    # 11. Why is Counting Sort Fast?

    Comparison-based sorting algorithms such as:

    ```text
    Bubble Sort
    Selection Sort
    Insertion Sort
    Merge Sort
    Quick Sort
    ```

    generally determine order by comparing elements.

    Counting Sort avoids element-to-element comparisons.

    Instead:

    ```text
    Value → Count
    ```

    For a small range of integers, this can be extremely efficient.

    ---

    # 12. Important Condition

    Counting Sort works best when:

    ```text
    Range of values (k) is not very large.
    ```

    For example:

    ```text
    [2, 5, 1, 4, 3]
    ```

    Excellent.

    But consider:

    ```text
    [2, 1000000000]
    ```

    The range is enormous:

    ```text
    1,000,000,000 - 2 + 1
    ```

    Creating a count array that large would be highly inefficient.

    ---

    # 13. Counting Sort vs Merge Sort

    | Feature   | Counting Sort       | Merge Sort              |
    | --------- | ------------------- | ----------------------- |
    | Type      | Non-comparison      | Comparison              |
    | Best      | O(n + k)            | O(n log n)              |
    | Average   | O(n + k)            | O(n log n)              |
    | Worst     | O(n + k)            | O(n log n)              |
    | Space     | O(n + k)            | O(n)                    |
    | Stable    | Can be              | Yes                     |
    | Data Type | Mainly integers     | General comparable data |
    | Best For  | Small integer range | General large datasets  |

    ---

    # 14. Counting Sort vs Insertion Sort

    | Feature  | Counting Sort | Insertion Sort |
    | -------- | ------------- | -------------- |
    | Approach | Counting      | Comparison     |
    | Best     | O(n + k)      | O(n)           |
    | Average  | O(n + k)      | O(n²)          |
    | Worst    | O(n + k)      | O(n²)          |
    | Space    | O(n + k)      | O(1)           |
    | Stable   | Can be        | Yes            |
    | In-place | No            | Yes            |

    ---

    # 15. Counting Sort vs Selection Sort

    | Feature     | Counting Sort | Selection Sort |
    | ----------- | ------------- | -------------- |
    | Approach    | Counting      | Comparison     |
    | Best        | O(n + k)      | O(n²)          |
    | Average     | O(n + k)      | O(n²)          |
    | Worst       | O(n + k)      | O(n²)          |
    | Space       | O(n + k)      | O(1)           |
    | Stable      | Can be        | Usually No     |
    | Large Range | Poor          | Better         |

    ---

    # 16. Is Counting Sort Stable?

    **Counting Sort can be stable**, but the simple reconstruction version is not the typical stable implementation.

    A stable Counting Sort uses **cumulative counts** and places elements into an output array while processing the input in the appropriate order.

    This version is commonly used when Counting Sort is a subroutine of **Radix Sort**.

    ---

    # 17. Is Counting Sort In-Place?

    The standard implementation is:

    ```text
    No
    ```

    because it requires additional memory for the count array and often an output array.

    Typical space:

    ```text
    O(n + k)
    ```

    ---

    # 18. Advantages

    * Very fast when the value range is small.
    * `O(n + k)` time.
    * Does not use element comparisons.
    * Can be stable.
    * Useful as a subroutine in Radix Sort.
    * Simple for integer data with a limited range.

    ---

    # 19. Disadvantages

    * Mainly suitable for integer or discrete values.
    * Requires extra memory.
    * Can be inefficient when the value range is very large.
    * Not suitable for arbitrary objects without a suitable key/range representation.

    ---

    # 20. When Should You Use Counting Sort?

    Use Counting Sort when:

    * Data consists of integers.
    * The range of values is reasonably small.
    * You need very fast sorting.
    * Memory for a count array is available.
    * You are implementing Radix Sort.

    Example:

    ```text
    [4, 2, 2, 8, 3, 3, 1]
    ```

    Excellent candidate.

    ---

    # 21. When Should You NOT Use Counting Sort?

    Avoid it when:

    * Values have a huge range.
    * Data contains arbitrary objects.
    * Values are floating-point numbers without a suitable discrete key.
    * Memory is limited.

    Example:

    ```text
    [5, 1000000000]
    ```

    Counting Sort is a poor choice because the range is extremely large compared with `n`.

    ---

    # 22. Interview Questions

    ### Q1. What is Counting Sort?

    Counting Sort is a non-comparison sorting algorithm that sorts elements by counting the frequency of each value.

    ### Q2. What is its time complexity?

    ```text
    O(n + k)
    ```

    where `n` is the number of elements and `k` is the range of values.

    ### Q3. What is its space complexity?

    ```text
    O(n + k)
    ```

    depending on the implementation.

    ### Q4. Is Counting Sort a comparison-based algorithm?

    No.

    It is a **non-comparison-based** sorting algorithm.

    ### Q5. Can Counting Sort handle negative numbers?

    Yes, with an offset based on the minimum value.

    ### Q6. Is Counting Sort stable?

    It can be stable when implemented using cumulative counts and an output array.

    ### Q7. Is Counting Sort in-place?

    The standard implementation is not in-place.

    ### Q8. When is Counting Sort efficient?

    When the range `k` is relatively small compared with the number of elements `n`.

    ### Q9. What is the main disadvantage?

    It can require a large amount of memory when the value range is large.

    ### Q10. Is Counting Sort faster than Merge Sort?

    It can be, when `k` is small, because its complexity is `O(n + k)` instead of `O(n log n)`.

    ---

    # 23. Counting Sort Formula

    The most important formula is:

    ```text
    k = maximum - minimum + 1
    ```

    For your array:

    ```text
    maximum = 46
    minimum = 2

    k = 46 - 2 + 1
    = 45
    ```

    So the count array needs `45` positions.

    ---

    # 24. Key Concept

    Remember:

    ```text
    Counting Sort
        ↓
    Find min/max
        ↓
    Create count array
        ↓
    Count occurrences
        ↓
    Reconstruct sorted array
    ```

    ### One-line definition

    **Counting Sort sorts integer values by counting how many times each value occurs instead of comparing elements with one another.**

    ### Main formula

    ```text
    Time = O(n + k)
    Space = O(n + k)
    ```

    Where:

    ```text
    n = number of elements
    k = range of values
    ```

    ---

    # 25. Final Summary

    ```text
    Counting Sort
    │
    ├── Non-comparison based
    ├── Mainly for integers
    │
    ├── Find Minimum / Maximum
    ├── Create Count Array
    ├── Count Frequencies
    └── Reconstruct Sorted Array
    │
    ├── Best       → O(n + k)
    ├── Average    → O(n + k)
    ├── Worst      → O(n + k)
    │
    ├── Space      → O(n + k)
    ├── Stable     → Can be
    └── In-place   → No (standard)
    ```

    **Remember:**

    ```text
    Selection Sort → Select minimum
    Bubble Sort    → Swap adjacent elements
    Insertion Sort → Shift and insert
    Merge Sort     → Divide and merge
    Counting Sort  → Count frequencies
    ```

"""


