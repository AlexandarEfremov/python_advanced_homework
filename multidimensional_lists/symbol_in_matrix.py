row = int(input())
matrix = [[x for x in input()] for _ in range(row)]
special_symbol = input()

result = ''
for row_index, row in enumerate(matrix):
    for col_index, element in enumerate(row):
        if matrix[row_index][col_index] == special_symbol:
            result = (row_index, col_index)
            print(result)
            exit()
else:
    print(f"{special_symbol} does not occur in the matrix")

