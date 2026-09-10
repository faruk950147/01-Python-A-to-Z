"""
    # Selection Sort

    ## 1. What is Selection Sort?

    **Selection Sort** is a simple, comparison-based, in-place sorting algorithm.

    It repeatedly selects the **smallest element** from the unsorted part of the array and places it at the beginning of the unsorted part.

    For **ascending order**, Selection Sort selects the minimum element.

    For **descending order**, it selects the maximum element.

    ### One-Line Definition

    > Selection Sort repeatedly selects the minimum element from the unsorted portion and places it in its correct position.

    ---

    # 2. Core Idea

    The array is conceptually divided into two parts:

    ### Sorted Subarray

    Elements that are already in their correct positions.

    ### Unsorted Subarray

    Elements that still need to be processed.

    Initially:

    ```text
    Sorted:   []
    Unsorted: [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    After Pass 1:

    ```text
    Sorted:   [2]
    Unsorted: [44, 38, 5, 15, 26, 27, 3, 46, 4]
    ```

    After Pass 2:

    ```text
    Sorted:   [2, 3]
    Unsorted: [38, 5, 15, 26, 27, 44, 46, 4]
    ```

    The sorted portion grows by one position after every pass.

    ---

    # 3. How Selection Sort Works

    For every position `i`:

    1. Assume `arr[i]` is the minimum element.
    2. Store its index in `min_index`.
    3. Search the remaining unsorted elements.
    4. If a smaller element is found, update `min_index`.
    5. Swap `arr[i]` with `arr[min_index]`.
    6. Move to the next position.
    7. Repeat until the array is sorted.

    ---

    # 4. Example Array

    We will use the same array throughout these notes:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    Array size:

    ```text
    n = 10
    ```

    Therefore, number of passes:

    ```text
    n - 1 = 9
    ```

    ---

    # 5. Pass 1

    Initial array:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ↑
    i = 0
    ```

    Assume:

    ```text
    min_index = 0
    minimum = 3
    ```

    Now search the unsorted portion.

    ### Comparisons

    ```text
    44 < 3
    → No

    38 < 3
    → No

    5 < 3
    → No

    15 < 3
    → No

    26 < 3
    → No

    27 < 3
    → No

    2 < 3
    → min_index = 7

    46 < 2
    → No

    4 < 2
    → No
    ```

    Therefore:

    ```text
    Minimum = 2
    Minimum index = 7
    ```

    Swap:

    ```text
    3 ↔ 2
    ```

    Result:

    ```text
    [2, 44, 38, 5, 15, 26, 27, 3, 46, 4]
    ```

    Sorted part:

    ```text
    [2]
    ```

    ---

    # 6. Pass 2

    Sorted part:

    ```text
    [2]
    ```

    Unsorted part:

    ```text
    [44, 38, 5, 15, 26, 27, 3, 46, 4]
    ```

    Current position:

    ```text
    i = 1
    ```

    Assume:

    ```text
    min_index = 1
    minimum = 44
    ```

    ### Comparisons

    ```text
    38 < 44
    → min_index = 2

    5 < 38
    → min_index = 3

    15 < 5
    → No

    26 < 5
    → No

    27 < 5
    → No

    3 < 5
    → min_index = 7

    46 < 3
    → No

    4 < 3
    → No
    ```

    Therefore:

    ```text
    Minimum = 3
    Minimum index = 7
    ```

    Swap:

    ```text
    44 ↔ 3
    ```

    Result:

    ```text
    [2, 3, 38, 5, 15, 26, 27, 44, 46, 4]
    ```

    Sorted part:

    ```text
    [2, 3]
    ```

    ---

    # 7. Pass 3

    Sorted part:

    ```text
    [2, 3]
    ```

    Unsorted part:

    ```text
    [38, 5, 15, 26, 27, 44, 46, 4]
    ```

    Current position:

    ```text
    i = 2
    ```

    Assume:

    ```text
    min_index = 2
    minimum = 38
    ```

    ### Comparisons

    ```text
    5 < 38
    → min_index = 3

    15 < 5
    → No

    26 < 5
    → No

    27 < 5
    → No

    44 < 5
    → No

    46 < 5
    → No

    4 < 5
    → min_index = 9
    ```

    Therefore:

    ```text
    Minimum = 4
    Minimum index = 9
    ```

    Swap:

    ```text
    38 ↔ 4
    ```

    Result:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    ```

    Sorted part:

    ```text
    [2, 3, 4]
    ```

    ---

    # 8. Pass 4

    Sorted part:

    ```text
    [2, 3, 4]
    ```

    Unsorted part:

    ```text
    [5, 15, 26, 27, 44, 46, 38]
    ```

    Assume:

    ```text
    min_index = 3
    minimum = 5
    ```

    Compare:

    ```text
    15 < 5
    → No

    26 < 5
    → No

    27 < 5
    → No

    44 < 5
    → No

    46 < 5
    → No

    38 < 5
    → No
    ```

    `5` is already the minimum.

    No swap is required.

    Result:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    ```

    Sorted part:

    ```text
    [2, 3, 4, 5]
    ```

    ---

    # 9. Pass 5

    Sorted part:

    ```text
    [2, 3, 4, 5]
    ```

    Unsorted part:

    ```text
    [15, 26, 27, 44, 46, 38]
    ```

    Assume:

    ```text
    min_index = 4
    minimum = 15
    ```

    Compare:

    ```text
    26 < 15
    → No

    27 < 15
    → No

    44 < 15
    → No

    46 < 15
    → No

    38 < 15
    → No
    ```

    `15` is already the minimum.

    No swap.

    Result:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    ```

    ---

    # 10. Pass 6

    Sorted part:

    ```text
    [2, 3, 4, 5, 15]
    ```

    Unsorted part:

    ```text
    [26, 27, 44, 46, 38]
    ```

    Assume:

    ```text
    min_index = 5
    minimum = 26
    ```

    Compare:

    ```text
    27 < 26
    → No

    44 < 26
    → No

    46 < 26
    → No

    38 < 26
    → No
    ```

    `26` is already in the correct position.

    No swap.

    Result:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    ```

    ---

    # 11. Pass 7

    Sorted part:

    ```text
    [2, 3, 4, 5, 15, 26]
    ```

    Unsorted part:

    ```text
    [27, 44, 46, 38]
    ```

    Assume:

    ```text
    min_index = 6
    minimum = 27
    ```

    Compare:

    ```text
    44 < 27
    → No

    46 < 27
    → No

    38 < 27
    → No
    ```

    `27` is already in the correct position.

    No swap.

    Result:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    ```

    ---

    # 12. Pass 8

    Sorted part:

    ```text
    [2, 3, 4, 5, 15, 26, 27]
    ```

    Unsorted part:

    ```text
    [44, 46, 38]
    ```

    Assume:

    ```text
    min_index = 7
    minimum = 44
    ```

    Compare:

    ```text
    46 < 44
    → No

    38 < 44
    → min_index = 9
    ```

    Therefore:

    ```text
    Minimum = 38
    Minimum index = 9
    ```

    Swap:

    ```text
    44 ↔ 38
    ```

    Result:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 46, 44]
    ```

    ---

    # 13. Pass 9

    Sorted part:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38]
    ```

    Unsorted part:

    ```text
    [46, 44]
    ```

    Assume:

    ```text
    min_index = 8
    minimum = 46
    ```

    Compare:

    ```text
    44 < 46
    → min_index = 9
    ```

    Therefore:

    ```text
    Minimum = 44
    Minimum index = 9
    ```

    Swap:

    ```text
    46 ↔ 44
    ```

    Result:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 14. Final Sorted Array

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 15. Complete Pass Summary

    | Pass | Minimum | Index | Array After Pass                       |
    | ---- | ------: | ----: | -------------------------------------- |
    | 1    |       2 |     7 | `[2, 44, 38, 5, 15, 26, 27, 3, 46, 4]` |
    | 2    |       3 |     7 | `[2, 3, 38, 5, 15, 26, 27, 44, 46, 4]` |
    | 3    |       4 |     9 | `[2, 3, 4, 5, 15, 26, 27, 44, 46, 38]` |
    | 4    |       5 |     3 | `[2, 3, 4, 5, 15, 26, 27, 44, 46, 38]` |
    | 5    |      15 |     4 | `[2, 3, 4, 5, 15, 26, 27, 44, 46, 38]` |
    | 6    |      26 |     5 | `[2, 3, 4, 5, 15, 26, 27, 44, 46, 38]` |
    | 7    |      27 |     6 | `[2, 3, 4, 5, 15, 26, 27, 44, 46, 38]` |
    | 8    |      38 |     9 | `[2, 3, 4, 5, 15, 26, 27, 38, 46, 44]` |
    | 9    |      44 |     9 | `[2, 3, 4, 5, 15, 26, 27, 38, 44, 46]` |

    ---

    # 16. Pseudocode

    ```text
    SELECTION-SORT(A):

        n = length(A)

        for i = 0 to n - 2:

            min_index = i

            for j = i + 1 to n - 1:

                if A[j] < A[min_index]:

                    min_index = j

            if i != min_index:

                swap A[i] and A[min_index]
    ```

    ---

    # 17. Python Implementation
    class SelectionSort:
        def __init__(self):
            pass
        
        def selection_sort(self, arr):
            n = len(arr)
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if arr[j] < arr[i]:
                        arr[i], arr[j] = arr[j], arr[i]
                print(f"After pass {i + 1}: {arr}")
                
            return arr
            
    if __name__ == "__main__":  
        selection_sort = SelectionSort()
        arr = [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
        
    

    ```18. Selection Sort - Python Optimized
    class SelectionSort:

        def selection_sort(self, arr):
            n = len(arr)

            for i in range(n - 1):
                # Assume current position contains minimum
                min_index = i

                # Search minimum in the unsorted portion
                for j in range(i + 1, n):
                    if arr[j] < arr[min_index]:
                        min_index = j

                # Swap only if minimum is not already in place
                if i != min_index:
                    arr[i], arr[min_index] = arr[min_index], arr[i]

                print(f"After pass {i + 1}: {arr}")

            return arr


    if __name__ == "__main__":

        selection_sort = SelectionSort()

        arr = [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

        print(f"Original array: {arr}")

        result = selection_sort.selection_sort(arr)

        print(f"Selection Sort result: {result}")
    ```

    ---

    # 19. Output

    ```text
    Original array: [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

    After pass 1: [2, 44, 38, 5, 15, 26, 27, 3, 46, 4]
    After pass 2: [2, 3, 38, 5, 15, 26, 27, 44, 46, 4]
    After pass 3: [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    After pass 4: [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    After pass 5: [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    After pass 6: [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    After pass 7: [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    After pass 8: [2, 3, 4, 5, 15, 26, 27, 38, 46, 44]
    After pass 9: [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]

    Selection Sort result: [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 20. Number of Passes

    For an array containing `n` elements:

    ```text
    Number of passes = n - 1
    ```

    Our array:

    ```text
    n = 10
    ```

    Therefore:

    ```text
    10 - 1 = 9 passes
    ```

    ---

    # 21. Number of Comparisons

    For an array of `n` elements:

    ### Pass 1

    ```text
    n - 1
    ```

    ### Pass 2

    ```text
    n - 2
    ```

    ### Pass 3

    ```text
    n - 3
    ```

    ...

    ### Last Pass

    ```text
    1
    ```

    Therefore:

    ```text
    Total comparisons
    = (n - 1) + (n - 2) + ... + 2 + 1
    ```

    Formula:

    ```text
    n(n - 1) / 2
    ```

    For our array:

    ```text
    n = 10

    Comparisons
    = 10 × 9 / 2
    = 45
    ```

    Therefore:

    ```text
    Total comparisons = 45
    ```

    ---

    # 22. Time Complexity

    ## Best Case

    ```text
    O(n²)
    ```

    Even if the array is already sorted, Selection Sort still searches the entire unsorted portion.

    Example:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    It still performs:

    ```text
    9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
    = 45 comparisons
    ```

    Therefore:

    ```text
    Best Case = O(n²)
    ```

    ---

    ## Average Case

    ```text
    O(n²)
    ```

    Therefore:

    ```text
    Average Case = O(n²)
    ```

    ---

    ## Worst Case

    ```text
    O(n²)
    ```

    Therefore:

    ```text
    Worst Case = O(n²)
    ```

    ---

    # 23. Time Complexity Summary

    | Case         | Complexity |
    | ------------ | ---------- |
    | Best Case    | O(n²)      |
    | Average Case | O(n²)      |
    | Worst Case   | O(n²)      |

    ---

    # 24. Why is Best Case O(n²)?

    Selection Sort does not stop early.

    Even if the array is already sorted:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    It still searches every remaining element.

    Number of comparisons:

    ```text
    9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
    = 45
    ```

    Therefore:

    ```text
    Best Case = O(n²)
    ```

    ---

    # 25. Space Complexity

    Selection Sort is an **in-place sorting algorithm**.

    It does not require another array.

    It uses only a few extra variables:

    ```text
    i
    j
    min_index
    temporary value during swapping
    ```

    Therefore:

    ```text
    Space Complexity = O(1)
    ```

    ---

    # 26. Number of Swaps

    Selection Sort performs at most:

    ```text
    n - 1 swaps
    ```

    For our array:

    ```text
    n = 10

    Maximum swaps = 9
    ```

    However, the actual number of swaps depends on the input.

    Our example has swaps in:

    ```text
    Pass 1 → Swap
    Pass 2 → Swap
    Pass 3 → Swap
    Pass 4 → No swap
    Pass 5 → No swap
    Pass 6 → No swap
    Pass 7 → No swap
    Pass 8 → Swap
    Pass 9 → Swap
    ```

    Total:

    ```text
    5 swaps
    ```

    ---

    # 27. Stability

    Selection Sort is **not stable by default**.

    A sorting algorithm is stable if equal elements maintain their original relative order.

    Example:

    ```text
    [2a, 2b, 1]
    ```

    Initially:

    ```text
    2a comes before 2b
    ```

    Selection Sort finds `1` and swaps it with `2a`.

    Result:

    ```text
    [1, 2b, 2a]
    ```

    Now:

    ```text
    2b comes before 2a
    ```

    The relative order has changed.

    Therefore:

    ```text
    Selection Sort = Not Stable
    ```

    ---

    # 28. In-Place Sorting

    Selection Sort is an **in-place algorithm**.

    It modifies the original array instead of creating a separate array.

    Therefore:

    ```text
    Auxiliary Space = O(1)
    ```

    ---

    # 29. Descending Order

    For descending order, select the **maximum element** instead of the minimum.

    Example:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    First, find the maximum:

    ```text
    46
    ```

    Swap it with the first element:

    ```text
    [46, 44, 38, 5, 15, 26, 27, 2, 3, 4]
    ```

    Continue the same process.

    Final descending order:

    ```text
    [46, 44, 38, 27, 26, 15, 5, 4, 3, 2]
    ```

    ---

    # 29. Descending Order Condition

    Ascending:

    ```python
    if arr[j] < arr[min_index]:
        min_index = j
    ```

    Descending:

    ```python
    if arr[j] > arr[max_index]:
        max_index = j
    ```

    ---

    # 30. Advantages

    * Very easy to understand.
    * Very easy to implement.
    * Simple control flow.
    * In-place sorting algorithm.
    * Requires `O(1)` extra space.
    * Performs at most `n - 1` swaps.
    * Useful when swapping/writing data is expensive.
    * Good for educational purposes.
    * Does not require an additional array.

    ---

    # 31. Disadvantages

    * `O(n²)` time complexity in all cases.
    * Not efficient for large datasets.
    * Does not benefit significantly from an already sorted array.
    * Usually slower than `O(n log n)` algorithms.
    * Not stable by default.
    * Not suitable for performance-sensitive applications.

    ---

    # 32. When to Use Selection Sort

    Use Selection Sort when:

    * The dataset is very small.
    * Simplicity is important.
    * Memory is extremely limited.
    * `O(1)` extra space is required.
    * The number of swaps should be minimized.
    * You are learning sorting algorithms.
    * You need a simple in-place sorting algorithm.

    ---

    # 33. When NOT to Use Selection Sort

    Do not use Selection Sort when:

    * The dataset is large.
    * Performance is important.
    * You need `O(n log n)` performance.
    * Stable sorting is required.
    * The array is frequently updated.
    * A more efficient sorting algorithm is available.

    ---

    # 34. Better Alternatives

    For larger datasets, consider:

    ### Merge Sort

    ```text
    Best:    O(n log n)
    Average: O(n log n)
    Worst:   O(n log n)
    Stable:  Yes
    ```

    ### Quick Sort

    ```text
    Best:    O(n log n)
    Average: O(n log n)
    Worst:   O(n²)
    ```

    ### Heap Sort

    ```text
    Best:    O(n log n)
    Average: O(n log n)
    Worst:   O(n log n)
    Space:   O(1)
    ```

    ### Insertion Sort

    ```text
    Best:    O(n)
    Average: O(n²)
    Worst:   O(n²)
    ```

    Insertion Sort is especially good for **small or nearly sorted arrays**.

    ---

    # 35. Selection Sort vs Bubble Sort vs Insertion Sort

    | Feature       | Selection Sort | Bubble Sort    | Insertion Sort |
    | ------------- | -------------- | -------------- | -------------- |
    | Best          | O(n²)          | O(n) optimized | O(n)           |
    | Average       | O(n²)          | O(n²)          | O(n²)          |
    | Worst         | O(n²)          | O(n²)          | O(n²)          |
    | Stable        | No             | Yes            | Yes            |
    | In-place      | Yes            | Yes            | Yes            |
    | Extra Space   | O(1)           | O(1)           | O(1)           |
    | Maximum swaps | n - 1          | Can be O(n²)   | Uses shifts    |
    | Nearly sorted | Not ideal      | Can be good    | Excellent      |

    ---

    # 36. Selection Sort vs Bubble Sort

    ### Selection Sort

    ```text
    Find minimum
        ↓
    Swap
        ↓
    Next position
        ↓
    Repeat
    ```

    ### Bubble Sort

    ```text
    Compare adjacent elements
        ↓
    Swap if necessary
        ↓
    Repeat
    ```

    The major advantage of Selection Sort is that it performs at most:

    ```text
    n - 1 swaps
    ```

    while Bubble Sort can perform many more swaps.

    ---

    # 37. Selection Sort vs Insertion Sort

    ### Selection Sort

    ```text
    Find minimum → Swap
    ```

    ### Insertion Sort

    ```text
    Take element → Shift elements → Insert
    ```

    Insertion Sort is usually better for nearly sorted arrays because its best-case complexity is:

    ```text
    O(n)
    ```

    Selection Sort remains:

    ```text
    O(n²)
    ```

    ---

    # 38. Stable Selection Sort

    Standard Selection Sort is not stable.

    It can be modified to become stable.

    Instead of directly swapping the minimum element:

    ```text
    A[i] ↔ A[min_index]
    ```

    we can shift the elements between `i` and `min_index` one position to the right.

    Example:

    ```text
    [2a, 2b, 1]
    ```

    Stable result:

    ```text
    [1, 2a, 2b]
    ```

    The relative order of `2a` and `2b` is preserved.

    However, this requires additional shifting operations.

    ---

    # 39. Important Properties

    ```text
    Selection Sort
    │
    ├── Comparison-based
    ├── In-place
    ├── O(1) extra space
    ├── Best = O(n²)
    ├── Average = O(n²)
    ├── Worst = O(n²)
    ├── Not stable by default
    ├── Maximum swaps = n - 1
    └── Comparisons = n(n - 1)/2
    ```

    ---

    # 40. Interview Questions

    ### Q1. What is Selection Sort?

    Selection Sort repeatedly finds the minimum element from the unsorted portion and places it in its correct position.

    ### Q2. What is the best-case complexity?

    ```text
    O(n²)
    ```

    ### Q3. What is the average-case complexity?

    ```text
    O(n²)
    ```

    ### Q4. What is the worst-case complexity?

    ```text
    O(n²)
    ```

    ### Q5. Why is the best case O(n²)?

    Because Selection Sort still scans the entire unsorted portion even if the array is already sorted.

    ### Q6. Is Selection Sort stable?

    No. Standard Selection Sort is not stable.

    ### Q7. Is Selection Sort in-place?

    Yes.

    ```text
    Space = O(1)
    ```

    ### Q8. What is the maximum number of swaps?

    ```text
    n - 1
    ```

    ### Q9. How many comparisons are performed?

    ```text
    n(n - 1) / 2
    ```

    ### Q10. How many passes are required?

    ```text
    n - 1
    ```

    ### Q11. How do you sort in descending order?

    Find the maximum element instead of the minimum element.

    ### Q12. Is Selection Sort good for large datasets?

    No. Its `O(n²)` time complexity makes it inefficient for large datasets.

    ---

    # 41. Easy Way to Remember

    The name tells you the main idea:

    ```text
    SELECTION SORT
        ↓
    SELECT
        ↓
    Minimum
        ↓
    Put it in correct position
        ↓
    Repeat
    ```

    For ascending order:

    ```text
    SELECT MINIMUM → MOVE LEFT
    ```

    For descending order:

    ```text
    SELECT MAXIMUM → MOVE LEFT
    ```

    ---

    # 42. Final Example

    Input:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    After Pass 1:

    ```text
    [2, 44, 38, 5, 15, 26, 27, 3, 46, 4]
    ```

    After Pass 2:

    ```text
    [2, 3, 38, 5, 15, 26, 27, 44, 46, 4]
    ```

    After Pass 3:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    ```

    After Pass 4:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    ```

    After Pass 5:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    ```

    After Pass 6:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    ```

    After Pass 7:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 44, 46, 38]
    ```

    After Pass 8:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 46, 44]
    ```

    After Pass 9:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    Final:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 43. Final Summary

    | Property      | Selection Sort                           |
    | ------------- | ---------------------------------------- |
    | Type          | Comparison-based                         |
    | Technique     | Select minimum and swap                  |
    | Best Case     | O(n²)                                    |
    | Average Case  | O(n²)                                    |
    | Worst Case    | O(n²)                                    |
    | Space         | O(1)                                     |
    | In-place      | Yes                                      |
    | Stable        | No                                       |
    | Passes        | n - 1                                    |
    | Comparisons   | n(n - 1) / 2                             |
    | Maximum Swaps | n - 1                                    |
    | Good for      | Small datasets, learning, limited memory |
    | Not good for  | Large/performance-sensitive datasets     |

    ## Most Important Formula

    ```text
    Comparisons = n(n - 1) / 2
    ```

    For our array:

    ```text
    n = 10

    Comparisons = 10 × 9 / 2
                = 45
    ```

    ## Most Important Concept

    ```text
    Unsorted Array
        ↓
    Find Minimum
        ↓
    Swap with First Unsorted Element
        ↓
    Sorted Portion Grows
        ↓
    Repeat
    ```

    ### Final Takeaway

    > **Selection Sort repeatedly selects the smallest element from the unsorted portion and places it at the beginning of that portion. It is simple, in-place, and uses at most `n - 1` swaps, but it always takes `O(n²)` time.**

"""

class SelectionSort:

    def selection_sort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            # Assume current position contains minimum
            min_index = i

            # Search minimum in the unsorted portion
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Swap only if minimum is not already in place
            # (it's a good practice to avoid unnecessary swaps)
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]

            print(f"After pass {i + 1}: {arr}")

        return arr

if __name__ == "__main__":

    selection_sort = SelectionSort()

    arr = [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

    print(f"Original array: {arr}")

    result = selection_sort.selection_sort(arr)

    print(f"Selection Sort result: {result}")

  
