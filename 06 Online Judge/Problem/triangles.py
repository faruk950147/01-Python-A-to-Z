import math
# Heron's formula method
def triangleAreaHeronsFormula1(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    else:
        return "Invalid triangle"
    
print(triangleAreaHeronsFormula1(3, 4, 5))

# Math library method
def triangleAreaHeronsFormula2(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        return "Invalid triangle"
    
print(triangleAreaHeronsFormula2(3, 4, 5))

# Base and height method
def triangle_area(base, height):
    return 0.5 * base * height

print(triangle_area(10, 20))