size_of_matrix = int(input())
wonderland_matrix = []

alice_index = []
rabbit_index = []

for row in range(size_of_matrix):
    input_info = input().split()
    wonderland_matrix.append(input_info)
    if "A" in input_info:
        alice_index.extend([row, input_info.index("A")])
    elif "R" in input_info:
        rabbit_index.extend([row, input_info.index("R")])

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

total_tea_bags = 0
starting_row, starting_col = alice_index
wonderland_matrix[starting_row][starting_col] = "*"

current_row = starting_row
current_col = starting_col

while total_tea_bags < 10:
    commands_for_alice = input()
    if commands_for_alice == "up":
        current_row += directions["up"][0]
        current_col += directions["up"][1]
        if 0 <= current_row < size_of_matrix and 0 <= current_col < size_of_matrix:
            if wonderland_matrix[current_row][current_col].isdigit():
                total_tea_bags += int(wonderland_matrix[current_row][current_col])
                wonderland_matrix[current_row][current_col] = "*"
            elif wonderland_matrix[current_row][current_col] == "R":
                wonderland_matrix[current_row][current_col] = "*"
                print("Alice didn't make it to the tea party.")
                break
            else:
                wonderland_matrix[current_row][current_col] = "*"
        else:
            print("Alice didn't make it to the tea party.")
            break
    elif commands_for_alice == "down":
        current_row += directions["down"][0]
        current_col += directions["down"][1]
        if 0 <= current_row < size_of_matrix and 0 <= current_col < size_of_matrix:
            if wonderland_matrix[current_row][current_col].isdigit():
                total_tea_bags += int(wonderland_matrix[current_row][current_col])
                wonderland_matrix[current_row][current_col] = "*"
            elif wonderland_matrix[current_row][current_col] == "R":
                wonderland_matrix[current_row][current_col] = "*"
                print("Alice didn't make it to the tea party.")
                break
            else:
                wonderland_matrix[current_row][current_col] = "*"
        else:
            print("Alice didn't make it to the tea party.")
            break
    elif commands_for_alice == "left":
        current_row += directions["left"][0]
        current_col += directions["left"][1]
        if 0 <= current_row < size_of_matrix and 0 <= current_col < size_of_matrix:
            if wonderland_matrix[current_row][current_col].isdigit():
                total_tea_bags += int(wonderland_matrix[current_row][current_col])
                wonderland_matrix[current_row][current_col] = "*"
            elif wonderland_matrix[current_row][current_col] == "R":
                wonderland_matrix[current_row][current_col] = "*"
                print("Alice didn't make it to the tea party.")
                break
            else:
                wonderland_matrix[current_row][current_col] = "*"
        else:
            print("Alice didn't make it to the tea party.")
            break
    elif commands_for_alice == "right":
        current_row += directions["right"][0]
        current_col += directions["right"][1]
        if 0 <= current_row < size_of_matrix and 0 <= current_col < size_of_matrix:
            if wonderland_matrix[current_row][current_col].isdigit():
                total_tea_bags += int(wonderland_matrix[current_row][current_col])
                wonderland_matrix[current_row][current_col] = "*"
            elif wonderland_matrix[current_row][current_col] == "R":
                wonderland_matrix[current_row][current_col] = "*"
                print("Alice didn't make it to the tea party.")
                break
            else:
                wonderland_matrix[current_row][current_col] = "*"
        else:
            print("Alice didn't make it to the tea party.")
            break

if total_tea_bags >= 10:
    print("She did it! She went to the party.")
[print(*el) for el in wonderland_matrix]