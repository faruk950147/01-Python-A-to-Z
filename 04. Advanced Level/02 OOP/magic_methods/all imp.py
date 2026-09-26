import all

print(dir())

# output:
# [
# '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
# '__name__', '__package__', '__spec__', 'all'
# ]

from all import *


print(str1)
print(dir())

# output:
# [
#     '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
#     '__name__', '__package__', '__spec__', 'default_info', 'personal_info', 'private_info', 
#     'protected_info', 'str1'
# ]

