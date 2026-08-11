from pricing import bulk_discount_percent, cart_total, line_total


def test_line_total_multiplies_price_by_quantity():
    assert line_total(2.50, 4) == 10.0


def test_no_bulk_discount_below_threshold():
    assert bulk_discount_percent(9) == 0


def test_bulk_discount_applies_at_exactly_ten_units():
    # A customer ordering exactly 10 units qualifies for the bulk discount.
    assert bulk_discount_percent(10) == 15


def test_cart_total_applies_discount_then_tax():
    # 10 x $10.00 = $100.00, less 15% = $85.00, plus 8% tax = $91.80
    assert cart_total(10.00, 10) == 91.80
