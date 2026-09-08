"""
Reverse a list using recursion efficiently.

Logic:
1. Use two pointers: left and right.
2. Swap the elements at left and right.
3. Recursively move toward the center.
4. Stop when left >= right.
O(n) time complexity and O(n) space complexity due to recursion stack.
"""

def reverse_list(lst, left=0, right=None):

    # Set right pointer to the last index.
    if right is None:
        right = len(lst) - 1

    # Base case: stop when pointers meet or cross.
    if left >= right:
        return lst

    # Swap elements.
    lst[left], lst[right] = lst[right], lst[left]

    # Recursive call: move both pointers inward.
    return reverse_list(lst, left + 1, right - 1)




"""
Reverse a list using recursion. less efficient.

Logic:

1. If the list is empty, return an empty list.
2. Otherwise, take the last element of the list.
3. Recursively reverse the remaining elements.
4. Combine the last element with the reversed list.
O(n^2) time complexity and O(n^2) space complexity due to list concatenation and recursion stack.
"""

def reverse_list(lst):

    # Base case: stop recursion when the list is empty.
    if len(lst) == 0:
        return []

    # Recursive case:
    # Take the last element and combine it
    # with the reversed remaining list.
    else:
        return [lst[-1]] + reverse_list(lst[:-1])
print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]