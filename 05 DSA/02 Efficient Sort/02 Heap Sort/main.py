'''
# Heap Sort

## 1. What is Heap Sort?

**Heap Sort** is a **comparison-based sorting algorithm** that uses a **Binary Heap** data structure.

Heap Sort works by:

1. Building a Heap from the array.
2. Selecting the largest or smallest element from the Heap.
3. Moving that element to its correct position.
4. Reducing the Heap size.
5. Repeating the process until the array is sorted.

The main idea is:

```text
Build Heap → Extract Maximum → Heapify → Repeat
```

For ascending order, we normally use a **Max Heap**.

---

# 2. What is a Heap?

A **Heap** is a special type of **Complete Binary Tree**.

There are two main types:

### Max Heap

In a Max Heap:

```text
Parent >= Children
```

Example:

```text
        50
       /  \
     30    40
    / \    /
   10 20  35
```

The largest element is always at the root.

```text
Maximum = 50
```

### Min Heap

In a Min Heap:

```text
Parent <= Children
```

Example:

```text
        10
       /  \
     20    15
    / \    /
   30 40  25
```

The smallest element is always at the root.

```text
Minimum = 10
```

---

# 3. Why Heap Sort Uses Heap?

Suppose we want to sort an array in ascending order.

We need the largest element first.

A **Max Heap** always keeps the largest element at the root.

For example:

```text
        90
       /  \
     50    70
    / \    /
   20 30  60
```

The maximum element:

```text
90
```

is always at the root.

So we can:

```text
Take maximum
     ↓
Put it at the end
     ↓
Reduce heap size
     ↓
Heapify again
```

---

# 4. Array Representation of Heap

A Heap is usually stored in an **array**, not using separate tree nodes.

Consider:

```text
        50
       /  \
     30    40
    / \    /
   10 20  35
```

Array representation:

```text
[50, 30, 40, 10, 20, 35]
```

For an element at index `i`:

### Left Child

```text
2 * i + 1
```

### Right Child

```text
2 * i + 2
```

### Parent

```text
(i - 1) // 2
```

---

# 5. Example of Array Index

Consider:

```text
arr = [50, 30, 40, 10, 20, 35]
```

Index:

```text
        50(0)
       /     \
   30(1)    40(2)
   /  \      /
10(3) 20(4) 35(5)
```

For index `0`:

```text
Left Child  = 2(0) + 1 = 1
Right Child = 2(0) + 2 = 2
```

For index `1`:

```text
Left Child  = 2(1) + 1 = 3
Right Child = 2(1) + 2 = 4
```

For index `2`:

```text
Left Child  = 2(2) + 1 = 5
Right Child = 2(2) + 2 = 6
```

---

# 6. Heap Sort Basic Idea

Consider:

```text
[4, 10, 3, 5, 1]
```

First, build a Max Heap.

```text
        10
       /  \
      5    3
     / \
    4   1
```

Array:

```text
[10, 5, 3, 4, 1]
```

The largest element is now at index `0`.

```text
10
```

Swap it with the last element:

```text
[1, 5, 3, 4, 10]
```

Now `10` is in its final position.

Heapify the remaining part:

```text
[5, 4, 3, 1, 10]
```

Again, move the maximum to the end:

```text
[1, 4, 3, 5, 10]
```

Continue until the array becomes:

```text
[1, 3, 4, 5, 10]
```

---

# 7. Heap Sort Steps

Heap Sort has two major phases.

### Phase 1 — Build Max Heap

Convert the array into a Max Heap.

```text
Array
  ↓
Build Max Heap
  ↓
Max Heap
```

### Phase 2 — Extract Maximum

Repeatedly:

```text
Swap root with last element
        ↓
Reduce heap size
        ↓
Heapify
        ↓
Repeat
```

---

# 8. Build Max Heap

Consider:

```text
[4, 10, 3, 5, 1]
```

We need to convert it into a Max Heap.

Initial tree:

```text
        4
       / \
     10   3
    / \
   5   1
```

This is not a Max Heap because:

```text
10 > 4
```

After heapifying:

```text
        10
       /  \
      5    3
     / \
    4   1
```

Array:

```text
[10, 5, 3, 4, 1]
```

Now it is a Max Heap.

---

# 9. What is Heapify?

**Heapify** is the process of restoring the Heap property.

For a Max Heap:

```text
Parent >= Children
```

Suppose:

```text
        4
       / \
      10  3
```

This violates Max Heap property.

Compare:

```text
4 vs 10 vs 3
```

Largest is:

```text
10
```

Swap:

```text
        10
       /  \
      4    3
```

Now the Heap property is restored.

---

# 10. Heapify Example

Suppose:

```text
arr = [4, 10, 3, 5, 1]
```

Consider index:

```text
i = 0
```

Current value:

```text
4
```

Children:

```text
Left  = 10
Right = 3
```

Largest:

```text
10
```

So swap:

```text
[10, 4, 3, 5, 1]
```

But now we need to check the new position of `4`.

Its children are:

```text
5
1
```

Since:

```text
5 > 4
```

swap again:

```text
[10, 5, 3, 4, 1]
```

Now the Max Heap is:

```text
        10
       /  \
      5    3
     / \
    4   1
```

---

# 11. Heap Sort Example

Consider:

```text
[4, 10, 3, 5, 1]
```

### Step 1 — Build Max Heap

```text
[10, 5, 3, 4, 1]
```

### Step 2 — Swap root with last element

```text
[1, 5, 3, 4, 10]
```

`10` is now fixed.

Heapify remaining part:

```text
[5, 4, 3, 1, 10]
```

### Step 3

Swap root with last element of heap:

```text
[1, 4, 3, 5, 10]
```

Heapify:

```text
[4, 1, 3, 5, 10]
```

### Step 4

Swap:

```text
[3, 1, 4, 5, 10]
```

Heapify:

```text
[3, 1, 4, 5, 10]
```

Continue.

Final result:

```text
[1, 3, 4, 5, 10]
```

---

# 12. Heap Sort Pseudocode

```text
HeapSort(arr):

    n = length(arr)

    Build Max Heap

    for i = n/2 - 1 down to 0:
        Heapify(arr, n, i)

    for i = n - 1 down to 1:

        swap arr[0] and arr[i]

        Heapify(arr, i, 0)
```

---

# 13. Heapify Pseudocode

```text
Heapify(arr, n, i):

    largest = i

    left = 2 * i + 1

    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:

        swap arr[i] and arr[largest]

        Heapify(arr, n, largest)
```

---

# 14. Python Implementation

```python
class HeapSort:

    def heap_sort(self, arr):

        n = len(arr)

        # Build Max Heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Extract elements one by one
        for i in range(n - 1, 0, -1):

            # Move current maximum to the end
            arr[0], arr[i] = arr[i], arr[0]

            # Heapify the reduced heap
            self.heapify(arr, i, 0)


    def heapify(self, arr, n, i):

        # Assume current node is largest
        largest = i

        # Calculate child indexes
        left = 2 * i + 1
        right = 2 * i + 2

        # Check left child
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check right child
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If current node is not largest
        if largest != i:

            # Swap
            arr[i], arr[largest] = arr[largest], arr[i]

            # Recursively heapify affected subtree
            self.heapify(arr, n, largest)


if __name__ == "__main__":

    heap_sort = HeapSort()

    arr = [4, 10, 3, 5, 1]

    print(f"Original array: {arr}")

    heap_sort.heap_sort(arr)

    print(f"Heap Sort result: {arr}")
```

---

# 15. Output

```text
Original array:
[4, 10, 3, 5, 1]

Heap Sort result:
[1, 3, 4, 5, 10]
```

---

# 16. Understanding the Code

The first important part is:

```python
n = len(arr)
```

This gives the number of elements.

Then:

```python
for i in range(n // 2 - 1, -1, -1):
```

This loop starts from the last **non-leaf node** and moves toward the root.

Why?

Because leaf nodes are already valid heaps.

Then:

```python
self.heapify(arr, n, i)
```

restores the Max Heap property.

---

# 17. Why `n // 2 - 1`?

For an array of size `n`, the last non-leaf node is:

```text
n // 2 - 1
```

For example:

```text
n = 5
```

Then:

```text
5 // 2 - 1 = 1
```

So we start from:

```text
index = 1
```

and move:

```text
1 → 0
```

---

# 18. Extract Maximum

After building the Max Heap:

```text
[10, 5, 3, 4, 1]
```

The maximum is at:

```text
arr[0]
```

So:

```python
arr[0], arr[i] = arr[i], arr[0]
```

moves the maximum to the end.

For example:

```text
[10, 5, 3, 4, 1]
```

After swapping:

```text
[1, 5, 3, 4, 10]
```

Now:

```text
10
```

is in its final position.

---

# 19. Why Heap Size Decreases?

After placing `10` at the end:

```text
[1, 5, 3, 4, 10]
```

We don't need to touch `10` anymore.

So the active Heap is:

```text
[1, 5, 3, 4]
```

That's why:

```python
self.heapify(arr, i, 0)
```

uses `i` as the Heap size.

---

# 20. Time Complexity

Heap Sort has:

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | **O(n log n)**  |
| Average Case | **O(n log n)**  |
| Worst Case   | **O(n log n)**  |

One important advantage of Heap Sort is that the worst-case performance is still:

```text
O(n log n)
```

---

# 21. Why O(n log n)?

There are two major operations:

### Building the Heap

```text
O(n)
```

### Extracting elements

There are `n` elements.

Each extraction requires heapify:

```text
O(log n)
```

Therefore:

```text
n × O(log n)
```

So:

```text
O(n log n)
```

Overall:

```text
O(n) + O(n log n)
```

Therefore:

```text
O(n log n)
```

---

# 22. Space Complexity

Heap Sort can be implemented with constant extra space.

```text
Space Complexity = O(1)
```

The recursive `heapify()` implementation uses recursion stack, so the actual stack usage can be `O(log n)`.

An iterative heapify implementation can achieve:

```text
O(1)
```

auxiliary space.

---

# 23. Is Heap Sort Stable?

**No.**

Standard Heap Sort is **not stable**.

Equal elements may change their original relative order.

---

# 24. Is Heap Sort In-Place?

**Yes.**

Heap Sort can sort the array in-place.

It does not require an additional array of size `n`.

```text
Space Complexity = O(1)
```

for an iterative in-place implementation.

---

# 25. Advantages of Heap Sort

* Guaranteed **O(n log n)** worst-case time.
* In-place sorting is possible.
* Requires very little extra memory.
* Good for memory-constrained applications.
* Does not suffer from Quick Sort's `O(n²)` worst-case time.
* Uses a well-defined Heap data structure.

---

# 26. Disadvantages of Heap Sort

* Not stable.
* Usually has worse cache performance than some other sorting algorithms.
* More complicated than simple sorting algorithms.
* Often slower in practice than well-implemented Quick Sort.
* Heap operations can make the implementation harder to understand initially.

---

# 27. Heap Sort vs Quick Sort

| Feature              | Heap Sort  | Quick Sort    |
| -------------------- | ---------- | ------------- |
| Best                 | O(n log n) | O(n log n)    |
| Average              | O(n log n) | O(n log n)    |
| Worst                | O(n log n) | O(n²)         |
| Space                | O(1)*      | O(log n) avg. |
| Stable               | No         | No            |
| In-place             | Yes        | Usually Yes   |
| Main Concept         | Heap       | Partition     |
| Worst-case Guarantee | Yes        | No            |

`*` For iterative in-place implementation.

---

# 28. Heap Sort vs Merge Sort

| Feature      | Heap Sort  | Merge Sort |
| ------------ | ---------- | ---------- |
| Best         | O(n log n) | O(n log n) |
| Average      | O(n log n) | O(n log n) |
| Worst        | O(n log n) | O(n log n) |
| Space        | O(1)*      | O(n)       |
| Stable       | No         | Yes        |
| In-place     | Yes        | No*        |
| Main Concept | Heap       | Merge      |

`*` Depends on implementation.

---

# 29. Heap Sort vs Selection Sort

| Feature    | Heap Sort  | Selection Sort |
| ---------- | ---------- | -------------- |
| Best       | O(n log n) | O(n²)          |
| Average    | O(n log n) | O(n²)          |
| Worst      | O(n log n) | O(n²)          |
| Space      | O(1)*      | O(1)           |
| Stable     | No         | No*            |
| In-place   | Yes        | Yes            |
| Large Data | Good       | Poor           |

`*` Standard implementations.

---

# 30. Important Heap Concept

Remember these formulas:

```text
Left Child  = 2 * i + 1

Right Child = 2 * i + 2

Parent      = (i - 1) // 2
```

For Max Heap:

```text
Parent >= Children
```

For Min Heap:

```text
Parent <= Children
```

---

# 31. Important Code Pattern

For interviews, remember the main Heap Sort structure:

```python
def heap_sort(arr):

    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract maximum
    for i in range(n - 1, 0, -1):

        arr[0], arr[i] = arr[i], arr[0]

        heapify(arr, i, 0)
```

And the core `heapify()`:

```python
def heapify(arr, n, i):

    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:

        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)
```

These two functions are the **core of Heap Sort**.

---

# 32. Interview Questions

### Q1. What is Heap Sort?

Heap Sort is a comparison-based sorting algorithm that uses a Binary Heap to repeatedly select the maximum or minimum element.

### Q2. What data structure does Heap Sort use?

```text
Binary Heap
```

### Q3. What is the time complexity?

```text
Best    → O(n log n)
Average → O(n log n)
Worst   → O(n log n)
```

### Q4. What is the space complexity?

An iterative in-place implementation uses:

```text
O(1)
```

auxiliary space.

### Q5. Is Heap Sort stable?

```text
No
```

### Q6. Is Heap Sort in-place?

```text
Yes
```

### Q7. Which Heap is used for ascending order?

```text
Max Heap
```

### Q8. Which Heap is used for descending order?

```text
Min Heap
```

### Q9. What is the root of a Max Heap?

```text
Largest element
```

### Q10. What is the root of a Min Heap?

```text
Smallest element
```

### Q11. What is the left child index?

```text
2 * i + 1
```

### Q12. What is the right child index?

```text
2 * i + 2
```

### Q13. What is the parent index?

```text
(i - 1) // 2
```

### Q14. What is Heapify?

Heapify is the process of restoring the Heap property after an element is changed or moved.

### Q15. Why is Heap Sort O(n log n)?

Because building the heap takes `O(n)` and extracting `n` elements with `O(log n)` heapify operations gives `O(n log n)` overall.

---

# 33. Real-World Use Cases

Heap-based techniques are useful for:

* Priority Queues
* Scheduling systems
* Finding Top-K elements
* Finding K-th largest/smallest elements
* Priority-based processing
* Memory-sensitive sorting
* Algorithms such as Dijkstra's and Prim's algorithm

---

# 34. Final Summary

```text
Heap Sort
    │
    ├── Comparison-based Sorting
    │
    ├── Uses Binary Heap
    │
    ├── Build Max Heap
    │
    ├── Maximum at Root
    │
    ├── Swap Root with Last Element
    │
    ├── Reduce Heap Size
    │
    ├── Heapify
    │
    ├── Repeat
    │
    ├── Best Case    → O(n log n)
    ├── Average Case → O(n log n)
    ├── Worst Case   → O(n log n)
    │
    ├── Stable       → No
    └── In-place     → Yes
```

### One-line definition

**Heap Sort is a comparison-based sorting algorithm that builds a Heap and repeatedly extracts the maximum or minimum element to produce a sorted array.**

### Main formula to remember

```text
Build Heap → Extract Root → Heapify → Repeat
```

### Most Important Formulas

```text
Left Child  = 2 * i + 1

Right Child = 2 * i + 2

Parent      = (i - 1) // 2
```

### Quick Memory Trick

```text
Max Heap → Biggest at Root → Ascending Sort

Min Heap → Smallest at Root → Descending Sort
```

'''
