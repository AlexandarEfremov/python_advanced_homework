size_of_fishery = int(input())
fishery_matrix = []
starting_position = []

for i in range(size_of_fishery):
    line = [int(el) if el.isdigit() else el for el in input()]
    fishery_matrix.append(line)
    if "S" in line:
        starting_position = [i, line.index("S")]
        fishery_matrix[starting_position[0]][starting_position[1]] = "-"

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

input_info = input()
current_row, current_col = starting_position[0], starting_position[1]
collected = 0
drown = False
while input_info != "collect the nets":
    if input_info == "up":
        move_row, move_col = current_row + directions["up"][0], current_col + directions["up"][1]
        if move_row < 0:
            move_row = size_of_fishery - 1
        if fishery_matrix[move_row][move_col] != "W" and fishery_matrix[move_row][move_col] != "-":
            collected += fishery_matrix[move_row][move_col]
            fishery_matrix[move_row][move_col] = "-"
        if fishery_matrix[move_row][move_col] == "W":
            drown = True
            break
    elif input_info == "down":
        move_row, move_col = current_row + directions["down"][0], current_col + directions["down"][1]
        if move_row == size_of_fishery:
            move_row = 0
        if fishery_matrix[move_row][move_col] != "W" and fishery_matrix[move_row][move_col] != "-":
            collected += fishery_matrix[move_row][move_col]
            fishery_matrix[move_row][move_col] = "-"
        if fishery_matrix[move_row][move_col] == "W":
            drown = True
            break
    elif input_info == "left":
        move_row, move_col = current_row + directions["left"][0], current_col + directions["left"][1]
        if move_col < 0:
            move_col = size_of_fishery - 1
        if fishery_matrix[move_row][move_col] != "W" and fishery_matrix[move_row][move_col] != "-":
            collected += fishery_matrix[move_row][move_col]
            fishery_matrix[move_row][move_col] = "-"
        if fishery_matrix[move_row][move_col] == "W":
            drown = True
            break
    elif input_info == "right":
        move_row, move_col = current_row + directions["right"][0], current_col + directions["right"][1]
        if move_col == size_of_fishery:
            move_col = 0
        if fishery_matrix[move_row][move_col] != "W" and fishery_matrix[move_row][move_col] != "-":
            collected += int(fishery_matrix[move_row][move_col])
            fishery_matrix[move_row][move_col] = "-"
        if fishery_matrix[move_row][move_col] == "W":
            drown = True
            break
    current_row, current_col = move_row, move_col
    input_info = input()

fishery_matrix[current_row][current_col] = "S"
if drown:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{move_row},{move_col}]")
    collected = 0
else:
    if collected >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected} tons of fish more.")
if collected > 0:
    print(f"Amount of fish caught: {collected} tons.")
if not drown:
    str_matrix = [[str(el) for el in row] for row in fishery_matrix]
    for row in str_matrix:
        print("".join(row))