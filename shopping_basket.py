shopping_basket = [10, 20, 12, 24, 78, 16]
print(f"Total price: {sum(shopping_basket)}")

def calc_discount(prices, items_with_sale, sale_percent, has_card=False):
    total = 0
    for i in range(len(prices)):
        price = prices[i]
        if i in items_with_sale:
            price_with_discount = price * (1 - sale_percent/100)
            total = total + price_with_discount
        else:
            total = total + price

    if has_card:
        result = total*0.95
    else:
        result = total
    return result
    
print(f"Price with discount: "
    f"{calc_discount(shopping_basket, [1, 3, 5], 10, has_card=True)}")
