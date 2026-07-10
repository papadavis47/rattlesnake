notebooks = 4
price = 2.5
total = notebooks * price


def test_purchase_total():
    assert notebooks == 4
    assert price == 2.5
    assert total == 10.0
