# Order pricing rules for the storefront checkout.

TAX_RATE = 0.08
BULK_THRESHOLD = 10
BULK_DISCOUNT_PERCENT = 15


# Orders of BULK_THRESHOLD units or more receive the bulk discount.
def bulk_discount_percent(quantity):
    if quantity >= BULK_THRESHOLD:
        return BULK_DISCOUNT_PERCENT
    return 0


# Price for a single cart line before discounts or tax.
def line_total(unit_price, quantity):
    return unit_price * quantity


# Final charge for an order: bulk discount first, then tax.
def cart_total(unit_price, quantity):
    subtotal = line_total(unit_price, quantity)
    discounted = subtotal * (1 - bulk_discount_percent(quantity) / 100)
    return round(discounted * (1 + TAX_RATE), 2)