matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
bombs = [[int(x) for x in item.split(",")] for item in input().split()]

temp_matrix = matrix.copy()


def bomb_aftermath(coordinates, matrix_in_use):
    detonation_row, detonation_col = [int(x) for x in coordinates]
    detonation_value = matrix_in_use[detonation_row][detonation_col]

    if matrix_in_use[detonation_row][detonation_col] <= 0:
        return matrix_in_use
    else:
        matrix_in_use[detonation_row][detonation_col] = 0

    if detonation_row - 1 >= 0 and matrix_in_use[detonation_row - 1][detonation_col] > 0:
        matrix_in_use[detonation_row - 1][detonation_col] -= detonation_value

    if detonation_row + 1 < len(matrix_in_use) and matrix_in_use[detonation_row + 1][detonation_col] > 0:
        matrix_in_use[detonation_row + 1][detonation_col] -= detonation_value
    if detonation_col - 1 >= 0 and matrix_in_use[detonation_row][detonation_col - 1] > 0:
        matrix_in_use[detonation_row][detonation_col - 1] -= detonation_value
    if detonation_col + 1 < len(matrix_in_use[detonation_row]) and matrix_in_use[detonation_row][detonation_col + 1] \
            > 0:
        matrix_in_use[detonation_row][detonation_col + 1] -= detonation_value

    if detonation_row - 1 >= 0 and detonation_col - 1 >= 0 and matrix_in_use[detonation_row - 1][detonation_col - 1] \
            > 0:
        matrix_in_use[detonation_row - 1][detonation_col - 1] -= detonation_value

    if detonation_row - 1 >= 0 and detonation_col + 1 < len(matrix_in_use[detonation_row]) and \
            matrix_in_use[detonation_row - 1][detonation_col + 1] > 0:
        matrix_in_use[detonation_row - 1][detonation_col + 1] -= detonation_value

    if detonation_row + 1 < len(matrix_in_use) and detonation_col - 1 >= 0 and \
            matrix_in_use[detonation_row + 1][detonation_col - 1] > 0:
        matrix_in_use[detonation_row + 1][detonation_col - 1] -= detonation_value

    if detonation_row + 1 < len(matrix_in_use) and detonation_col + 1 < len(matrix_in_use[detonation_row]) and \
            matrix_in_use[detonation_row + 1][detonation_col + 1] > 0:
        matrix_in_use[detonation_row + 1][detonation_col + 1] -= detonation_value

    return matrix_in_use


for bomb in bombs:
    temp_matrix = bomb_aftermath(bomb, temp_matrix)

active_cells = 0
for row in temp_matrix:
    for cell in row:
        if cell > 0:
            active_cells += 1

sum_cells = 0
for row in temp_matrix:
    for cell in row:
        if cell > 0:
            sum_cells += cell

print(f"Alive cells: {active_cells}")
print(f"Sum: {sum_cells}")

[print(*item) for item in temp_matrix]