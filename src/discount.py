import os


def calculate_cart_total(cart_sum, tier, promos):
    price = cart_sum
    if cart_sum > 15000:
        price = cart_sum * 0.85
    for p in promos:
        if p == "SUMMER":
            price = price - 500
        elif p == "VIP":
            price = price * 0.90
    if tier == 1:
        price = price * 0.97
    elif tier == 2:
        price = price * 0.93
    if price < cart_sum * 0.70:
        price = cart_sum * 0.70  # нижняя граница: итоговая скидка не может превышать 30% от суммы корзины
    return price
