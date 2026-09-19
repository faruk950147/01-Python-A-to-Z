"""
range(start, stop, step)
range(len(str)-1, -1, -1)
       ↑          ↑    ↑
     start       stop step

Example:
str = "hello"

len(str) = 5
len(str)-1 = 4

range(4, -1, -1)

4 → 3 → 2 → 1 → 0

start = 4     → Start from the last index
stop = -1     → Stop before -1 (so 0 is included)
step = -1     → Move backward by 1

"""