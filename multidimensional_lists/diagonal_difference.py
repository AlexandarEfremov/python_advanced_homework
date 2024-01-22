matrix_size = int(input())
matrix = [[int(x) for x in input().split()] for index in range(matrix_size)]
first_dia = sum([matrix[i][i] for i in range(matrix_size)])
second_dia = sum([matrix[i][matrix_size - i - 1] for i in range(matrix_size)])
diff = abs(first_dia - second_dia)
print(diff)