rows, cols = (int(x) for x in input().split())
initial_lair = []
current_position = []

for row in range(rows):
    line = [y for y in input()]
    initial_lair.append(line)
    if "P" in line:
        current_position = [row, initial_lair[row].index("P")]

commands = input()

directions = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}


def bunny_multi(lair, **dir):
    temp_lair = [row.copy() for row in lair]
    for i, current_ro in enumerate(lair):
        if "B" in current_ro:
            current_bunny_position = [i, current_ro.index("B")]
            for position in dir.keys():
                expanded_row, expanded_col = current_bunny_position[0] + dir[position][0], \
                    current_bunny_position[1] + dir[position][1]
                if 0 <= expanded_row < rows and 0 <= expanded_col < rows and temp_lair[expanded_row][expanded_col]:
                    if temp_lair[expanded_row][expanded_col] == "P":
                        break
                    else:
                        temp_lair[expanded_row][expanded_col] = "B"
    lair = temp_lair
    return lair


for command in commands:
    r, c = current_position[0] + directions[command][0], current_position[1] + directions[command][1]
    initial_lair[current_position[0]][current_position[1]] = "."
    if not (0 <= r < rows and 0 <= c < rows):
        initial_lair = bunny_multi(initial_lair, **directions)
        initial_lair = ["".join(x) for x in initial_lair]
        [print(row, sep="\n") for row in initial_lair]
        print(f"won: {current_position[0]} {current_position[1]}")
        break
    if initial_lair[r][c] == "B":
        initial_lair = bunny_multi(initial_lair, **directions)
        initial_lair = ["".join(x) for x in initial_lair]
        [print(row, sep="\n") for row in initial_lair]
        print(f"dead: {r} {c}")
        break
    else:
        initial_lair = bunny_multi(initial_lair, **directions)
    current_position = [r, c]


