# Bismillahir Rahmanir Rahim

n = int(input())

for _ in range(n):

    # Large number handle using string
    num = input()

    # Get last digit
    last_digit = int(num[-1])

    # even / odd check
    if last_digit % 2 == 0:
        print("even")
    else:
        print("odd")