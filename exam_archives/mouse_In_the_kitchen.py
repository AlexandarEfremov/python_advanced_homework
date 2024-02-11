rows, cols = [int(x) for x in input().split(",")]
mouse_matrix = []
mouse_position = []
total_cheese = 0

for row in range(rows):
    line = [x for x in input()]
    mouse_matrix.append(line)
    if "M" in line:
        mouse_position = [row, line.index("M")]
        mouse_matrix[mouse_position[0]][mouse_position[1]] = "*"
    if "C" in line:
        for letter in line:
            if letter == "C":
                total_cheese += 1


directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

current_row, current_col = mouse_position[0], mouse_position[1]


while True:
    command = input()
    if command == "danger":
        if total_cheese > 0:
            mouse_matrix[current_row][current_col] = "M"
            print("Mouse will come back later!")
        break
    move_row, move_col = current_row + directions[command][0], current_col + directions[command][1]

    if move_row < 0 or move_row >= rows or move_col < 0 or move_col >= cols:
        mouse_matrix[current_row][current_col] = "M"
        print("No more cheese for tonight!")
        break
    if mouse_matrix[move_row][move_col] == "C":
        mouse_matrix[move_row][move_col] = "*"
        total_cheese -= 1
        if total_cheese == 0:
            mouse_matrix[move_row][move_col] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    if mouse_matrix[move_row][move_col] == "T":
        mouse_matrix[move_row][move_col] = "M"
        print("Mouse is trapped!")
        break
    if mouse_matrix[move_row][move_col] == "@":
        continue
    if mouse_matrix[move_row][move_col] == "*":
        pass
    current_row, current_col = move_row, move_col

[print("".join(line)) for line in mouse_matrix]