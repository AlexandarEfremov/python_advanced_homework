size_of_matrix = int(input())
racing_number = input()
racing_matrix = []
current_row, current_col = [0, 0]
km_passed = 0


directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

tunnel_start = []
tunnel_end = []

for row in range(size_of_matrix):
    line = [x for x in input().split()]
    racing_matrix.append(line)


def find_end(matrix):
    for index, row in enumerate(matrix):
        if "T" in row:
            position = [index, row.index("T")]
            return position


command_input = input()
finish = False
while command_input != "End":
    move_row, move_col = current_row + directions[command_input][0], current_col + directions[command_input][1]
    if racing_matrix[move_row][move_col] == "F":
        km_passed += 10
        print(f"Racing car {racing_number} finished the stage!")
        finish = True
        break
    if racing_matrix[move_row][move_col] == ".":
        km_passed += 10
    if racing_matrix[move_row][move_col] == "T":
        km_passed += 30
        racing_matrix[move_row][move_col] = "."
        current_row, current_col = find_end(racing_matrix)
        racing_matrix[current_row][current_col] = "."
        command_input = input()
        continue


    current_row, current_col = move_row, move_col
    command_input = input()

racing_matrix[move_row][move_col] = "C"
if not finish:
    print(f"Racing car {racing_number} DNF.")
print(f"Distance covered {km_passed} km.")

racing_matrix = ["".join(el) for el in racing_matrix]
print("\n".join(racing_matrix))


