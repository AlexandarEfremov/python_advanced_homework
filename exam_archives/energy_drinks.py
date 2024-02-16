from collections import deque

mils_of_caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

max_energy = 0

while mils_of_caffeine and energy_drinks:
    current_caffeine = mils_of_caffeine.pop()
    current_drink = energy_drinks.popleft()
    result = current_caffeine * current_drink
    if (result + max_energy) <= 300:
        max_energy += result
    else:
        energy_drinks.append(current_drink)
        max_energy -= 30 if (max_energy - 30) >= 0 else max_energy

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {max_energy} mg caffeine.")
