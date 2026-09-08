# Using formula
def sumOfNumbers(n):
    return (n * (n + 1)) // 2
print(sumOfNumbers(5))

# Using loop
def sumOfNumbers(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

print(sumOfNumbers(5))

# Using arguments
def sumOfNumbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sumOfNumbers(1, 2, 3, 4, 5))

# Recursion function using
def sumOfNumbers(n):
    if n == 1:
        return 1
    return n + sumOfNumbers(n-1)
print(sumOfNumbers(5))


# sum of n numbers using list
def sum_of_n_nums(nums, elements):
    """
    Calculate the sum of n numbers.
    
    Args:
        nums (int): Number of elements.
        elements (list): List of elements.
        
    Returns:
        int: Sum of the elements.
    """
    sum = 0
    for i in range(nums):
        sum += elements[i]
    return sum

nums = int(input("How many numbers you want to operations: "))
elements = []
for i in range(nums):
    element = int(input("Enter a number: "))
    elements.append(element)
print(sum_of_n_nums(nums, elements))

