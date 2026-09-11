class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        count = 0
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count
# Test locally
sol = Solution()
print(sol.countGoodTriplets([1, 2, 3, 4], 1, 1, 1))  # Output: 4

class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        count = 0
        n = len(arr)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue  # IF THIS IS NOT EVEN THEN WE DONT NEED TO CHECK K LOOP
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count
