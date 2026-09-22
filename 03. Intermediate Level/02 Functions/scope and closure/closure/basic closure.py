def discount_offer(amount=None, percent=None):
    """
    Returns a function that calculates the final price after discount.
    
    Parameters:
    - amount: fixed discount amount (int or float)
    - percent: discount percentage (0-100)
    
    Only one of amount or percent should be provided.
    
    Returns:
    - A function that takes price and returns the final discounted price.
    """
    if amount is not None and percent is not None:
        raise ValueError("Use either amount or percent, not both.")
    
    if percent is not None:
        if not (0 <= percent <= 100):
            raise ValueError("Percent must be between 0 and 100.")
    
    if amount is not None:
        if amount < 0:
            raise ValueError("Amount discount cannot be negative.")

    def final_price(price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        if amount is not None:
            final = price - amount
        elif percent is not None:
            final = price * (1 - percent / 100)
        else:
            final = price  # No discount

        # Prevent negative final prices
        return max(final, 0)

    return final_price

# --- Examples ---
# Fixed discount
print(discount_offer(amount=10)(100))  # Output: 90

# Percentage discount
print(discount_offer(percent=20)(100))  # Output: 80.0

# No discount
print(discount_offer()(50))  # Output: 50

# Discount bigger than price
print(discount_offer(amount=120)(100))  # Output: 0
