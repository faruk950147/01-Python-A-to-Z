"""You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]"
Explanation: There are three 0s that are moved to the end."""




class Solution:
    def pushZerosToEnd(self, arr):
        """
        Function to move all zeros in the array to the end
        while maintaining the relative order of non-zero elements.
        Operates in-place using efficient swapping.
        """
        pos = 0  # Index to place the next non-zero element
        for i in range(len(arr)):
            # If the current element is not equal to the target (0)
            if arr[i] != 0:
                # If the current index is not equal to the position index
                if i != pos:
                    # Swap current element with the position index
                    arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1
        return arr

sol = Solution()
print(sol.pushZerosToEnd([0, 1, 0, 3, 12])) 

class Solution:
    def pushZerosToEnd(self, arr, target):
        """
        Function to move all zeros in the array to the end
        while maintaining the relative order of non-zero elements.
        Operates in-place using efficient swapping.
        """
        pos = 0  # Index to place the next non-zero element
        for i in range(len(arr)):
            # If the current element is not equal to the target (0)
            if arr[i] != target:
                # If the current index is not equal to the position index
                if i != pos:
                    # Swap current element with the position index
                    arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1
        return arr  

sol = Solution()
print(sol.pushZerosToEnd([0, 1, 0, 3, 12], 0)) 

class Solution:
    def pushZerosToFront(self, arr, target=0):
        pos = len(arr) - 1
        for i in range(len(arr) - 1, -1, -1):
            # If the current element is not equal to the target (0)
            if arr[i] != target:
                # If the current index is not equal to the position index
                arr[pos] = arr[i]
                pos -= 1
        for i in range(pos, -1, -1):
            arr[i] = target
        return arr  

# Example
sol = Solution()
print(sol.pushZerosToFront([0, 1, 0, 3, 12]))  # Output: [0, 0, 1, 3, 12]

class Solution:
    def zerosInMiddle(self, arr, target=0):
        """
        Move all zeros (target) to the middle of the array,
        while keeping the relative order of non-zero elements.
        """
        # Non-target elements
        non_target = [x for x in arr if x != target]
        
        # Count how many zeros
        zeros_count = arr.count(target)
        
        # Calculate middle index of non-target elements
        mid = len(non_target) // 2
        
        # Insert zeros in the middle
        result = non_target[:mid] + [target]*zeros_count + non_target[mid:]
        
        # Copy back to original array (in-place)
        for i in range(len(arr)):
            # Copy each element from result to arr
            arr[i] = result[i]
        return arr

# Example usage
if __name__ == '__main__':
    sol = Solution()
    print(sol.zerosInMiddle([0, 1, 0, 3, 12]))


