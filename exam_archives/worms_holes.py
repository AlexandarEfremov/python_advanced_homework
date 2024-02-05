from collections import deque

worm_sizes = deque([int(x) for x in input().split()])
hole_sizes = deque([int(x) for x in input().split()])

matches = 0
no_home = 0

while worm_sizes and hole_sizes:
    current_worm = worm_sizes.pop()
    if current_worm == hole_sizes.popleft():
        matches += 1
        continue
    else:
        updated_value = current_worm - 3
        if updated_value > 0:
            worm_sizes.append(updated_value)
        else:
            no_home += 1

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worm_sizes and no_home == 0:
    print("Every worm found a suitable hole!")
elif no_home > 0:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join([str(x) for x in worm_sizes])}")

if not hole_sizes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join([str(x) for x in hole_sizes])}")
