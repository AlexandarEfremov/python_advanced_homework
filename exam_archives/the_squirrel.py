size_of_field = int(input())
squirrel_matrix = []
squirrel_position = []
move_commands = [command for command in input().split(", ")]
for row in range(size_of_field):
    line = [x for x in input()]
    squirrel_matrix.append(line)
    if "s" in line:
        squirrel_position = [row, line.index("s")]

total_hazelnuts = 0

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}
current_row, current_col = squirrel_position

for direction in move_commands:
    if total_hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        print(f"Hazelnuts collected: {total_hazelnuts}")
        exit()
    move_row, move_col = current_row + directions[direction][0], current_col + directions[direction][1]
    if move_row < 0 or move_row == size_of_field or move_col < 0 or move_col == size_of_field:
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {total_hazelnuts}")
        exit()
    if squirrel_matrix[move_row][move_col] == "h":
        squirrel_matrix[move_row][move_col] = "*"
        total_hazelnuts += 1
    if squirrel_matrix[move_row][move_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {total_hazelnuts}")
        exit()
    if squirrel_matrix[move_row][move_col] == "*":
        pass
    current_row, current_col = move_row, move_col
if total_hazelnuts < 3:
    print("There are more hazelnuts to collect.")
else:
    print("Good job! You have collected all hazelnuts!")

print(f"Hazelnuts collected: {total_hazelnuts}")

