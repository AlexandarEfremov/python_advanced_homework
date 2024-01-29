count_of_presents = int(input())
size_of_neighborhood = int(input())
santa_matrix = []
santa_position = []

nice_kids = 0
nice_kids_visited = 0

for row in range(size_of_neighborhood):
    input_info = input().split()
    santa_matrix.append(input_info)
    if "S" in input_info:
        santa_position = [row, input_info.index("S")]
        santa_matrix[row][santa_position[1]] = "-"
    if "V" in input_info:
        nice_kids += input_info.count("V")

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def find_a_cookie(presents_left, nice):
    for coord in directions.values():
        r = santa_position[0] + coord[0]
        c = santa_position[1] + coord[1]

        if santa_matrix[r][c].isalpha():
            if santa_matrix[r][c] == "V":
                nice += 1
            santa_matrix[r][c] = "-"
            presents_left -= 1
        if not presents_left:
            break
    return presents_left, nice


command = input()

while command != "Christmas morning":
    santa_position = [
        santa_position[0] + directions[command][0],
        santa_position[1] + directions[command][1]
    ]

    temp_value = santa_matrix[santa_position[0]][santa_position[1]]
    if temp_value == "V":
        nice_kids_visited += 1
        count_of_presents -= 1
    elif temp_value == "C":
        count_of_presents, nice_kids_visited = find_a_cookie(count_of_presents, nice_kids_visited)
    santa_matrix[santa_position[0]][santa_position[1]] = "-"

    if not count_of_presents or nice_kids_visited == nice_kids:
        break
    command = input()

santa_matrix[santa_position[0]][santa_position[1]] = "S"

if not count_of_presents and nice_kids_visited < nice_kids:
    print('Santa ran out of presents!')
[print(*line) for line in santa_matrix]

if nice_kids == nice_kids_visited:
    print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids - nice_kids_visited} nice kid/s.')


