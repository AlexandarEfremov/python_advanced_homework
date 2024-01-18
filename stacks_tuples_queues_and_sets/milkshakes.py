from collections import deque
chocolate_values = [int(x) for x in input().split(", ")]
milk_values = deque(int(x) for x in input().split(", "))

milkshake_counter = 0
while milkshake_counter != 5 and chocolate_values and milk_values:
    choc_element = chocolate_values.pop()
    milk_element = milk_values.popleft()
    if choc_element <= 0 and milk_element <= 0:
        continue
    elif choc_element <= 0:
        milk_values.appendleft(milk_element)
        continue
    elif milk_element <= 0:
        chocolate_values.append(choc_element)
        continue

    if choc_element == milk_element:
        milkshake_counter += 1
        continue
    else:
        chocolate_values.append(choc_element - 5)
        milk_values.append(milk_element)

if milkshake_counter >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_values:
    choc_str = ", ".join(map(str, chocolate_values))
    print(f"Chocolate: {choc_str}")
else:
    print("Chocolate: empty")
if milk_values:
    milk_str = ", ".join(map(str, milk_values))
    print(f"Milk: {milk_str}")
else:
    print("Milk: empty")