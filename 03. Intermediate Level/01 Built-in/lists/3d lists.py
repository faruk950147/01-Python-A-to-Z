# ============================= 1. What is List =============================


# ============================= 2. Basic 3D List =============================

list3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

print(list3d)


# ============================= 3. List Access =============================

list3d = [
    [
        ['H', 'e', 'l', 'l', 'o'],
        ['W', 'o', 'r', 'l', 'd']
    ],
    [
        ['H', 'e', 'l', 'l', 'o'],
        ['W', 'o', 'r', 'l', 'd']
    ]
]

print(list3d[0])
print(list3d[1])
print(list3d[0][1])
print(list3d[1][0])
print(list3d[1][2])
print(list3d[0][0][0])
print(list3d[0][1][0])
print(list3d[1][0][0])
print(list3d[1][1][0])



# ============================= 4. Row Slicing =============================

print(list3d[0:2])
print(list3d[1:])
print(list3d[:])


# ============================= 5. Column Slicing =============================

print([row[0] for row in list3d])
print([row[1] for row in list3d])
print([row[-1] for row in list3d])
print([row[1:3] for row in list3d])


# ============================= 6. Negative Indexing =============================

print(list3d[-1])
print(list3d[-2])
print([row[-1] for row in list3d])
print([row[-2] for row in list3d])


# ============================= 7. Diagonal Access =============================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print([matrix[i][i] for i in range(len(matrix))])
print([matrix[i][len(matrix)-i-1] for i in range(len(matrix))])


# ============================= 8. Reverse =============================

print(list3d[::-1])
print([row[::-1] for row in list3d])
print([row[::-1] for row in list3d[::-1]])


# ============================= 9. Add Functions =============================

list3d[0][0].append(11)
list3d[1][0].insert(1, 60)
list3d[0][1].extend([11, 12])
list3d[1][1].extend([70, 80])

print(list3d)


# ============================= 10. Modify Functions =============================

list3d[0][0][1] = 20
list3d[1][1] = [70, 80]

list3d[0][1].append(11)
list3d[1][0].insert(1, 60)

print(list3d)


# ============================= 11. Delete Functions =============================

list3d[0][1].remove(11)
list3d[1][0].pop(1)
list3d[0][1].clear()
list3d[1][1].pop()
list3d[0][0].remove(1)
list3d[1][1].pop()

print(list3d)


# ============================= 12. Looping 3D List =============================

for i in list3d:
    for j in i:
        for k in j:
            print(k, end=" ")
print()


# ============================= 13. List Comprehension =============================

flatten = [k for i in list3d for j in i for k in j]
print(flatten)


# ============================= 14. Condition Functions =============================

print(any(k == 70 for i in list3d for j in i for k in j))
print(all(k > 0 for i in list3d for j in i for k in j))
print(20 in flatten)
print(100 not in flatten)