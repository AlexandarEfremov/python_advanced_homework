size_of_airspace = int(input())
airspace_matrix = []
plane_position = []

armor = 300
enemy_planes_count = 0

for row in range(size_of_airspace):
    line = [x for x in input()]
    airspace_matrix.append(line)
    if "J" in line:
        plane_position = [row, line.index("J")]
        airspace_matrix[plane_position[0]][plane_position[1]] = "-"
    if "E" in line:
        enemy_planes_count += line.count("E")

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

current_row, current_col = plane_position[0], plane_position[1]

while enemy_planes_count != 0 and armor > 0:
    move = input()
    move_row, move_col = current_row + directions[move][0], current_col + directions[move][1]
    if airspace_matrix[move_row][move_col] == "-":
        current_row, current_col = move_row, move_col
        continue
    if airspace_matrix[move_row][move_col] == "E":
        airspace_matrix[move_row][move_col] = "-"
        enemy_planes_count -= 1
        if enemy_planes_count == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            current_row, current_col = move_row, move_col
            airspace_matrix[current_row][current_col] = "J"
            break
        else:
            armor -= 100
            if armor <= 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{move_row}, {move_col}]!")
                current_row, current_col = move_row, move_col
                airspace_matrix[current_row][current_col] = "J"
                break
            else:
                current_row, current_col = move_row, move_col
                continue
    if airspace_matrix[move_row][move_col] == "R":
        airspace_matrix[move_row][move_col] = "-"
        current_row, current_col = move_row, move_col
        armor = 300


airspace_matrix = ["".join(el) for el in airspace_matrix]
print('\n'.join(airspace_matrix))