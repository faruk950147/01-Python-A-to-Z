# ============================= 1. What is List =============================

# ============================= 2. Basic 2D List =============================

list2d = [
    [1, 2],
    [3, 4]
]

print(list2d)
print(list2d[0])
print(list2d[1])
print(list2d[0][1])
print(list2d[1][0])


# ============================= 3. List Access =============================

list2d = [
    ['H', 'e', 'l', 'l', 'o'],
    ['W', 'o', 'r', 'l', 'd']
]

print(list2d[0])
print(list2d[1])
print(list2d[0][1])
print(list2d[1][2])


# ============================= 4. Row Slicing =============================

print(list2d[0:2])
print(list2d[1:])
print(list2d[:])


# ============================= 5. Column Slicing =============================

print([row[0] for row in list2d])
print([row[1] for row in list2d])
print([row[-1] for row in list2d])
print([row[1:3] for row in list2d])


# ============================= 6. Negative Indexing =============================

print(list2d[-1])
print(list2d[-2])
print([row[-1] for row in list2d])
print([row[-2] for row in list2d])


# ============================= 7. Diagonal Access =============================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print([matrix[i][i] for i in range(len(matrix))])
print([matrix[i][len(matrix)-i-1] for i in range(len(matrix))])


# ============================= 8. Reverse =============================

print(list2d[::-1])
print([row[::-1] for row in list2d])
print([row[::-1] for row in list2d[::-1]])


# ============================= 9. Add Functions =============================

list2d = [
    [1, 2],
    [3, 4]
]

list2d[0].append(5)
list2d[1].insert(1, 6)
list2d[0].extend([7, 8])

print(list2d)


# ============================= 10. Modify Functions =============================

list2d[0][1] = 20
list2d[1] = [70, 80]

print(list2d)


# ============================= 11. Delete Functions =============================

list2d[0].remove(1)
list2d[1].pop()
list2d[0].clear()

print(list2d)


# ============================= 12. Looping =============================

for row in list2d:
    for item in row:
        print(item, end=" ")
print()


# ============================= 13. List Comprehension =============================

list2d = [
    [1, 2],
    [3, 4]
]

flatten = [j for i in list2d for j in i]
print(flatten)


# ============================= 14. Condition Functions =============================

list2d = [
    [10, 20],
    [30, 40]
]

flatten = [j for i in list2d for j in i]

print(any(20 in row for row in list2d))
print(all(all(k > 0 for k in row) for row in list2d))
print(20 in flatten)
print(100 not in flatten)