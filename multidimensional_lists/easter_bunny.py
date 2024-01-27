size_of_field = int(input())
bunny_matrix = [[int(x) if not x.isalpha() else x for x in input().split()] for _ in range(size_of_field)]

bunny_position = []

for row_index, row in enumerate(bunny_matrix):
    for col_index, col in enumerate(row):
        if col == "B":
            bunny_position.extend([row_index, col_index])
            break

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

max_collection = 0
best_direction = ""
best_collection = []

for direction, coordinates in directions.items():
    current_collection = []
    current_max = 0
    r, c = bunny_position
    current_row = r + coordinates[0]
    current_col = c + coordinates[1]

    while 0 <= current_row < size_of_field and 0 <= current_col < size_of_field:
        if bunny_matrix[current_row][current_col] == "X":
            break
        current_max += bunny_matrix[current_row][current_col]
        current_collection.append([current_row, current_col])
        current_row += coordinates[0]
        current_col += coordinates[1]

    if abs(current_max) >= max_collection:
        max_collection = current_max
        best_direction = direction
        best_collection = current_collection

print(best_direction)
[print(item) for item in best_collection]
print(max_collection)

