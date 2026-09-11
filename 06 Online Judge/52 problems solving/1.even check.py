
# Bismillahir Rahmanir Rahim

t = int(input("Enter a number for test cases: "))  # first input: how many times to check

for _ in range(t):
    n = int(input("Enter a number2: "))  # each number input
    if n % 2 == 0:
        print("Even")  # if number is even
    else:
        print("Odd")   # if number is odd
