def sumOfList(list1):
    sum = 0
    for i in range(len(list1)):
        sum += list1[i]
    return sum

def givenListEvenOdd(list1):
    even = []
    odd = []
    sumEven = 0
    sumOdd = 0
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            # even.append(list1[i])
            even += [list1[i]]
            sumEven += list1[i]
        else:
            # odd.append(list1[i])
            odd += [list1[i]]
            sumOdd += list1[i]
    return even, odd, sumEven, sumOdd

print(f"Sum of List: {sumOfList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
print(f"Even: {givenListEvenOdd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])[0]}")
print(f"Odd: {givenListEvenOdd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])[1]}")
print(f"Sum of Even: {givenListEvenOdd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])[2]}")
print(f"Sum of Odd: {givenListEvenOdd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])[3]}")