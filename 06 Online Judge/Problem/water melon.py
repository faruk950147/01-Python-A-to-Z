def water_melon(w):
    """
    Check if a watermelon of weight w can be divided into two parts,
    each with even weight.
    
    Logic:
    - If w is even and greater than 2, it can always be divided into two even parts.
    - For example: 4 -> 2 + 2, 6 -> 2 + 4, 8 -> 2 + 6, etc.
    
    Args:
        w (int): Weight of the watermelon
        
    Returns:
        str: "YES" if possible, "NO" otherwise
    """
    if w % 2 == 0 and w > 2:
        return "YES"
    else:
        return "NO"

print(water_melon(4))
print(water_melon(3))
print(water_melon(8))
print(water_melon(11))