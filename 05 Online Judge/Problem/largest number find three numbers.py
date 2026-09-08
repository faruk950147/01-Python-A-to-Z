def largest_number(a, b, c):
    return max(a, b, c)

print(largest_number(1, 2, 3))

def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(largest_number(1, 2, 3))

def largest_number(a, b, c):
    return a if a >= b and a >= c else b if b >= a and b >= c else c

print(largest_number(1, 2, 3))

def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(largest_number(1, 2, 3))

def largest_number(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

print(largest_number(1, 2, 3))

def largest_number(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

print(largest_number(1, 2, 3))

def largest_number(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

print(largest_number(1, 2, 3))

def largest_number(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

print(largest_number(1, 2, 3))




def largest_number(a, b):
    if a >= b:
        return a
    else:
        return b

print(largest_number(1, 2))
