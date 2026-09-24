"""
We can implement the basic idea of map()
using a Higher-Order Function.
"""
def maps(callback, arr):
    result = []

    for i in range(len(arr)):
        # just value send to callback function that means is_even function is a predicate
        if callback(arr[i]): 
            result.append(arr[i])
    return result


def maps(callback, arr):

    result = []

    for value in arr:

        result.append(callback(value))

    return result


def square(x):

    return x * x


numbers = [1, 2, 3, 4, 5]

result = maps(square, numbers)

print(result)

# Output:
# [1, 4, 9, 16, 25]


"""
Here:

maps()
    -> Higher-Order Function

square()
    -> Callback Function
"""

