"""
en(fruits) - 1 means:

Take the total number of items in the fruits list, then minus 1.

Why is it used?

In Python, indexing starts from 0, so:

First item → index 0
Last item → index len(fruits) - 1

Here:

len(fruits) = 4
Last index = 3
len(fruits) - 1 = 4 - 1 = 3 # this is the last index of the list
"""

def dynamic_last_element(fruits):
    # fruits[index] thats mean list of index?
    # fruits → list
    # [index] → list index we want which item
    # len(fruits) - 1 → last index
    # fruits[len(fruits) - 1] → last item
    # return fruits[len(fruits) - 1] → return last item
    # why fruits[len(fruits) - 1]? this inside of dynamic
    if len(fruits) > 0:
        # This is the index of the last element.
        # len(fruits) - 1
        # This index is used to access the last element.
        return fruits[len(fruits) - 1]

    return None


print(dynamic_last_element(["apple", "banana", "cherry", "Orange", "Mango", "Grape"]))
