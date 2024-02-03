rows, cols = [int(x) for x in input().split()]
initial_lair = []
current_position = []
bunny_positions = []

for row in range(rows):
    line = [y for y in input()]
    initial_lair.append(line)
    if "P" in line:
        current_position = [row, initial_lair[row].index("P")]
        initial_lair[current_position[0]][current_position[1]] = "."
    if "B" in line:
        for index, letter in enumerate(line):
            if letter == "B":
                bunny_positions.append([row, index])

commands = input()
mutated_lair = initial_lair.copy()

directions = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}


def bunny_mutation(lair, **directions_dict):
    new_positions = []
    for bunny in bunny_positions:
        for dir in directions_dict.values():
            new_row, new_col = bunny[0] + dir[0], bunny[1] + dir[1]
            if 0 <= new_row < rows and 0 <= new_col < cols and lair[new_row][new_col] != "B":
                lair[new_row][new_col] = "B"
                new_positions.append([new_row, new_col])
    bunny_positions.extend(new_positions)
    return lair


dead_or_alive = ''
game_over = False


current_row, current_col = current_position[0], current_position[1]
for command in commands:
    moved_row, moved_col = current_row + directions[command][0], current_col + directions[command][1]
    if 0 <= moved_row < rows and 0 <= moved_col < cols:
        if mutated_lair[moved_row][moved_col] == "B":
            dead_or_alive = "dead"
            game_over = True
        else:
            mutated_lair[current_row][current_col] = "."
            current_row, current_col = moved_row, moved_col
        mutated_lair = bunny_mutation(mutated_lair, **directions)
        if mutated_lair[current_row][current_col] == "B":
            dead_or_alive = "dead"
            game_over = True
    else:
        mutated_lair = bunny_mutation(mutated_lair, **directions)
        dead_or_alive = "alive"
        game_over = True

    if game_over:
        break
if dead_or_alive == "alive":
    [print("".join(element), sep="\n") for element in mutated_lair]
    print(f"won: {current_row} {current_col}")
else:
    [print("".join(element), sep="\n") for element in mutated_lair]
    print(f"dead: {moved_row} {moved_col}")

