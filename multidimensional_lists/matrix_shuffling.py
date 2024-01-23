rows, cols = [int(x) for x in input().split()]
matrix = [[el for el in input().split()] for _ in range(rows)]

input_info = input()
while input_info != "END":
    if "swap" in input_info:
        data = input_info.split()
        if len(data) == 5:
            row_one, col_one, row_two, col_two = [int(data[i]) for i in range(1, 5)]
            if all(x >= 0 for x in [row_one, col_one, row_two, col_two]):
                if row_one <= rows and row_two <= rows and col_one <= cols and col_two <= cols:
                    matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][
                        col_one]
                    [print(*el) for el in matrix]
                else:
                    print("Invalid input!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    input_info = input()