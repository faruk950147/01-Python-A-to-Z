
def lcm_of_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

nums = [4, 6, 8, 12]
print(lcm_of_list(nums)) # Output: 24


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18)) # Output: 6


def lcm(a, b):
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    gcd = x
    return a * b // gcd

print(lcm(12, 18)) # Output: 36

def gcd_of_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    return result

nums = [48, 18, 30]
print(gcd_of_list(nums)) # Output: 6


import math

def lcm_of_list(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = lcm * numbers[i] // math.gcd(lcm, numbers[i])
    return lcm

nums = [4, 6, 8, 12]
print(lcm_of_list(nums)) # Output: 24