"""A tiny invoice total. Small on purpose: the point is the tests around it, not the math.

Each line is (price in cents, how many). A discount is a percent off the whole order.
Money stays in whole cents, so nothing drifts by a fraction of a penny.
"""


def total_cents(lines: list[tuple[int, int]], discount_percent: int = 0) -> int:
    if not 0 <= discount_percent <= 100:
        # Fix 2: a discount over 100% used to make the total negative.
        raise ValueError("discount must be between 0 and 100")
    subtotal = 0
    for price, qty in lines:
        if qty < 0:
            # Fix 3: a negative quantity used to slip through and lower the bill.
            raise ValueError("quantity can't be negative")
        subtotal += price * qty
    # Fix 1: the discount used to be taken off each line and then off the total again.
    # Now it is taken once, from the subtotal, rounded to the nearest cent.
    return subtotal - round(subtotal * discount_percent / 100)
