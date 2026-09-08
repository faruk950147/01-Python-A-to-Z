# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))


from typing import List
class Solution:
    # using Type Hinting
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if first element is greater than target return empty list as there is no solution
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                # print(f"Found solution: {num} + {complement} = {target}")   
                return [lookup[complement], i]
            lookup[num] = i
            # print(f"Lookup after processing {num}: {lookup}")
        # if no solution found, return empty list
        return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print("Indices:", result)

"""
class Solution:
    # without Type Hinting
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i
        return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print("Indices:", result)
"""


# n = int(input("Enter a number: "))
# sum = 0 
# for i in range(1, n + 1):
#     sum += i
# print("The sum of the first", n, "numbers is:", sum)
# # The sum of the first n numbers is n(n + 1)/2  
