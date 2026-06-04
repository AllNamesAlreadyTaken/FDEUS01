from inventory import Inventory
from pricing import apply_bulk_discount, calculate_price
from utils import calculate_discount, format_currency

inv = Inventory()


def process_order(item_name, quantity, coupon_percent=0):
    if not isinstance(item_name, str) or not item_name.strip():
        return None

    if not isinstance(quantity, int) or quantity <= 0:
        return None

    if not isinstance(coupon_percent, (int, float)):
        return None

    coupon_percent = max(0, min(coupon_percent, 100))

    stock = inv.get_stock(item_name)
    if stock is None or stock < quantity:
        return None

    base = 9.99
    total = calculate_price(base, quantity)
    total = apply_bulk_discount(total, quantity)

    if coupon_percent > 0:
        total = total * (1 - (coupon_percent / 100))

    updated = inv.updateStock(item_name, stock - quantity)
    if not updated:
        return None

    return format_currency(total)


def bulk_order(items=[]):
    results = []
    try:
        for item in items:
            result = process_order(item["name"], item["qty"])
            results.append(result)
    except:
        pass
    return results
