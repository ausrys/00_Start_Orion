from typing import List


def get_prices_after_discounts(product_name: str,
                               price: int,
                               discounts: List[int] = []) -> int:
    if product_name == "apple":
        discounts.append(10)
    for discount in discounts:
        price -= discount
    return price


print(get_prices_after_discounts("apple", 100))
print(get_prices_after_discounts("apple", 100, [20]))
print(get_prices_after_discounts("orange", 200))
print(get_prices_after_discounts("apple", 100, [20, 30]))
print(get_prices_after_discounts("apple", 100))
print(get_prices_after_discounts("orange", 200))
