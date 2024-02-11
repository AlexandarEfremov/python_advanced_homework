rows, cols = [int(x) for x in input().split()]
block_matrix = []
starting_position = []

for row in range(rows):
    input_line = [x for x in input()]
    block_matrix.append(input_line)
    if "B" in input_line:
        starting_position = [row, input_line.index("B")]

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

current_row, current_col = starting_position[0], starting_position[1]

while True:
    command = input()
    current_row += directions[command][0]
    current_col += directions[command][1]

    if not 0 <= current_row < rows or not 0 <= current_col < cols:
        print("The delivery is late. Order is canceled.")
        block_matrix[starting_position[0]][starting_position[1]] = " "
        break
    if block_matrix[current_row][current_col] == '*':
        current_row -= directions[command][0]
        current_col -= directions[command][1]
    if block_matrix[current_row][current_col] == '-':
        block_matrix[current_row][current_col] = '.'

    if block_matrix[current_row][current_col] == 'P':
        block_matrix[current_row][current_col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")

    if block_matrix[current_row][current_col] == 'A':
        block_matrix[current_row][current_col] = 'P'
        print("Pizza is delivered on time! Next order...")
        break

print('\n'.join([''.join(el) for el in block_matrix]))




