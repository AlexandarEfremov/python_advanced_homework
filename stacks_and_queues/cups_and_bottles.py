from collections import deque

cups_capacity = deque(int(x) for x in input().split())
filled_bottles = deque(int(y) for y in input().split())
temp_bottle_len = len(filled_bottles)

wasted_water = 0
while cups_capacity and filled_bottles:
    current_bottle = filled_bottles.pop()
    current_cup = cups_capacity.popleft()
    if current_bottle - current_cup == 0:
        continue
    elif current_bottle - current_cup > 0:
        wasted_water += abs(current_cup - current_bottle)
    else:
        current_cup = current_cup - current_bottle
        cups_capacity.appendleft(current_cup)

if not cups_capacity:
    print(f"Bottles: {' '.join(str(x) for x in filled_bottles)}")
if not filled_bottles:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")
print(f"Wasted litters of water: {wasted_water}")