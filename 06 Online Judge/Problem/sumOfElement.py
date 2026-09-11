"""
def sumOfElement(lst):
    if isinstance(lst, list):
        total = 0
        for item in range(len(lst)):
            if isinstance(lst[item], (int, float)):  # just int or float will be added
                total += lst[item]
            # non-number ignore 
        return total
    else:
        return "Please provide a list"

# Test
print(sumOfElement([1, 2, 3, 4, 5, "a"]))  # Output: 15
print(sumOfElement([1, 2.5, "hello", {"a":1}, (1,2), {1,2,3}, 3]))  # Output: 6.5


def sumOfElement2(lst):
    if isinstance(lst, list):
        total = 0
        for item in lst:
            if isinstance(item, (int, float)):  # just int or float will be added
                total += item
            # non-number ignore 
        return total
    else:
        return "Please provide a list"

# Test
print(sumOfElement2([1, 2, 3, 4, 5, "a"]))  # Output: 15
print(sumOfElement2([1, 2.5, "hello", {"a":1}, (1,2), {1,2,3}, 3]))  # Output: 6.5
"""

def sumOfElement(data):
    total = 0

    # if data int or float → add all
    if isinstance(data, (int, float)):
        return data

    # if data list, tuple or set → recursive call
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            total += sumOfElement(item)
        return total

    # ignore other types
    else:
        return 0

# Test examples
print(sumOfElement([1, 2, (3, 4), {5, 6}, 7]))                # Output: 28
print(sumOfElement([1, 2.5, "hello", {"a":1, "b":2}, (3, 2), {1,2,3}, 3]))  # Output: 17.5

