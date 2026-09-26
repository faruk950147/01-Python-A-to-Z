# lst = [1, 2, 3, 4, 5]

# Creating a new list object or reference to the same list
# If we assign one list to another directly, both will refer to the same memory location.
# So any changes made to one list will also be reflected in the other.
# This happens because both variables point to the same object in memory.
# This issue is related to the concept of shallow copy and deep copy.

# new_lst = lst
# print("before old lst: ", lst, '\n', 'address: ', id(lst))
# print("before new new_lst: ", new_lst, '\n', 'address: ', id(new_lst))

# lst[0] = 10
# print("after old lst: ", lst, '\n', 'address: ', id(lst))
# print("after new new_lst: ", new_lst, '\n', 'address: ', id(new_lst))

# ======================= Shallow Copy vs Deep Copy =======================

# Shallow Copy:
# A shallow copy creates a new object but stores references of the original elements.
# So if the original object is modified, the changes may still be reflected in the copy
# (especially for nested or mutable objects).
import copy
lst = [1, 2, 3, 4, 5]
new_lst = copy.copy(lst)
print("before old lst: ", lst, 'address: ', id(lst))
print("before new new_lst: ", new_lst, 'address: ', id(new_lst))

lst[0] = 10
print("after old lst: ", lst, 'address: ', id(lst))
print("after new new_lst: ", new_lst, 'address: ', id(new_lst))

# Deep Copy:
# A deep copy creates a new object and recursively copies all elements from the original object.
# Changes to the original object will not affect the copy, as they are separate objects in memory.
new_lst = copy.deepcopy(lst)
print("before old lst: ", lst, 'address: ', id(lst))
print("before new new_lst: ", new_lst, 'address: ', id(new_lst))

lst[0] = 10
print("after old lst: ", lst, 'address: ', id(lst))
print("after new new_lst: ", new_lst, 'address: ', id(new_lst))

