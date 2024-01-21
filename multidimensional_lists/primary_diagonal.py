matrix_size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(matrix_size)]

dia_sum = 0
for index in range(matrix_size):
    dia_sum += matrix[index][index]

print(dia_sum)