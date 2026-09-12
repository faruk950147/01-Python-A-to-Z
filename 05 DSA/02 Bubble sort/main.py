"""
    # Bubble Sort

    ## 1. What is Bubble Sort?

    **Bubble Sort** is a simple, comparison-based, in-place sorting algorithm.

    It repeatedly compares **adjacent elements** and swaps them if they are in the wrong order.

    In ascending order, the **largest element gradually moves to the end** of the unsorted portion after each pass.

    This is why it is called **Bubble Sort** — larger elements "bubble" toward the end of the array.

    ### One-Line Definition

    > Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

    ---
    Important In Bubble Sort: Compare Adjacent Elements → Swap if Necessary → Repeat and Largest Element Moves Right

    # 2. Core Idea

    Bubble Sort works by comparing adjacent elements:

    ```text
    A[j] and A[j + 1]
    ```

    If:

    ```text
    A[j] > A[j + 1]
    ```

    then swap them.

    For ascending order:

    ```text
    Larger → moves right
    Smaller → moves left
    ```

    After every complete pass, the largest unsorted element reaches its correct position at the end.

    ---

    # 3. How Bubble Sort Works

    For ascending order:

    1. Start from the first element.
    2. Compare two adjacent elements.
    3. If the left element is greater than the right element, swap them.
    4. Move to the next pair.
    5. Continue until reaching the end of the unsorted portion.
    6. After one pass, the largest unsorted element is placed at the end.
    7. Repeat for the remaining unsorted portion.
    8. Continue until the array is sorted.

    ---

    # 4. Example Array

    We will use the same array throughout:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    Array size:

    ```text
    n = 10
    ```

    Maximum number of passes:

    ```text
    n - 1 = 9
    ```

    ---

    # 5. Pass 1

    Initial array:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    Compare adjacent elements.

    ### Comparison 1

    ```text
    3 and 44

    3 < 44
    → No swap
    ```

    Array:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    ### Comparison 2

    ```text
    44 and 38

    44 > 38
    → Swap
    ```

    ```text
    [3, 38, 44, 5, 15, 26, 27, 2, 46, 4]
    ```

    ### Comparison 3

    ```text
    44 and 5

    44 > 5
    → Swap
    ```

    ```text
    [3, 38, 5, 44, 15, 26, 27, 2, 46, 4]
    ```

    ### Comparison 4

    ```text
    44 and 15

    44 > 15
    → Swap
    ```

    ```text
    [3, 38, 5, 15, 44, 26, 27, 2, 46, 4]
    ```

    ### Comparison 5

    ```text
    44 and 26

    44 > 26
    → Swap
    ```

    ```text
    [3, 38, 5, 15, 26, 44, 27, 2, 46, 4]
    ```

    ### Comparison 6

    ```text
    44 and 27

    44 > 27
    → Swap
    ```

    ```text
    [3, 38, 5, 15, 26, 27, 44, 2, 46, 4]
    ```

    ### Comparison 7

    ```text
    44 and 2

    44 > 2
    → Swap
    ```

    ```text
    [3, 38, 5, 15, 26, 27, 2, 44, 46, 4]
    ```

    ### Comparison 8

    ```text
    44 and 46

    44 < 46
    → No swap
    ```

    ### Comparison 9

    ```text
    46 and 4

    46 > 4
    → Swap
    ```

    Result:

    ```text
    [3, 38, 5, 15, 26, 27, 2, 44, 4, 46]
    ```

    Largest element `46` is now in its correct position.

    Sorted portion:

    ```text
    [46]
    ```

    ---

    # 6. Pass 2

    Unsorted portion:

    ```text
    [3, 38, 5, 15, 26, 27, 2, 44, 4]
    ```

    Compare adjacent elements.

    ```text
    3 < 38
    → No swap
    ```

    ```text
    38 > 5
    → Swap

    [3, 5, 38, 15, 26, 27, 2, 44, 4, 46]
    ```

    ```text
    38 > 15
    → Swap

    [3, 5, 15, 38, 26, 27, 2, 44, 4, 46]
    ```

    ```text
    38 > 26
    → Swap

    [3, 5, 15, 26, 38, 27, 2, 44, 4, 46]
    ```

    ```text
    38 > 27
    → Swap

    [3, 5, 15, 26, 27, 38, 2, 44, 4, 46]
    ```

    ```text
    38 > 2
    → Swap

    [3, 5, 15, 26, 27, 2, 38, 44, 4, 46]
    ```

    ```text
    38 < 44
    → No swap
    ```

    ```text
    44 > 4
    → Swap

    [3, 5, 15, 26, 27, 2, 38, 4, 44, 46]
    ```

    Now `44` is in its correct position.

    ---

    # 7. Pass 3

    Start:

    ```text
    [3, 5, 15, 26, 27, 2, 38, 4, 44, 46]
    ```

    Comparisons:

    ```text
    3 < 5
    → No swap

    5 < 15
    → No swap

    15 < 26
    → No swap

    26 < 27
    → No swap

    27 > 2
    → Swap

    [3, 5, 15, 26, 2, 27, 38, 4, 44, 46]

    27 < 38
    → No swap

    38 > 4
    → Swap

    [3, 5, 15, 26, 2, 27, 4, 38, 44, 46]
    ```

    Now `38` is in its correct position.

    ---

    # 8. Pass 4

    Start:

    ```text
    [3, 5, 15, 26, 2, 27, 4, 38, 44, 46]
    ```

    Comparisons:

    ```text
    3 < 5
    → No swap

    5 < 15
    → No swap

    15 < 26
    → No swap

    26 > 2
    → Swap

    [3, 5, 15, 2, 26, 27, 4, 38, 44, 46]

    26 < 27
    → No swap

    27 > 4
    → Swap

    [3, 5, 15, 2, 26, 4, 27, 38, 44, 46]
    ```

    Now `27` is in its correct position.

    ---

    # 9. Pass 5

    Start:

    ```text
    [3, 5, 15, 2, 26, 4, 27, 38, 44, 46]
    ```

    Comparisons:

    ```text
    3 < 5
    → No swap

    5 < 15
    → No swap

    15 > 2
    → Swap

    [3, 5, 2, 15, 26, 4, 27, 38, 44, 46]

    15 < 26
    → No swap

    26 > 4
    → Swap

    [3, 5, 2, 15, 4, 26, 27, 38, 44, 46]
    ```

    Now `26` is in its correct position.

    ---

    # 10. Pass 6

    Start:

    ```text
    [3, 5, 2, 15, 4, 26, 27, 38, 44, 46]
    ```

    Comparisons:

    ```text
    3 < 5
    → No swap

    5 > 2
    → Swap

    [3, 2, 5, 15, 4, 26, 27, 38, 44, 46]

    5 < 15
    → No swap

    15 > 4
    → Swap

    [3, 2, 5, 4, 15, 26, 27, 38, 44, 46]
    ```

    Now `15` is in its correct position.

    ---

    # 11. Pass 7

    Start:

    ```text
    [3, 2, 5, 4, 15, 26, 27, 38, 44, 46]
    ```

    Comparisons:

    ```text
    3 > 2
    → Swap

    [2, 3, 5, 4, 15, 26, 27, 38, 44, 46]

    3 < 5
    → No swap

    5 > 4
    → Swap

    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    Now the array is sorted.

    ---

    # 12. Pass 8

    The array is already sorted:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    If using the **optimized Bubble Sort**, no swaps occur.

    Therefore, we can stop early.

    ```text
    No swaps → Array is already sorted
    ```

    So Pass 9 is not required in the optimized version.

    ---

    # 13. Final Sorted Array

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 14. Pass Summary

    | Pass | Largest Element Fixed | Array After Pass                       |
    | ---- | --------------------: | -------------------------------------- |
    | 1    |                    46 | `[3, 38, 5, 15, 26, 27, 2, 44, 4, 46]` |
    | 2    |                    44 | `[3, 5, 15, 26, 27, 2, 38, 4, 44, 46]` |
    | 3    |                    38 | `[3, 5, 15, 26, 2, 27, 4, 38, 44, 46]` |
    | 4    |                    27 | `[3, 5, 15, 2, 26, 4, 27, 38, 44, 46]` |
    | 5    |                    26 | `[3, 5, 2, 15, 4, 26, 27, 38, 44, 46]` |
    | 6    |                    15 | `[3, 2, 5, 4, 15, 26, 27, 38, 44, 46]` |
    | 7    |                     5 | `[2, 3, 4, 5, 15, 26, 27, 38, 44, 46]` |
    | 8    |               No swap | Already sorted                         |

    ---

    # 15. Pseudocode — Basic Bubble Sort

    ```text
    BUBBLE-SORT(A):

        n = length(A)

        for i = 0 to n - 2:

            for j = 0 to n - i - 2:

                if A[j] > A[j + 1]:

                    swap A[j] and A[j + 1]
    ```

    ---

    # 16. Python Implementation

    ```python
    class BubbleSort:
        def __init__(self):
            pass

        def bubble_sort(self, arr):
            n = len(arr)

            for i in range(n - 1):

                for j in range(n - i - 1):

                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

                print(f"After pass {i + 1}: {arr}")

            return arr


    if __name__ == "__main__":

        bubble_sort = BubbleSort()

        arr = [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

        print(f"Original array: {arr}")

        result = bubble_sort.bubble_sort(arr)

        print(f"Bubble Sort result: {result}")
    ```

    ---

    # 17. Optimized Bubble Sort

    The basic Bubble Sort always performs all possible passes.

    We can improve it by checking whether any swap occurred during a pass.

    If **no swap occurs**, the array is already sorted.

    Then we can stop early.

    ```python
    class BubbleSort:

        def __init__(self):
            pass

        def bubble_sort(self, arr):
            n = len(arr)

            for i in range(n - 1):

                swapped = False

                for j in range(n - i - 1):

                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True

                print(f"After pass {i + 1}: {arr}")

                if not swapped:
                    break

            return arr


    if __name__ == "__main__":

        bubble_sort = BubbleSort()

        arr = [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

        print(f"Original array: {arr}")

        result = bubble_sort.bubble_sort(arr)

        print(f"Bubble Sort result: {result}")
    ```

    ---

    # 18. Why Use `swapped`?

    Consider an already sorted array:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    During the first pass:

    ```text
    2 < 3
    3 < 4
    4 < 5
    ...
    44 < 46
    ```

    No elements need to be swapped.

    Therefore:

    ```text
    swapped = False
    ```

    This tells us:

    > The array is already sorted.

    So the algorithm can stop.

    This optimization improves the **best-case complexity from O(n²) to O(n)**.

    ---

    # 19. Time Complexity

    ## Basic Bubble Sort

    ### Best Case

    ```text
    O(n²)
    ```

    Without optimization, even an already sorted array still goes through all passes.

    ### Average Case

    ```text
    O(n²)
    ```

    ### Worst Case

    ```text
    O(n²)
    ```

    ---

    # 20. Optimized Bubble Sort Complexity

    With the `swapped` optimization:

    ### Best Case

    ```text
    O(n)
    ```

    If the array is already sorted, only one pass is needed.

    ### Average Case

    ```text
    O(n²)
    ```

    ### Worst Case

    ```text
    O(n²)
    ```

    ---

    # 21. Complexity Summary

    | Version               | Best  | Average | Worst |
    | --------------------- | ----- | ------- | ----- |
    | Basic Bubble Sort     | O(n²) | O(n²)   | O(n²) |
    | Optimized Bubble Sort | O(n)  | O(n²)   | O(n²) |

    ---

    # 22. Why is the Worst Case O(n²)?

    Consider a reverse-sorted array:

    ```text
    [46, 44, 38, 27, 26, 15, 5, 4, 3, 2]
    ```

    Almost every adjacent comparison requires a swap.

    The number of comparisons is approximately:

    ```text
    (n - 1) + (n - 2) + ... + 1
    ```

    Therefore:

    ```text
    n(n - 1) / 2
    ```

    So:

    ```text
    Worst Case = O(n²)
    ```

    ---

    # 23. Number of Comparisons

    For `n` elements:

    ```text
    Pass 1 → n - 1
    Pass 2 → n - 2
    Pass 3 → n - 3
    ...
    Last   → 1
    ```

    Total:

    ```text
    (n - 1) + (n - 2) + ... + 1
    ```

    Therefore:

    ```text
    Comparisons = n(n - 1) / 2
    ```

    For our array:

    ```text
    n = 10

    Comparisons
    = 10 × 9 / 2
    = 45
    ```

    So the maximum number of comparisons is:

    ```text
    45
    ```

    ---

    # 24. Space Complexity

    Bubble Sort sorts the array in-place.

    It only uses a few extra variables such as:

    ```text
    i
    j
    swapped
    temporary value during swapping
    ```

    Therefore:

    ```text
    Space Complexity = O(1)
    ```

    ---

    # 25. Stability

    Bubble Sort is **stable** by default.

    Why?

    It only swaps elements when:

    ```text
    A[j] > A[j + 1]
    ```

    It does not swap equal elements.

    Example:

    ```text
    [2a, 2b, 1]
    ```

    After sorting:

    ```text
    [1, 2a, 2b]
    ```

    The relative order of `2a` and `2b` remains unchanged.

    Therefore:

    ```text
    Bubble Sort = Stable
    ```

    ---

    # 26. In-Place

    Bubble Sort is an **in-place sorting algorithm**.

    It modifies the original array and does not require another array.

    Therefore:

    ```text
    Auxiliary Space = O(1)
    ```

    ---

    # 27. Ascending Order

    For ascending order:

    ```python
    if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    ```

    Larger elements move toward the right.

    Example:

    ```text
    [5, 3]
    ```

    Since:

    ```text
    5 > 3
    ```

    swap:

    ```text
    [3, 5]
    ```

    ---

    # 28. Descending Order

    For descending order, reverse the comparison:

    ```python
    if arr[j] < arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    ```

    Example:

    ```text
    [3, 5]
    ```

    Since:

    ```text
    3 < 5
    ```

    swap:

    ```text
    [5, 3]
    ```

    Final descending order for our array:

    ```text
    [46, 44, 38, 27, 26, 15, 5, 4, 3, 2]
    ```

    ---

    # 29. Advantages

    * Very easy to understand.
    * Very easy to implement.
    * Simple control flow.
    * In-place sorting algorithm.
    * Requires `O(1)` extra space.
    * Stable sorting algorithm.
    * Optimized version performs well on already sorted data.
    * Good for educational purposes.
    * Useful for understanding adjacent comparisons and swapping.

    ---

    # 30. Disadvantages

    * `O(n²)` average-case complexity.
    * `O(n²)` worst-case complexity.
    * Very slow for large datasets.
    * Performs many swaps in the worst case.
    * Not suitable for performance-sensitive applications.
    * Usually slower than efficient `O(n log n)` sorting algorithms.

    ---

    # 31. When to Use Bubble Sort

    Bubble Sort can be useful when:

    * The dataset is very small.
    * Simplicity is important.
    * You are learning sorting algorithms.
    * You need a stable in-place algorithm.
    * The data is already or nearly sorted and the optimized version is used.
    * You want to demonstrate adjacent comparisons and swapping.

    ---

    # 32. When NOT to Use Bubble Sort

    Avoid Bubble Sort when:

    * The dataset is large.
    * Performance is important.
    * You need efficient `O(n log n)` sorting.
    * The algorithm will run frequently on large arrays.
    * A better sorting algorithm is available.

    ---

    # 33. Better Alternatives

    ### Insertion Sort

    Good for:

    ```text
    Small or nearly sorted arrays
    ```

    Complexity:

    ```text
    Best    = O(n)
    Average = O(n²)
    Worst   = O(n²)
    ```

    ### Merge Sort

    ```text
    Best    = O(n log n)
    Average = O(n log n)
    Worst   = O(n log n)
    ```

    ### Quick Sort

    ```text
    Best    = O(n log n)
    Average = O(n log n)
    Worst   = O(n²)
    ```

    ### Heap Sort

    ```text
    Best    = O(n log n)
    Average = O(n log n)
    Worst   = O(n log n)
    ```

    ---

    # 34. Bubble Sort vs Selection Sort vs Insertion Sort

    | Feature       | Bubble Sort            | Selection Sort | Insertion Sort |
    | ------------- | ---------------------- | -------------- | -------------- |
    | Best          | O(n) optimized         | O(n²)          | O(n)           |
    | Average       | O(n²)                  | O(n²)          | O(n²)          |
    | Worst         | O(n²)                  | O(n²)          | O(n²)          |
    | Stable        | Yes                    | No             | Yes            |
    | In-place      | Yes                    | Yes            | Yes            |
    | Space         | O(1)                   | O(1)           | O(1)           |
    | Swaps         | Can be O(n²)           | At most n - 1  | Uses shifts    |
    | Nearly sorted | Good with optimization | Not ideal      | Excellent      |

    ---

    # 35. Bubble Sort vs Selection Sort

    ### Bubble Sort

    ```text
    Compare adjacent elements
            ↓
    Swap if necessary
            ↓
    Largest moves right
            ↓
    Repeat
    ```

    ### Selection Sort

    ```text
    Find minimum
        ↓
    Swap with first unsorted element
        ↓
    Sorted portion grows
        ↓
    Repeat
    ```

    Main difference:

    ```text
    Bubble Sort → Adjacent comparisons
    Selection Sort → Find minimum
    ```

    ---

    # 36. Bubble Sort vs Insertion Sort

    Bubble Sort:

    ```text
    Compare adjacent elements
    → Swap
    → Repeat
    ```

    Insertion Sort:

    ```text
    Take an element
    → Shift larger elements
    → Insert element
    ```

    For nearly sorted data, Insertion Sort is generally more efficient.

    ---

    # 37. Important Properties

    ```text
    Bubble Sort
    │
    ├── Comparison-based
    ├── In-place
    ├── Stable
    ├── Space = O(1)
    ├── Basic Best = O(n²)
    ├── Optimized Best = O(n)
    ├── Average = O(n²)
    ├── Worst = O(n²)
    └── Adjacent elements are compared
    ```

    ---

    # 38. Key Interview Questions

    ### Q1. What is Bubble Sort?

    Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

    ### Q2. Why is it called Bubble Sort?

    Because larger elements gradually "bubble" toward the end of the array in ascending order.

    ### Q3. What is the best-case complexity?

    Basic:

    ```text
    O(n²)
    ```

    Optimized:

    ```text
    O(n)
    ```

    ### Q4. What is the average-case complexity?

    ```text
    O(n²)
    ```

    ### Q5. What is the worst-case complexity?

    ```text
    O(n²)
    ```

    ### Q6. Is Bubble Sort stable?

    Yes.

    ### Q7. Is Bubble Sort in-place?

    Yes.

    ### Q8. What is its space complexity?

    ```text
    O(1)
    ```

    ### Q9. How does optimized Bubble Sort improve the algorithm?

    It stops early when a complete pass produces no swaps.

    ### Q10. How do you sort in descending order?

    Change:

    ```python
    arr[j] > arr[j + 1]
    ```

    to:

    ```python
    arr[j] < arr[j + 1]
    ```

    ### Q11. What is the main difference between Bubble Sort and Selection Sort?

    Bubble Sort repeatedly compares adjacent elements, while Selection Sort searches for the minimum element and swaps it into position.

    ---

    # 39. Easy Way to Remember

    Remember Bubble Sort like this:

    ```text
    COMPARE
    ↓
    ADJACENT ELEMENTS
    ↓
    WRONG ORDER?
    ↓
    SWAP
    ↓
    LARGEST BUBBLES RIGHT
    ↓
    REPEAT
    ```

    For ascending order:

    ```text
    Larger → Right
    Smaller → Left
    ```

    For descending order:

    ```text
    Smaller → Right
    Larger → Left
    ```

    ---

    # 40. Final Example

    Input:

    ```text
    [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]
    ```

    After Pass 1:

    ```text
    [3, 38, 5, 15, 26, 27, 2, 44, 4, 46]
    ```

    After Pass 2:

    ```text
    [3, 5, 15, 26, 27, 2, 38, 4, 44, 46]
    ```

    After Pass 3:

    ```text
    [3, 5, 15, 26, 2, 27, 4, 38, 44, 46]
    ```

    After Pass 4:

    ```text
    [3, 5, 15, 2, 26, 4, 27, 38, 44, 46]
    ```

    After Pass 5:

    ```text
    [3, 5, 2, 15, 4, 26, 27, 38, 44, 46]
    ```

    After Pass 6:

    ```text
    [3, 2, 5, 4, 15, 26, 27, 38, 44, 46]
    ```

    After Pass 7:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    Final:

    ```text
    [2, 3, 4, 5, 15, 26, 27, 38, 44, 46]
    ```

    ---

    # 41. Final Summary

    | Property       | Bubble Sort                        |
    | -------------- | ---------------------------------- |
    | Type           | Comparison-based                   |
    | Technique      | Adjacent comparison and swapping   |
    | Best Case      | O(n) optimized                     |
    | Average Case   | O(n²)                              |
    | Worst Case     | O(n²)                              |
    | Space          | O(1)                               |
    | In-place       | Yes                                |
    | Stable         | Yes                                |
    | Maximum Passes | n - 1                              |
    | Good for       | Small/nearly sorted data, learning |
    | Not good for   | Large datasets                     |

    ## Most Important Concept

    ```text
    Compare Adjacent Elements
            ↓
    Are They in Wrong Order?
            ↓
        Yes → Swap
            ↓
    Largest Element Moves Right
            ↓
    Repeat
    ```

    ## Most Important Formula

    ```text
    Maximum Comparisons = n(n - 1) / 2
    ```

    For `n = 10`:

    ```text
    10 × 9 / 2 = 45
    ```

    ### Final Takeaway

    > **Bubble Sort repeatedly compares adjacent elements and swaps them when they are in the wrong order. In ascending order, the largest unsorted element bubbles to the end after each pass. It is simple, stable, in-place, but generally inefficient for large datasets.**

"""



class BubbleSort:

    def __init__(self):
        pass

    def bubble_sort(self, arr):
        # Initialize the length of the array
        n = len(arr)

        # Iterate through the array
        for i in range(n - 1):
            # Initialize a flag to track if any swaps occurred during this pass
            swapped = False

            # Last i elements are already in place
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            print(f"After pass {i + 1}: {arr}")

            if not swapped:
                break

        return arr


if __name__ == "__main__":

    bubble_sort = BubbleSort()

    arr = [3, 44, 38, 5, 15, 26, 27, 2, 46, 4]

    print(f"Original array: {arr}")

    result = bubble_sort.bubble_sort(arr)

    print(f"Bubble Sort result: {result}")