def valid_coordinates(first, second):
    if 0 <= first < 5 and 0 <= second < 5:
        return True
    return False


size = 5
range_matrix = []
player_position = []
targets_left = 0
targets_hit = 0
target_hit_positions = []

for row in range(size):
    input_info = input().split()
    range_matrix.append(input_info)
    if "A" in input_info:
        player_position = [row, input_info.index("A")]
    if "x" in input_info:
        targets_left += input_info.count("x")

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for i in range(int(input())):
    command = input().split()

    if "move" in command:
        direction, steps = command[1], int(command[2])
        pos_one, pos_two = player_position

        r, c = directions[direction]

        for step in range(steps):
            pos_one += r
            pos_two += c
            if valid_coordinates(pos_one, pos_two):
                if step == (steps - 1) and range_matrix[pos_one][pos_two] == "x":
                    continue
                else:
                    player_position = [pos_one, pos_two]

    elif "shoot" in command:
        direction = command[1]
        pos_one, pos_two = player_position
        r, c = directions[direction]

        while True:
            pos_one += r
            pos_two += c

            if valid_coordinates(pos_one, pos_two):
                if range_matrix[pos_one][pos_two] == ".":
                    continue
                elif range_matrix[pos_one][pos_two] == "x":
                    targets_left -= 1
                    targets_hit += 1
                    target_hit_positions.append([pos_one, pos_two])
                    range_matrix[pos_one][pos_two] = "."
                    break
            else:
                break

        if not targets_left:
            print(f"Training completed! All {targets_hit} targets hit.")
            break

if targets_left:
    print(f"Training not completed! {targets_left} targets left.")

print(*target_hit_positions, sep='\n')
