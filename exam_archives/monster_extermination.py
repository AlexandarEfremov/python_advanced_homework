from collections import deque

monster_armor = deque([int(x) for x in input().split(",")])
striking_impact = [int(x) for x in input().split(",")]

killed_monsters = 0

while monster_armor and striking_impact:
    current_monster = monster_armor.popleft()
    current_soldier = striking_impact.pop()

    if current_soldier >= current_monster:
        remaining_strike = current_soldier - current_monster
        killed_monsters += 1
        if remaining_strike != 0 and striking_impact:
            striking_impact[-1] += remaining_strike
        elif not striking_impact and remaining_strike != 0:
            striking_impact.append(remaining_strike)
    elif current_monster > current_soldier:
        remaining_armour = current_monster - current_soldier
        monster_armor.append(remaining_armour)

if not monster_armor:
    print("All monsters have been killed!")
if not striking_impact:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
