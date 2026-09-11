
"""
    ধরো তোমার কাছে ৩টা কার্ড আছে
    1   2   3


    তুমি সবভাবে সাজাতে চাও।

    কোডটা আসলে কী করছে (মানুষের ভাষায়)
    x = lst[i]

    একটা কার্ড হাতে নিলে

    যেমন:

    আগে নিলে 1

    তারপর 2

    তারপর 3

    xs = lst[:i] + lst[i+1:]

    হাতে নেওয়া কার্ড বাদে বাকি কার্ডগুলো টেবিলে

    যেমন:

    x = 1 → xs = [2,3]

    x = 2 → xs = [1,3]

    x = 3 → xs = [1,2]

    perm(xs)

    বাকি কার্ডগুলো নিজেরা যতভাবে পারে সাজে

    যেমন:

    perm([2,3]) → [ [2,3], [3,2] ]

    [x] + p

    হাতের কার্ডটা সামনে বসাও

    যেমন:

    x = 1
    p = [3,2]
    → [1,3,2]

    একদম ছোট উদাহরণ (শুধু এইটা দেখো)
    x = 2
    p = [1,3]
    [x] + p = [2,1,3]


    এই লাইনটা বুঝলেই সব শেষ।

    সব মিলিয়ে কী হচ্ছে?
    হাতে নেওয়া	বাকি	ফল
    1	[2,3]	[1,2,3], [1,3,2]
    2	[1,3]	[2,1,3], [2,3,1]
    3	[1,2]	[3,1,2], [3,2,1]
    সবচেয়ে গুরুত্বপূর্ণ কথা 

    কোডটা কিছুই ম্যাজিক না
    শুধু:
    একটা সামনে রাখে, বাকিগুলো ঘুরায়

    এখন শুধু এটা বলো:

    [x] + p মানে কী?

    এইটা বুঝলেই তুমি recursion বুঝে ফেলছো।    
"""

def permutation(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        list1 = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in permutation(xs):
                list1.append([x] + p)
        return list1


print(permutation([1, 2, 3]))


import math
def permutation1(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]

    result = []
    # first character fix
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]

        # permutation of remaining string
        for p in permutation(remaining):
            result.append(char + p)
    return result


print(permutation1("abc"))


def nPr(n, r):
    if r > n:
        return 0   
    return math.perm(n, r) 

print(nPr(5, 2))


def nPr(n, r):
    if r > n:
        return 0
    return math.factorial(n) // math.factorial(n - r)  # noqa: F821

print(nPr(5, 2))  # Output: 20
