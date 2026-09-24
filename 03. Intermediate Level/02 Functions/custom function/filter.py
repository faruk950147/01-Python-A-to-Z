"""
The basic idea of Python's built-in filter()
can be implemented using a Higher-Order Function.
"""
def filter(arr, callback):
    result = []
    for i in range(len(arr)):
         # just value send to callback function that means is_even function is a predicate
        if callback(arr[i]): 
            result.append(arr[i])
    return result

def filter(arr, callback):

    result = []

    for value in arr:

        if callback(value):

            result.append(value)

    return result


def is_even(value):
    return value % 2 == 0

print(filter([1, 2, 3, 4, 5], is_even))

"""
Flow:

filter(numbers, is_even)
        |
        v
callback = is_even
        |
        v
Loop through numbers
        |
        v
is_even(value)
        |
        v
True / False
        |
        v
If True -> append value
        |
        v
Return result
"""
# Predicate Function

"""
A Predicate Function is a function that returns
a Boolean value.

Usually:

True
OR
False


Example:

def is_even(value):

    return value % 2 == 0


is_even(2)
    -> True

is_even(3)
    -> False


In our custom filter():

if callback(value):

the callback is expected to behave like
a predicate function.
"""
