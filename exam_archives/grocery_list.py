def shop_from_grocery_list(budget, grocery_list, *args):
    purchased_list = []
    spend = 0
    left_products = grocery_list.copy()
    for product_name, price in args:
        if budget <= 0:
            break
        if product_name not in grocery_list:
            continue
        if product_name in purchased_list:
            continue
        else:
            price = float(price)
            diff = budget - price
            if diff >= 0:
                purchased_list.append(product_name)
                left_products.remove(product_name)
                spend += price
                budget -= price
            elif diff < 0:
                break
    if not left_products:
        return f"Shopping is successful. Remaining budget: {(budget):.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(left_products)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
