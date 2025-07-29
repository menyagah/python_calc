def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        price = discount_percent*price/100 + price
        return price
    return price


print(calculate_discount(50, 24))