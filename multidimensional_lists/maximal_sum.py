rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float("-inf")
max_matrix = []

for i in range(rows - 2):
    for col in range(cols - 2):
        line_one = [matrix[i][col], matrix[i][col + 1], matrix[i][col + 2]]
        line_two = [matrix[i + 1][col], matrix[i + 1][col + 1], matrix[i + 1][col + 2]]
        line_three = [matrix[i + 2][col], matrix[i + 2][col + 1], matrix[i + 2][col + 2]]
        current_total = sum(line_one) + sum(line_two) + sum(line_three)
        if current_total > max_sum:
            max_sum = current_total
            max_matrix = [line_one, line_two, line_three]

print(f"Sum = {max_sum}")
[print(*x) for x in max_matrix]