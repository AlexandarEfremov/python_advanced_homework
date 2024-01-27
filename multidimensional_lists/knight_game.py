matrix_size = int(input())
knight_matrix = [list(input()) for _ in range(matrix_size)]
knight_moves = (
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
)

removed_knights = 0
while True:
    max_attack = 0
    max_attack_knight_pos = []

    for row in range(matrix_size):
        for col in range(matrix_size):
            if knight_matrix[row][col] == "K":
                attacks = 0

                for position in knight_moves:
                    current_row = row + position[0]
                    current_col = col + position[1]

                    if 0 <= current_row < matrix_size and 0 <= current_col < matrix_size:
                        if knight_matrix[current_row][current_col] == "K":
                            attacks += 1
                if attacks > max_attack:
                    max_attack = attacks
                    max_attack_knight_pos = [row, col]
    if max_attack_knight_pos:
        r, c = max_attack_knight_pos
        knight_matrix[r][c] = "0"
        removed_knights += 1
    else:
        break
print(removed_knights)