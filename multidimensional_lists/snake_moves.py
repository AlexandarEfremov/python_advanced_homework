from collections import deque
rows, cols = [int(x) for x in input().split()]
snake_string = deque(input())

snake_path = []
for i in range(rows):
    current_word = ""
    for _ in range(cols):
        current_letter = snake_string.popleft()
        current_word += current_letter
        snake_string.append(current_letter)
    if i % 2 == 0:
        snake_path.append(current_word)
    else:
        snake_path.append(current_word[::-1])

[print(el, sep="\n") for el in snake_path]