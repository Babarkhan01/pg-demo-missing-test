def price_after_discount(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("invalid percent")
    return round(price * (1 - percent / 100), 2)


def bulk_discount(price, quantity):
    if quantity >= 100:
        return round(price * 0.8, 2)
    if quantity >= 10:
        return round(price * 0.9, 2)
    return price
