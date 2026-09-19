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

Because we want to read the string from the last character to the first character.

Take:

str = "hello"

Indexes are:

 h   e   l   l   o
 0   1   2   3   4
Why len(str)-1?

len(str) is 5, but the last index is 4.

len(str) - 1
= 5 - 1
= 4

So we start at 4:

h e l l o
        ↑
        4
Why -1 as the stop?

We want to reach index 0.

Python's range() does not include the stop value.

So:

range(4, -1, -1)

gives:

4 → 3 → 2 → 1 → 0

If we used:

range(4, 0, -1)

we would get:

4 → 3 → 2 → 1

0 would be missing.

Why -1 as the step?

Because we want to move backward:

4
↓ -1
3
↓ -1
2
↓ -1
1
↓ -1
0

So the whole thing:

range(len(str)-1, -1, -1)

simply means:

Start from the last index → go backward → stop after reaching index 0.
"""