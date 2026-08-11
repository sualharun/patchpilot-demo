BULK_THRESHOLD = 10
BULK_DISCOUNT_PERCENT = 15


def bulk_discount_percent(quantity):
    """Orders of BULK_THRESHOLD units or more receive the bulk discount."""
    if quantity >= BULK_THRESHOLD:
        return BULK_DISCOUNT_PERCENT
    return 0
