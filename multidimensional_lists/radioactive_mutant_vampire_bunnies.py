rows, cols = (int(x) for x in input().split())
initial_lair = []
current_position = []

for row in rows:
    line = input().split()
    initial_lair.append(line)
    if "P" in line:
        current_position = [row, initial_lair[row].index("P")]

commands = input()

directions = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

for command in commands:
    r, c = current_position[0] + directions[command][0], current_position[1] + directions[command][1]
    if not (0 <= r < rows and 0 <= c < rows):
        continue
    if initial_lair[r][c] == "B":
        break
    current_position = [r, c]


