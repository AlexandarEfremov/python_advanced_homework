rows, cols = [int(x) for x in input().split()]
playground_matrix = []
starting_position = []
total_opponents = 0

for row in range(rows):
    line = [x for x in input().split()]
    playground_matrix.append(line)
    if "B" in line:
        starting_position = [row, line.index("B")]
    if "P" in line:
        total_opponents += line.count("P")

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

current_row, current_col = starting_position[0], starting_position[1]
moves = 0
touched_opponents = 0

input_command = input()
while input_command != "Finish":
    if total_opponents == 0:
        break
    move_row, move_col = current_row + directions[input_command][0], current_col + directions[input_command][1]
    if move_row < 0 or move_row == rows or move_col < 0 or move_col == cols:
        input_command = input()
        continue
    if playground_matrix[move_row][move_col] == "O":
        input_command = input()
        continue
    if playground_matrix[move_row][move_col] == "P":
        touched_opponents += 1
        total_opponents -= 1
        playground_matrix[move_row][move_col] = "-"
    moves += 1
    current_row, current_col = move_row, move_col
    input_command = input()

print(f"Game over!\nTouched opponents: {touched_opponents} Moves made: {moves}")