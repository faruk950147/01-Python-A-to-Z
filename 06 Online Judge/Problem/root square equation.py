# your code is finding one root of a quadratic equation.

def root_square_equation(a, b, c):
    return (-b + (b**2 - 4*a*c)**0.5) / (2*a)

print(root_square_equation(1, -5, 6))
'''
# Full Notes: Quadratic Equation in Python

# Quadratic Equation:
# ax² + bx + c = 0

# Example Equation:
# x² - 5x + 6 = 0

# Here:
a = 1
b = -5
c = 6

# Root means:
# A value of x that makes the equation equal to 0.

# Quadratic Formula:
# x = (-b ± √(b² - 4ac)) / (2a)

# Discriminant:
# D = b² - 4ac

# Step 1: Calculate Discriminant

D = b**2 - 4*a*c

print("Discriminant:", D)

# Step 2: Find First Root

x1 = (-b + D**0.5) / (2*a)

# Step 3: Find Second Root

x2 = (-b - D**0.5) / (2*a)

print("First Root:", x1)
print("Second Root:", x2)

# Full Function

def root_square_equation(a, b, c):

    # Discriminant
    d = (b**2 - 4*a*c)**0.5

    # First Root
    x1 = (-b + d) / (2*a)

    # Second Root
    x2 = (-b - d) / (2*a)

    return x1, x2


print(root_square_equation(1, -5, 6))

# Output:
# (3.0, 2.0)
'''
