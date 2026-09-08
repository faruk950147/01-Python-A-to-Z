# write a program for flowing the requirement of the user
# if user enter the or input 2 512
# 2*2 = 4
# 4*2 = 8
# 8*2 = 16
# 16*2 = 32
# 32*2 = 64
# 64*2 = 128
# 128*2 = 256
# 256*2 = 512

def get_number(num1, num2):
    result = num1
    count = 0
    
    # Keep multiplying by 2 until we reach or exceed the target
    while result < num2:
        result *= 2
        count += 1
        
    # Check if we exactly reached the target
    if result == num2:
        return count
    else:
        return "Target is not reachable by multiplying by 2 from the starting number."

print(get_number(2, 512))  # Output: 8
print(get_number(3, 512))  # Output: Target is not reachable...
