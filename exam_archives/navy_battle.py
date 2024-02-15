battlefield_size = int(input())
battlefield_matrix = []
submarine_position = []

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for row in range(battlefield_size):
    line = [x for x in input()]
    battlefield_matrix.append(line)
    if "S" in line:
        submarine_position = [row, line.index("S")]
        battlefield_matrix[submarine_position[0]][submarine_position[1]] = "-"
current_row, current_col = submarine_position[0], submarine_position[1]
mines_hit = 0
cruisers_destroyed = 0
while True:
    direction = input()
    move_row, move_col = current_row + directions[direction][0], current_col + directions[direction][1]
    if battlefield_matrix[move_row][move_col] == "-":
        current_row, current_col = move_row, move_col
        continue
    if battlefield_matrix[move_row][move_col] == "*":
        battlefield_matrix[move_row][move_col] = "-"
        mines_hit += 1
        if mines_hit > 2:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{move_row}, {move_col}]!")
            break
    if battlefield_matrix[move_row][move_col] == "C":
        battlefield_matrix[move_row][move_col] = "-"
        cruisers_destroyed += 1
        if cruisers_destroyed == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    current_row, current_col = move_row, move_col

battlefield_matrix[move_row][move_col] = "S"
battlefield_matrix = ["".join(el) for el in battlefield_matrix]
print(*battlefield_matrix, sep="\n")