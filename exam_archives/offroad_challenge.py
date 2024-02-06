from collections import deque

initial_fuel_integers = deque([int(x) for x in input().split()])
consumption_indexes = deque([int(x) for x in input().split()])
quantities_needed = deque([int(x) for x in input().split()])
fail = False
alt = 0

while initial_fuel_integers:
    current_fuel = initial_fuel_integers.pop()
    current_fuel_index = consumption_indexes.popleft()
    result = current_fuel - current_fuel_index
    current_needed_fuel = quantities_needed.popleft()

    if result >= current_needed_fuel:
        alt += 1
        print(f"John has reached: Altitude {alt}")
        continue
    else:
        fail = True
        print(f"John did not reach: Altitude {alt + 1}")
        break

reached_altitudes = [f"Altitude {i + 1}" for i in range(alt)]

if fail and alt > 0:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_altitudes)}")
elif fail and alt == 0:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")

