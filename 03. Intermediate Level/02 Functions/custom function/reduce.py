'''
lst = [1, 2, 3, 4, 5]
print(reduceFind(lst, add, 0))
# Initial Setup
lst = [1,2,3,4,5]
initial = 0
result = initial = 0
# Loop Execution Flow
# Iteration 1 (i = 0)
current = 1
prev = result = 0
result = add(0, 1) = 1
# Iteration 2 (i = 1)
current = 2
prev = result = 1
result = add(1, 2) = 3
# Iteration 3 (i = 2)
current = 3
prev = result = 3
result = add(3, 3) = 6
# Iteration 4 (i = 3)
current = 4
prev = result = 6
result = add(6, 4) = 10
# Iteration 5 (i = 4)
current = 5
prev = result = 10
result = add(10, 5) = 15
# Final Output
15
# Visualization (Super Simple)
0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
# Key Concept
result বারবার update হচ্ছে

প্রতিবার:

result = callback(previous_result, current_value)
তাই এটাকে বলে accumulator pattern
Bonus (Real reduce analogy)

Python built-in:

from functools import reduce
reduce(add, lst, 0)

তোমার function = custom reduce

'''

def reduceFind(lst, callback, initial):
    # list iteration work in all elements
    # callback function work in updated result and current element
    # callback function return updated result
    # initial is the first value of result
    result = initial
    for i in range(len(lst)):
        # just value send if we want to send index and list then use lst[i], i, lst
        # result = callback(result, lst[i], i, lst)
        result = callback(result, lst[i]) 
    return result

# just a callback
def add(prev, curr): # just value send if we want to send index and list then use lst[i], i, lst
    # previous is the updated result
    # current is the current element
    # return updated result
    # prev + curr
    return prev + curr 

lst = [1, 2, 3, 4, 5]
print(reduceFind(lst, add, 0))

'''
Step by Step 
lst = [1, 2, 3, 4, 5]
print(reduceFind(lst, add, 0))
start:
result = initial = 0
Iteration 1:
prev = 0
curr = 1
result = 0 + 1 = 1
Iteration 2:
prev = 1
curr = 2
result = 1 + 2 = 3
Iteration 3:
prev = 3
curr = 3
result = 3 + 3 = 6
Iteration 4:
prev = 6
curr = 4
result = 6 + 4 = 10
Iteration 5:
prev = 10
curr = 5
result = 10 + 5 = 15
Final Output:
15
সহজ ভাষায়

reduceFind() মানে:

"একটা result নিয়ে list-এর প্রতিটা element দিয়ে বারবার update করা"

Built-in reduce এর সাথে মিল

Python-এ already এটা আছে 

from functools import reduce

reduce(add, lst, 0)

তুমি basically নিজের হাতে এটা বানিয়েছো 

Bonus (Different Example)
Multiplication:
def mul(prev, curr):
    return prev * curr

print(reduceFind([1,2,3,4], mul, 1))

Output:

24
Pro Tip

তুমি চাইলে এটা আরও powerful করতে পারো 

result = callback(result, lst[i], i, lst)

তাহলে callback function এ:

index
পুরো list

দুটাই access করতে পারবে
'''


"""
Basic idea of reduce():

Multiple values
      |
      v
Repeatedly apply callback
      |
      v
One final value
"""


def my_reduce(callback, iterable):

    iterator = iter(iterable)

    result = next(iterator)

    for value in iterator:

        result = callback(result, value)

    return result


def add(x, y):

    return x + y


numbers = [1, 2, 3, 4, 5]

result = my_reduce(add, numbers)

print(result)

# Output:
# 15


"""
Flow:

result = 1

1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15

Final result:

15
"""
