rows = int(input())
commands = [x for x in input().split()]

mine_matrix = [[x for x in input().split()] for _ in range(rows)]


def target_coordinates(target_element, matrix):
    for row_index, ro in enumerate(matrix):
        for col_index, element in enumerate(ro):
            if element == target_element:
                result = (row_index, col_index)
                return result


coals_in_matrix = sum(row.count("c") for row in mine_matrix)


starting_position = target_coordinates("s", mine_matrix)
ro_current, co_current = starting_position
break_cond = False
for com in commands:
    if com == "up":
        if ro_current - 1 >= 0:
            ro_current -= 1
        else:
            continue
    elif com == "down":
        if ro_current + 1 < rows:
            ro_current += 1
        else:
            continue
    elif com == "left":
        if co_current - 1 >= 0:
            co_current -= 1
        else:
            continue
    elif com == "right":
        if co_current + 1 < rows:
            co_current += 1
        else:
            continue
    if mine_matrix[ro_current][co_current] == "c":
        coals_in_matrix -= 1
        mine_matrix[ro_current][co_current] = "*"
    if mine_matrix[ro_current][co_current] == "e":
        break_cond = True
        break

if coals_in_matrix:
    if break_cond:
        print(f"Game over! ({ro_current}, {co_current})")
    else:
        print(f"{coals_in_matrix} pieces of coal left. ({ro_current}, {co_current})")
else:
    print(f"You collected all coal! ({ro_current}, {co_current})")