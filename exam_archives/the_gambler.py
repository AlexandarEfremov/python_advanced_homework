size_of_matrix = int(input())
gambling_matrix = []
gambler_position = []

for row in range(size_of_matrix):
    line = [x for x in input()]
    gambling_matrix.append(line)
    if "G" in line:
        gambler_position.extend([row, line.index("G")])
        gambling_matrix[row][line.index("G")] = "-"

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

account = 100
command_input = input()
current_row, current_col = gambler_position[0], gambler_position[1]
jackpot = False
total_loss = False

while command_input != "end":
    move_row, move_col = current_row + directions[command_input][0], current_col + directions[command_input][1]
    if not (0 <= move_row < size_of_matrix) or not (0 <= move_col < size_of_matrix):
        total_loss = True
        break
    if account <= 0:
        total_loss = True
        break
    if gambling_matrix[move_row][move_col] == "-":
        pass
    elif gambling_matrix[move_row][move_col] == "P":
        account -= 200
        gambling_matrix[move_row][move_col] = "-"
        if account <= 0:
            total_loss = True
            break
    elif gambling_matrix[move_row][move_col] == "W":
        account += 100
        gambling_matrix[move_row][move_col] = "-"
    elif gambling_matrix[move_row][move_col] == "J":
        account += 100000
        gambling_matrix[move_row][move_col] = "-"
        jackpot = True
        current_row, current_col = move_row, move_col
        break
    current_row, current_col = move_row, move_col
    command_input = input()

gambling_matrix[current_row][current_col] = "G"
if total_loss:
    print("Game over! You lost everything!")
else:
    if jackpot:
        print(f"You win the Jackpot!\n End of the game. Total amount: {account}$")
        new_matrix = [''.join(el)for el in gambling_matrix]
        print(*new_matrix, sep="\n")
    else:
        print(f"End of the game. Total amount: {account}$")
        new_matrix = [''.join(el) for el in gambling_matrix]
        print(*new_matrix, sep="\n")


