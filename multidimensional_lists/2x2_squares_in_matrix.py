rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

count = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        first_el = matrix[i][j]
        second_el = matrix[i][j + 1]
        first_below = matrix[i + 1][j]
        second_below = matrix[i + 1][j + 1]

        if all(x == first_el for x in [second_el, first_below, second_below]):
            count += 1
if count:
    print(count)
else:
    print(0)
