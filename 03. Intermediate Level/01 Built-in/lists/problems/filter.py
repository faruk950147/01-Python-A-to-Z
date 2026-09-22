# filter() takes two parameters:
# 1. function
# 2. iterable


# ============================================================
# Example 1: Filter even numbers using a normal function
# ============================================================

def is_even(num):
    return num % 2 == 0


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = filter(is_even, nums)

print(list(evens))


# ============================================================
# Example 2: Filter even numbers using lambda function
# ============================================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = filter(lambda num: num % 2 == 0, nums)

print(list(evens))



