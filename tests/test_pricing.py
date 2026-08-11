from pricing import bulk_discount_percent


def test_bulk_discount_applies_at_exactly_ten_units():
    # A customer ordering exactly 10 units qualifies for the bulk discount.
    assert bulk_discount_percent(10) == 15
