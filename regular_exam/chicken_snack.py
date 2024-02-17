from collections import deque

amount_of_money = [int(x) for x in input().split()]
prices_of_foods = deque([int(x) for x in input().split()])
amount_of_food = 0

while amount_of_money and prices_of_foods:
    current_amount = amount_of_money.pop()
    current_price = prices_of_foods.popleft()
    if current_amount == current_price:
        amount_of_food += 1
        pass
    elif current_amount > current_price:
        if amount_of_money:
            diff = current_amount - current_price
            amount_of_money[-1] += diff
            amount_of_food += 1
        else:
            diff = current_amount - current_price
            amount_of_money.append(diff)
            amount_of_food += 1
    else:
        pass

if amount_of_food >= 4:
    print(f"Gluttony of the day! Henry ate {amount_of_food} foods.")
elif 1 < amount_of_food < 4:
    print(f"Henry ate: {amount_of_food} foods.")
elif amount_of_food == 1:
    print(f"Henry ate: {amount_of_food} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
