matrix_size = int(input())
matrix = [[int(x) for x in input().split(", ")] for index in range(matrix_size)]

first_dia = [matrix[index][index] for index in range(matrix_size)]
second_dia = []

first_index = 0
second_index = matrix_size - 1

for i in range(matrix_size):
    current_matrix = matrix[first_index][second_index]
    second_dia.append(current_matrix)

    first_index += 1
    second_index -= 1

print(f"Primary diagonal: {', '.join(map(str, first_dia))}. Sum: {sum(first_dia)}")
print(f"Secondary diagonal: {', '.join(map(str, second_dia))}. Sum: {sum(second_dia)}")
