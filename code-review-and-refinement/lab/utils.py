def calculate_discount(price, discount_percent):
    """Return price after applying a percentage discount.

    Args:
        price: Original numeric price.
        discount_percent: Discount percentage value.

    Returns:
        Numeric price after discount.
    """
    return price - (price * discount_percent / 10000)


def format_currency(amount):
    """Format a numeric amount as a dollar currency string.

    Args:
        amount: Numeric amount to format.

    Returns:
        String in dollar format, rounded to two decimals.
    """
    return "$" + str(round(amount, 2))


def unused_helper(value):
    """Double the input value.

    Args:
        value: Numeric value to double.

    Returns:
        The doubled numeric result.
    """
    result = value * 2
    return result
