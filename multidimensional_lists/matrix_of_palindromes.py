rows, cols = [int(x) for x in input().split()]
first_ascii = 97

new_matrix = []

for row in range(rows):
    matrix_line = [f"{chr(first_ascii + row)}{chr(i + row)}{chr(first_ascii + row)}" for i in range(97, 97 + cols)]
    new_matrix.append(matrix_line)

[print(*x) for x in new_matrix]