rows, columns = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
for index in range(columns):
    temp_sum = 0
    for sub_matrix in matrix:
        temp_sum += sub_matrix[index]
    print(temp_sum)
