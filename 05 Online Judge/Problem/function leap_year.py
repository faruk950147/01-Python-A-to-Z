def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  
        return True  # leap is True
    return False  # leap False 

year = int(input())  # input
print(is_leap(year)) # call fun
