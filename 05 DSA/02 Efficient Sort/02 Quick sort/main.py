"""
    # Quick Sort

    ## 1. What is Quick Sort?

    **Quick Sort** is a **divide-and-conquer** sorting algorithm.

    It works by:

    1. Selecting an element as a **pivot**.
    2. Partitioning the array around the pivot.
    3. Putting smaller elements on the left side.
    4. Putting larger elements on the right side.
    5. Recursively sorting the left and right parts.

    The main idea is:

    ```text
    Choose Pivot → Partition → Recursively Sort
    ```

    ---

    # 2. Basic Idea

    Consider:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    Suppose we choose the last element as the pivot:

    ```text
    pivot = 4
    ```

    Now partition the array:

    ```text
    [3, 2]  4  [44, 38, 5, 15, 26, 27, 46]
            ↑
        Pivot
    ```

    The elements smaller than `4` go to the left.

    The elements larger than `4` go to the right.

    Then we recursively sort the left and right parts.

    ---

    # 3. Divide and Conquer

    Quick Sort follows the **Divide and Conquer** technique.

    ### Divide

    Choose a pivot and partition the array.

    ### Conquer

    Recursively sort the left and right parts.

    ### Combine

    No separate merge operation is required.

    After partitioning, the pivot is already in its correct position.

    ```text
            Array
            |
        Choose Pivot
            |
        Partition
        /      \
        Left     Right
        |          |
    Sort        Sort
        \          /
        Sorted Array
    ```

    ---

    # 4. What is a Pivot?

    A **pivot** is an element selected from the array that is used to partition the array.

    For example:

    ```text
    [8, 3, 7, 4, 9, 2]
    ```

    If:

    ```text
    pivot = 4
    ```

    Then after partitioning:

    ```text
    [3, 2]  4  [8, 7, 9]
    ```

    The rule is:

    ```text
    Left  → elements <= pivot
    Pivot → correct position
    Right → elements > pivot
    ```

    ---

    # 5. Pivot Selection

    There are several ways to select a pivot.

    ### First Element

    ```python
    pivot = arr[0]
    ```

    ### Last Element

    ```python
    pivot = arr[-1]
    ```

    ### Middle Element

    ```python
    pivot = arr[len(arr) // 2]
    ```

    ### Random Element

    A random element can also be selected as the pivot.

    For learning and interview practice, using the **last element as pivot** is simple and common.

    ---

    # 6. Partition

    The most important operation in Quick Sort is **Partition**.

    Consider:

    ```text
    [3, 7, 8, 5, 2, 4]
    ```

    Pivot:

    ```text
    4
    ```

    After partitioning:

    ```text
    [3, 2]  4  [7, 8, 5]
    ```

    The pivot `4` is now in its correct position.

    This operation is called **Partition**.

    ---

    # 7. Partition Example

    Given:

    ```text
    [3, 7, 8, 5, 2, 4]
    ```

    Pivot:

    ```text
    4
    ```

    Compare each element with the pivot.

    ```text
    3 < 4
    ```

    So `3` goes to the left.

    ```text
    7 > 4
    ```

    So `7` goes to the right.

    ```text
    8 > 4
    ```

    So `8` goes to the right.

    ```text
    5 > 4
    ```

    So `5` goes to the right.

    ```text
    2 < 4
    ```

    So `2` goes to the left.

    Final partition:

    ```text
    [3, 2]  4  [7, 8, 5]
    ```

    ---

    # 8. Quick Sort Example

    Given:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    Choose last element as pivot:

    ```text
    pivot = 4
    ```

    Partition:

    ```text
    [3, 2]  4  [44, 38, 5, 15, 26, 27, 46]
    ```

    Now sort the left side:

    ```text
    [3, 2]
    ```

    Choose:

    ```text
    pivot = 2
    ```

    Partition:

    ```text
    [] 2 [3]
    ```

    Result:

    ```text
    [2, 3]
    ```

    Now sort the right side:

    ```text
    [44, 38, 5, 15, 26, 27, 46]
    ```

    Choose:

    ```text
    pivot = 46
    ```

    All elements are smaller than `46`.

    So:

    ```text
    [44, 38, 5, 15, 26, 27] 46
    ```

    Continue recursively.

    Eventually:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 9. Quick Sort Pseudocode

    ```text
    QuickSort(arr, low, high):

        if low < high:

            pivot_index = Partition(arr, low, high)

            QuickSort(arr, low, pivot_index - 1)

            QuickSort(arr, pivot_index + 1, high)
    ```

    ### Partition Function

    ```text
    Partition(arr, low, high):

        pivot = arr[high]

        i = low - 1

        for j from low to high - 1:

            if arr[j] <= pivot:

                i++

                swap arr[i] and arr[j]

        swap arr[i + 1] and arr[high]

        return i + 1
    ```

    ---

    # 10. Python Implementation

    ```python
    class QuickSort:
        def __init__(self):
            pass

        def quick_sort(self, arr, low, high):

            # Base case
            if low < high:

                # Partition the array
                pivot_index = self.partition(arr, low, high)

                # Sort left side
                self.quick_sort(arr, low, pivot_index - 1)

                # Sort right side
                self.quick_sort(arr, pivot_index + 1, high)


        def partition(self, arr, low, high):

            # Choose last element as pivot
            pivot = arr[high]

            # Index of smaller element
            i = low - 1

            # Compare elements with pivot
            for j in range(low, high):

                if arr[j] <= pivot:

                    i += 1

                    # Swap
                    arr[i], arr[j] = arr[j], arr[i]

            # Put pivot in correct position
            arr[i + 1], arr[high] = arr[high], arr[i + 1]

            return i + 1


    if __name__ == "__main__":

        quick_sort = QuickSort()

        arr = [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

        print(f"Original array: {arr}")

        quick_sort.quick_sort(arr, 0, len(arr) - 1)

        print(f"Quick Sort result: {arr}")
    ```

    ---

    # 11. Output

    ```text
    Original array:
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

    Quick Sort result:
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 12. Understanding the Code

    The first important line is:

    ```python
    pivot = arr[high]
    ```

    Here, the last element is selected as the pivot.

    Then:

    ```python
    i = low - 1
    ```

    `i` keeps track of the boundary of elements that are smaller than or equal to the pivot.

    Then:

    ```python
    for j in range(low, high):
    ```

    `j` scans the array.

    If:

    ```python
    arr[j] <= pivot
    ```

    then the current element belongs to the left side.

    So:

    ```python
    i += 1
    ```

    Then swap:

    ```python
    arr[i], arr[j] = arr[j], arr[i]
    ```

    Finally, put the pivot in its correct position:

    ```python
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    ```

    Then return the pivot index:

    ```python
    return i + 1
    ```

    ---

    # 13. Understanding `i` and `j`

    This is one of the most important concepts in Quick Sort.

    ```text
    i → boundary of smaller elements
    j → current element being checked
    ```

    Conceptually:

    ```text
    [ elements <= pivot ][ elements > pivot ][ unknown ]
                        ↑                 ↑
                        i                 j
    ```

    `j` scans the array.

    When it finds an element smaller than or equal to the pivot, `i` moves forward and the elements are swapped.

    ---

    # 14. Time Complexity

    Quick Sort complexity depends on pivot selection.

    | Case         | Time Complexity |
    | ------------ | --------------- |
    | Best Case    | **O(n log n)**  |
    | Average Case | **O(n log n)**  |
    | Worst Case   | **O(n²)**       |

    ### Best Case

    If the pivot divides the array into approximately equal parts:

    ```text
            n
        / \
        n/2 n/2
    ```

    Then:

    ```text
    O(n log n)
    ```

    ### Worst Case

    If the pivot is always the smallest or largest element:

    ```text
    n
    \
    n-1
        \
        n-2
        \
            ...
    ```

    Then:

    ```text
    O(n²)
    ```

    ---

    # 15. Why Worst Case Can Be O(n²)?

    Consider:

    ```text
    [1, 2, 3, 4, 5, 6]
    ```

    If we always choose the last element as pivot:

    ```text
    pivot = 6
    ```

    Then:

    ```text
    [1, 2, 3, 4, 5] 6
    ```

    Again:

    ```text
    pivot = 5
    ```

    Then:

    ```text
    [1, 2, 3, 4] 5
    ```

    The partition becomes very unbalanced.

    Therefore:

    ```text
    O(n²)
    ```

    ---

    # 16. Space Complexity

    Quick Sort uses recursion stack memory.

    ### Average Case

    ```text
    O(log n)
    ```

    ### Worst Case

    ```text
    O(n)
    ```

    The exact space usage depends on the implementation and recursion behavior.

    ---

    # 17. Is Quick Sort Stable?

    **No.**

    Standard Quick Sort is generally **not stable**.

    If two elements have the same value, their original relative order may change.

    ---

    # 18. Is Quick Sort In-Place?

    Yes.

    Standard partition-based Quick Sort is generally considered **in-place** because it does not require an additional `O(n)` temporary array like the standard array implementation of Merge Sort.

    However, recursion stack memory is still required.

    ---

    # 19. Advantages of Quick Sort

    * Average time complexity is **O(n log n)**.
    * Usually fast in practice.
    * Can work in-place.
    * Does not require an additional array for merging.
    * Good for large arrays.
    * Uses divide-and-conquer.
    * Can have good cache performance.

    ---

    # 20. Disadvantages of Quick Sort

    * Worst-case time complexity is **O(n²)**.
    * Poor pivot selection can cause bad performance.
    * Standard Quick Sort is not stable.
    * Uses recursion.
    * Already sorted or reverse-sorted data can cause problems with naive pivot selection.

    ---

    # 21. Quick Sort vs Merge Sort

    | Feature      | Quick Sort       | Merge Sort       |
    | ------------ | ---------------- | ---------------- |
    | Best         | O(n log n)       | O(n log n)       |
    | Average      | O(n log n)       | O(n log n)       |
    | Worst        | O(n²)            | O(n log n)       |
    | Extra Array  | Usually No       | Yes              |
    | Stable       | No               | Yes              |
    | In-place     | Usually Yes      | No*              |
    | Approach     | Divide & Conquer | Divide & Conquer |
    | Main Concept | Partition        | Merge            |

    `*` Standard array implementation.

    ---

    # 22. Quick Sort vs Insertion Sort

    | Feature       | Quick Sort                        | Insertion Sort |
    | ------------- | --------------------------------- | -------------- |
    | Best          | O(n log n)                        | O(n)           |
    | Average       | O(n log n)                        | O(n²)          |
    | Worst         | O(n²)                             | O(n²)          |
    | Space         | O(log n) avg.                     | O(1)           |
    | Stable        | No                                | Yes            |
    | In-place      | Yes                               | Yes            |
    | Large Data    | Good                              | Poor           |
    | Nearly Sorted | Can be problematic with bad pivot | Excellent      |

    ---

    # 23. Important Quick Sort Concept

    Suppose:

    ```text
    Left  = [3, 15, 2]
    Pivot = 10
    Right = [20, 8]
    ```

    After partitioning:

    ```text
    [3, 2, 8] 10 [20, 15]
    ```

    The main rule is:

    ```text
    Left  → <= Pivot
    Pivot → Correct Position
    Right → > Pivot
    ```

    Then:

    ```text
    QuickSort(Left)
    QuickSort(Right)
    ```

    ---

    # 24. Important Code Pattern

    For interviews, remember:

    ```python
    def quick_sort(arr, low, high):

        if low < high:

            pivot_index = partition(arr, low, high)

            quick_sort(arr, low, pivot_index - 1)

            quick_sort(arr, pivot_index + 1, high)
    ```

    Partition pattern:

    ```python
    def partition(arr, low, high):

        pivot = arr[high]

        i = low - 1

        for j in range(low, high):

            if arr[j] <= pivot:

                i += 1

                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1
    ```

    These two functions are the **core of Quick Sort**.

    ---

    # 25. Interview Questions

    ### Q1. What is Quick Sort?

    Quick Sort is a **divide-and-conquer sorting algorithm** that selects a pivot, partitions the array around the pivot, and recursively sorts the two partitions.

    ### Q2. What is the average time complexity?

    ```text
    O(n log n)
    ```

    ### Q3. What is the worst-case time complexity?

    ```text
    O(n²)
    ```

    ### Q4. Why can Quick Sort become O(n²)?

    Because poor pivot selection can create highly unbalanced partitions.

    ### Q5. Is Quick Sort stable?

    ```text
    No
    ```

    ### Q6. Is Quick Sort in-place?

    ```text
    Usually Yes
    ```

    ### Q7. What is the main operation in Quick Sort?

    ```text
    Partition
    ```

    ### Q8. What is a pivot?

    A pivot is an element used to partition the array into smaller and larger elements.

    ### Q9. What happens after partition?

    The pivot is placed in its correct position, and the left and right parts are recursively sorted.

    ### Q10. Quick Sort vs Merge Sort — which has better worst-case complexity?

    ```text
    Merge Sort → O(n log n)
    Quick Sort → O(n²)
    ```

    So Merge Sort has the better worst-case guarantee.

    ---

    # 26. Real-World Use Cases

    Quick Sort can be useful for:

    * General-purpose sorting
    * Sorting large arrays
    * Memory-sensitive applications
    * Situations where in-place sorting is useful
    * Applications where average-case performance is important

    ---

    # 27. Final Summary

    ```text
    Quick Sort
        │
        ├── Divide and Conquer
        │
        ├── Choose Pivot
        │
        ├── Partition
        │   ├── Smaller → Left
        │   └── Larger  → Right
        │
        ├── Recursively Sort Left
        │
        ├── Recursively Sort Right
        │
        ├── Best Case    → O(n log n)
        ├── Average Case → O(n log n)
        ├── Worst Case   → O(n²)
        │
        ├── Stable       → No
        └── In-place     → Usually Yes
    ```

    ### One-line definition

    **Quick Sort is a divide-and-conquer sorting algorithm that selects a pivot, partitions the array around it, and recursively sorts the left and right parts.**

    ### Main formula to remember

    ```text
    Choose Pivot → Partition → Recursively Sort
    ```

"""

class QuickSort:
    def __init__(self):
        pass

    def quick_sort(self, arr, low, high):

        # Base case
        if low < high:

            # Partition the array
            pivot_index = self.partition(arr, low, high)

            # Sort left side
            self.quick_sort(arr, low, pivot_index - 1)

            # Sort right side
            self.quick_sort(arr, pivot_index + 1, high)


    def partition(self, arr, low, high):

        # Choose last element as pivot
        pivot = arr[high]

        # Index of smaller element
        i = low - 1

        # Compare elements with pivot
        for j in range(low, high):

            if arr[j] <= pivot:

                i += 1

                # Swap
                arr[i], arr[j] = arr[j], arr[i]

        # Put pivot in correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1


if __name__ == "__main__":

    quick_sort = QuickSort()

    arr = [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

    print(f"Original array: {arr}")

    quick_sort.quick_sort(arr, 0, len(arr) - 1)

    print(f"Quick Sort result: {arr}")