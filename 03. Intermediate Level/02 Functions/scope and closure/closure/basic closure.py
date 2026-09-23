from typing import Callable, Optional, Union

Number = Union[int, float]

def discount_offer(
    amount: Optional[Number] = None,
    percent: Optional[Number] = None
) -> Callable[[Number], Number]:
    """
    Returns a function that calculates the final price after discount.

    Parameters:
    - amount: fixed discount amount (int or float)
    - percent: discount percentage (0–100)

    Only one of amount or percent should be provided.

    Returns:
    - A function that takes a price (int or float) and returns the final
      discounted price (float), never negative.
    """
    if amount is not None and percent is not None:
        raise ValueError("Use either amount or percent, not both.")

    if percent is not None and not (0 <= percent <= 100):
        raise ValueError("Percent must be between 0 and 100.")

    if amount is not None and amount < 0:
        raise ValueError("Amount discount cannot be negative.")

    def final_price(price: Number) -> Number:
        if price < 0:
            raise ValueError("Price cannot be negative.")

        if amount is not None:
            final = price - amount
        elif percent is not None:
            final = price * (1 - percent / 100)
        else:
            final = price  # No discount

        return max(final, 0)

    return final_price
