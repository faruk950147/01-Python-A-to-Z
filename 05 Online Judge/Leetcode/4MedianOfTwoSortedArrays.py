# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



from typing import List

# Binary Search
# Time Complexity: O(log(min(n, m))) where n and m are the lengths of the two arrays.
# Space Complexity: O(1)
#it efficiently finds the median of two sorted arrays by performing a binary search on the smaller array.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # small array-in binary search 
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

        raise ValueError("Arrays are not sorted properly.")

if __name__ == "__main__":
    # Example usage
    nums1 = [1, 3]
    nums2 = [2]
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.0



# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         # Merge the arrays into a single sorted array.
#         merged = nums1 + nums2

#         # Sort the merged array.
#         merged.sort()

#         # Calculate the total number of elements in the merged array.
#         total = len(merged)

#         if total % 2 == 1:
#             # If the total number of elements is odd, return the middle element as the median.
#             return float(merged[total // 2])
#         else:
#             # If the total number of elements is even, calculate the average of the two middle elements as the median.
#             middle1 = merged[total // 2 - 1]
#             middle2 = merged[total // 2]
#             return (float(middle1) + float(middle2)) / 2.0
        
# if __name__ == "__main__":
#     # Example usage
#     nums1 = [1, 3]
#     nums2 = [2]
#     solution = Solution()
#     print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.0