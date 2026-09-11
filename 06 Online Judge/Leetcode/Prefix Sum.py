'''Prefix Sum কি?

Prefix Sum হলো একটি array এর running sum বা cumulative sum।
মানে, array এর প্রতিটি index পর্যন্ত সব elements এর যোগফল।

Example:

arr = [1, 2, 3, 4, 5]

Index 0: 1 → sum = 1

Index 1: 1+2 = 3

Index 2: 1+2+3 = 6

Index 3: 1+2+3+4 = 10

Index 4: 1+2+3+4+5 = 15

Prefix Sum Array:

prefix = [1, 3, 6, 10, 15]
 কেন Prefix Sum ব্যবহার করি?

সাধারণভাবে:
যদি array এর subarray sum বার বার বের করতে চাই, direct sum করলে O(n) লাগে।
Prefix Sum ব্যবহার করলে আমরা একবারে O(1) সময়েই subarray sum বের করতে পারি।

Formula:

sum of subarray arr[l..r] = prefix[r] - prefix[l-1]  (যদি l > 0)
sum of subarray arr[0..r] = prefix[r]               (যদি l = 0)

Example:

arr = [1,2,3,4,5]
prefix = [1,3,6,10,15]

# sum of arr[1..3] = 2+3+4 = 9
# formula দিয়ে: prefix[3] - prefix[0] = 10 - 1 = 9
 Python কোড উদাহরণ
def prefix_sum(arr):
    n = len(arr)
    prefix = [0]*n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix

arr = [1,2,3,4,5]
prefix = prefix_sum(arr)
print("Prefix Sum:", prefix)

# subarray sum arr[1..3]
l, r = 1, 3
sub_sum = prefix[r] - prefix[l-1] if l > 0 else prefix[r]
print("Subarray sum arr[1..3]:", sub_sum)

Output:

Prefix Sum: [1, 3, 6, 10, 15]
Subarray sum arr[1..3]: 9
Common Problems যেখানে Prefix Sum ব্যবহার হয়

Subarray sum queries
যেমন, একটি array থেকে বিভিন্ন index এর sum বারবার খুঁজতে হবে।

Contiguous subarray sum = target
Two sum এর মতোই, কিন্তু subarrays।

Range updates in array
Large array এ একাধিক addition/subtraction করতে পারি O(1) এ।

Leetcode problems

Subarray Sum Equals K

Range Sum Query

Maximum Subarray Sum variations
Problem: Subarray Sum Equals K

Problem:

একটি array nums এবং একটি integer k দেওয়া আছে।
তুমি বের করবে কতটি contiguous subarray এর sum = k।

Example:

nums = [1, 1, 1]
k = 2

Subarrays যেগুলোর sum = 2 → [1,1], [1,1]

Output = 2

Approach: Prefix Sum + HashMap

Idea:

Subarray sum = prefix[j] - prefix[i]
মানে, যদি আমরা prefix[j] - k আগে দেখেছি, তাহলে subarray sum = k পাওয়া যাবে।

Dictionary ব্যবহার করে প্রতি prefix sum এর frequency রাখি।

O(n) time এ সব solve করা যায়।

Python কোড
def subarraySum(nums, k):
    prefix_count = {0: 1}  # sum 0 একবার আছে
    total = 0              # running prefix sum
    result = 0             # count of subarrays

    for num in nums:
        total += num
        # check if total - k existed before
        if (total - k) in prefix_count:
            result += prefix_count[total - k]
        # save current total in dictionary
        prefix_count[total] = prefix_count.get(total, 0) + 1

    return result

# Example
nums = [1,1,1]
k = 2
print("Number of subarrays:", subarraySum(nums, k))

Output:

Number of subarrays: 2
Step by Step (Bangla)

prefix_count = {0: 1} → sum 0 একবার আছে (empty subarray এর জন্য)।

total দিয়ে চলমান sum রাখি।

প্রতি number এ check করি total - k আগে এসেছে কিনা।

যদি এসেছে, মানে আমরা একটি subarray পেয়েছি যার sum = k।

শেষে সব গোনা subarrays count করি।

Time Complexity: O(n)
Space Complexity: O(n) (dictionary এর জন্য)
'''


def subarraySum(nums, k):
    prefix_count = {0: 1}  # sum 0
    total = 0  # running prefix sum
    result = 0  # count of subarrays

    for num in nums:
        total += num
        # check if total - k existed before
        if (total - k) in prefix_count:
            result += prefix_count[total - k]
        # save current total in dictionary
        prefix_count[total] = prefix_count.get(total, 0) + 1

    return result


# Example
nums = [1, 1, 1]
k = 2
print("Number of subarrays:", subarraySum(nums, k))