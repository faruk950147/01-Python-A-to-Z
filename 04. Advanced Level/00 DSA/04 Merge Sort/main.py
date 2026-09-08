"""
    # Merge Sort

    ## 1. What is Merge Sort?

    **Merge Sort** is a **divide-and-conquer** sorting algorithm.

    It works by:

    1. Dividing the array into smaller parts.
    2. Recursively sorting those parts.
    3. Merging the sorted parts together.

    The main idea is:

    ```text
    Divide → Sort → Merge
    ```

    ---

    # 2. Basic Idea

    Consider:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    First, divide the array:

    ```text
    [3, 44, 38, 5, 15]    [26, 27, 2, 46, 4]
    ```

    Then divide again:

    ```text
    [3, 44] [38, 5, 15]    [26, 27] [2, 46, 4]
    ```

    Continue dividing until each part contains only one element.

    ```text
    [3] [44] [38] [5] [15] [26] [27] [2] [46] [4]
    ```

    A single element is already sorted.

    Then we **merge** the small sorted arrays.

    ---

    # 3. Divide and Conquer

    Merge Sort follows the **Divide and Conquer** technique.

    ### Divide

    Break the array into two halves.

    ### Conquer

    Recursively sort each half.

    ### Combine

    Merge the sorted halves.

    ```text
                Array
                |
            Divide
            /      \
        Left      Right
        |          |
        Divide     Divide
        / \        / \
        ...        ...
        \          /
            Merge
            |
        Sorted Array
    ```

    ---

    # 4. Example

    Given:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    ### Step 1 — Divide

    ```text
    [3, 44, 38, 5, 15] [26, 27, 2, 46, 4]
    ```

    ### Step 2 — Divide Again

    ```text
    [3, 44] [38, 5, 15]

    [26, 27] [2, 46, 4]
    ```

    ### Step 3 — Continue

    ```text
    [3] [44]

    [38] [5, 15]

    [26] [27]

    [2] [46, 4]
    ```

    Continue:

    ```text
    [5] [15]
    [46] [4]
    ```

    Now every part has one element.

    ---

    # 5. Start Merging

    Now we merge sorted arrays.

    ### Merge `[3]` and `[44]`

    Compare:

    ```text
    3 < 44
    ```

    Result:

    ```text
    [3, 44]
    ```

    ---

    ### Merge `[5]` and `[15]`

    ```text
    [5, 15]
    ```

    Now merge:

    ```text
    [38] + [5, 15]
    ```

    Compare:

    ```text
    38 vs 5 → 5
    38 vs 15 → 15
    38 remains → 38
    ```

    Result:

    ```text
    [5, 15, 38]
    ```

    Now merge:

    ```text
    [3, 44] + [5, 15, 38]
    ```

    Step by step:

    ```text
    3 < 5   → 3
    44 > 5  → 5
    44 > 15 → 15
    44 > 38 → 38
    44 remains → 44
    ```

    Result:

    ```text
    [3, 5, 15, 38, 44]
    ```

    ---

    # 6. Merge the Right Half

    Right side:

    ```text
    [26, 27, 2, 46, 4]
    ```

    First:

    ```text
    [26] + [27]
    ```

    Result:

    ```text
    [26, 27]
    ```

    Next:

    ```text
    [46] + [4]
    ```

    Result:

    ```text
    [4, 46]
    ```

    Now:

    ```text
    [2] + [4, 46]
    ```

    Result:

    ```text
    [2, 4, 46]
    ```

    Now merge:

    ```text
    [26, 27] + [2, 4, 46]
    ```

    Compare:

    ```text
    26 vs 2  → 2
    26 vs 4  → 4
    26 vs 46 → 26
    27 vs 46 → 27
    46 remains
    ```

    Result:

    ```text
    [2, 4, 26, 27, 46]
    ```

    ---

    # 7. Final Merge

    Now we have two sorted halves:

    ```text
    Left:
    [3, 5, 15, 38, 44]

    Right:
    [2, 4, 26, 27, 46]
    ```

    Merge them.

    ### Comparison

    ```text
    3 vs 2   → 2
    3 vs 4   → 3
    5 vs 4   → 4
    5 vs 26  → 5
    15 vs 26 → 15
    38 vs 26 → 26
    38 vs 27 → 27
    38 vs 46 → 38
    44 vs 46 → 44
    46 remains
    ```

    Final result:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 8. Merge Sort Pseudocode

    ```text
    MergeSort(arr):

        if length of arr <= 1:
            return arr

        mid = length(arr) / 2

        left = first half
        right = second half

        left = MergeSort(left)
        right = MergeSort(right)

        return Merge(left, right)
    ```

    ### Merge Function

    ```text
    Merge(left, right):

        create empty result

        while left and right are not empty:

            if left[0] <= right[0]:
                add left[0] to result
                remove left[0]

            else:
                add right[0] to result
                remove right[0]

        add remaining elements

        return result
    ```

    ---

    # 9. Python Implementation

    ```python
    class MergeSort:

        def merge_sort(self, arr):
            # Base case
            if len(arr) <= 1:
                return arr

            # Find middle
            mid = len(arr) // 2

            # Divide into two halves
            left = arr[:mid]
            right = arr[mid:]

            # Recursively sort both halves
            left = self.merge_sort(left)
            right = self.merge_sort(right)

            # Merge sorted halves
            return self.merge(left, right)

        def merge(self, left, right):
            result = []

            i = 0
            j = 0

            # Compare elements from both arrays
            while i < len(left) and j < len(right):

                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1

                else:
                    result.append(right[j])
                    j += 1

            # Add remaining elements from left
            while i < len(left):
                result.append(left[i])
                i += 1

            # Add remaining elements from right
            while j < len(right):
                result.append(right[j])
                j += 1

            return result


    if __name__ == "__main__":
        merge_sort = MergeSort()

        arr = [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

        print(f"Original array: {arr}")
        print(f"Merge Sort result: {merge_sort.merge_sort(arr)}")
    ```

    ---

    # 10. Output

    ```text
    Original array:
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

    Merge Sort result:
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 11. Time Complexity

    Merge Sort has:

    | Case         | Time Complexity |
    | ------------ | --------------- |
    | Best Case    | **O(n log n)**  |
    | Average Case | **O(n log n)**  |
    | Worst Case   | **O(n log n)**  |

    Unlike Bubble Sort and Insertion Sort, Merge Sort maintains **O(n log n)** performance even in the worst case.

    ---

    # 12. Why O(n log n)?

    There are two important parts.

    ### Division

    The array is repeatedly divided into halves.

    The number of levels is:

    ```text
    log₂(n)
    ```

    ### Merging

    At every level, all `n` elements are processed.

    Therefore:

    ```text
    n × log(n)
    ```

    So:

    ```text
    Time Complexity = O(n log n)
    ```

    ---

    # 13. Space Complexity

    The implementation above creates temporary arrays during merging.

    Therefore:

    ```text
    Space Complexity = O(n)
    ```

    So Merge Sort is **not in-place** in its standard array implementation.

    ---

    # 14. Is Merge Sort Stable?

    Yes.

    Merge Sort can be **stable**.

    The important condition is:

    ```python
    if left[i] <= right[j]:
    ```

    When two values are equal, the element from the left side is selected first, preserving their original relative order.

    ---

    # 15. Is Merge Sort In-Place?

    The standard implementation is:

    ```text
    No
    ```

    because it requires additional memory for merging.

    Typical space complexity:

    ```text
    O(n)
    ```

    There are specialized in-place Merge Sort implementations, but they are more complex and are not the standard approach.

    ---

    # 16. Advantages of Merge Sort

    * Guaranteed **O(n log n)** time.
    * Stable sorting algorithm.
    * Good for large datasets.
    * Uses divide-and-conquer.
    * Works well with linked lists.
    * Predictable performance.
    * Suitable for external sorting and large data that cannot fit entirely in memory.

    ---

    # 17. Disadvantages of Merge Sort

    * Requires additional memory.
    * Standard implementation uses **O(n)** extra space.
    * Usually more complicated than Insertion Sort or Bubble Sort.
    * For small arrays, simpler algorithms can sometimes be faster because of lower overhead.

    ---

    # 18. Merge Sort vs Selection Sort

    | Feature    | Merge Sort       | Selection Sort |
    | ---------- | ---------------- | -------------- |
    | Best       | O(n log n)       | O(n²)          |
    | Average    | O(n log n)       | O(n²)          |
    | Worst      | O(n log n)       | O(n²)          |
    | Space      | O(n)             | O(1)           |
    | Stable     | Yes              | No*            |
    | In-place   | No*              | Yes            |
    | Approach   | Divide & Conquer | Selection      |
    | Large Data | Excellent        | Poor           |

    `*` Standard implementations.

    ---

    # 19. Merge Sort vs Insertion Sort

    | Feature       | Merge Sort | Insertion Sort |
    | ------------- | ---------- | -------------- |
    | Best          | O(n log n) | O(n)           |
    | Average       | O(n log n) | O(n²)          |
    | Worst         | O(n log n) | O(n²)          |
    | Space         | O(n)       | O(1)           |
    | Stable        | Yes        | Yes            |
    | In-place      | No*        | Yes            |
    | Nearly Sorted | Good       | Excellent      |
    | Large Data    | Excellent  | Poor           |

    Insertion Sort is often better for **small or nearly sorted data**, while Merge Sort is much better for **large datasets**.

    ---

    # 20. Merge Sort vs Bubble Sort

    | Feature    | Merge Sort | Bubble Sort    |
    | ---------- | ---------- | -------------- |
    | Best       | O(n log n) | O(n) optimized |
    | Average    | O(n log n) | O(n²)          |
    | Worst      | O(n log n) | O(n²)          |
    | Space      | O(n)       | O(1)           |
    | Stable     | Yes        | Yes            |
    | Large Data | Excellent  | Poor           |

    ---

    # 21. Important Merge Concept

    Suppose:

    ```text
    Left  = [3, 15, 38]
    Right = [2, 5, 44]
    ```

    Compare the **first unused element** from each side:

    ```text
    3 vs 2 → 2
    3 vs 5 → 3
    15 vs 5 → 5
    15 vs 44 → 15
    38 vs 44 → 38
    44 remains → 44
    ```

    Result:

    ```text
    [2, 3, 5, 15, 38, 44]
    ```

    The key idea is:

    > **Both input arrays are already sorted, so we only need to compare their front elements.**

    ---

    # 22. Important Code Pattern

    For interviews, remember this structure:

    ```python
    def merge_sort(arr):

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)
    ```

    And the merge pattern:

    ```python
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    ```

    Then append the remaining elements.

    ---

    # 23. Interview Questions

    ### Q1. What is Merge Sort?

    Merge Sort is a divide-and-conquer sorting algorithm that recursively divides an array and then merges the sorted parts.

    ### Q2. What is its time complexity?

    ```text
    O(n log n)
    ```

    for best, average, and worst cases.

    ### Q3. What is its space complexity?

    Standard array implementation:

    ```text
    O(n)
    ```

    ### Q4. Is Merge Sort stable?

    Yes.

    ### Q5. Is Merge Sort in-place?

    Standard Merge Sort is not in-place.

    ### Q6. What technique does Merge Sort use?

    ```text
    Divide and Conquer
    ```

    ### Q7. What is the base case?

    ```python
    if len(arr) <= 1:
        return arr
    ```

    A single element is already sorted.

    ### Q8. Why is Merge Sort O(n log n)?

    Because there are approximately `log n` levels of division and `O(n)` work at each level for merging.

    ### Q9. Is Merge Sort better than Insertion Sort for large arrays?

    Yes. Merge Sort has `O(n log n)` average and worst-case complexity, while Insertion Sort has `O(n²)` average and worst-case complexity.

    ### Q10. Can Merge Sort be stable?

    Yes. Using `<=` when choosing between equal elements from the left and right halves preserves their relative order.

    ---

    # 24. Real-World Use Cases

    Merge Sort is useful for:

    * Large datasets.
    * External sorting.
    * Sorting linked lists.
    * Situations where stable sorting is required.
    * Applications requiring predictable `O(n log n)` performance.

    ---

    # 25. Final Summary

    ```text
    Merge Sort
    │
    ├── Divide and Conquer
    │
    ├── Divide
    │   └── Split array into halves
    │
    ├── Conquer
    │   └── Recursively sort each half
    │
    ├── Combine
    │   └── Merge sorted halves
    │
    ├── Best Case      → O(n log n)
    ├── Average Case   → O(n log n)
    ├── Worst Case     → O(n log n)
    │
    ├── Space          → O(n)
    ├── Stable         → Yes
    └── In-place       → No (standard implementation)
    ```

    ### One-line definition

    **Merge Sort repeatedly divides an array into smaller halves, sorts those halves recursively, and merges them back together to produce a sorted array.**

    ### Main formula to remember

    ```text
    Divide → Recursively Sort → Merge
    ```

"""



