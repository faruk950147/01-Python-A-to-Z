# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list1[:3])
# print(list1[3:])
# print(list1[:len(list1)])
# print(list1[:])

# print(list1[-1])    
# print(list1[-2:])    
# print(list1[:-2])    

# print(any(x > 3 for x in list1))

list2d = [
    [1, 2],
    [3, 4]
]
# print(list2d[0])
# print(list2d[1])
# print(list2d[0][0])
# print(list2d[0][1])
# print(list2d[1][0])
# print(list2d[1][1])


# for row in list2d:
#     for col in row:
#         print(col)

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

# print(list3d[0])
# print(list3d[1])
# print(list3d[0][0])
# print(list3d[0][1])
# print(list3d[1][0])
# print(list3d[1][1])
print(list3d[0][0][0])

# first loop is a row
# second loop is a column
# third loop is a character (element)
for row in list3d:
    print("Row:", row)
    for col in row:
        # for char in col:
        #     print(char)
        print("Column:", col)