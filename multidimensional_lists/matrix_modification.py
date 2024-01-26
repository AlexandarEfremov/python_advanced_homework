matrix = [[int(x) for x in input().split()] for i in range(int(input()))]
input_command = input()
while input_command != "END":
    instructions = input_command.split()
    command, add_row, add_col, add_value = instructions[0], int(instructions[1]), int(instructions[2]), int(instructions[3])
    if command == "Add" and 0 <= add_row < len(matrix) and 0 <= add_col < len(matrix):
        matrix[add_row][add_col] += add_value
    elif command == "Subtract" and 0 <= add_row < len(matrix) and 0 <= add_col < len(matrix):
        matrix[add_row][add_col] -= add_value
    else:
        print("Invalid coordinates")
    input_command = input()

[print(*el) for el in matrix]