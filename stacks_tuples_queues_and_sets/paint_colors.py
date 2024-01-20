from collections import deque
colour_string = deque(x for x in input().split())
main_colours = ["red", "yellow", "blue", "orange", "purple", "green"]
result = []

while colour_string:
    if len(colour_string) == 1:
        temp_result = colour_string.pop()
        if {temp_result}.issubset(main_colours):
            result.append(temp_result)
            break
        else:
            break
    left_string = colour_string.popleft()
    right_string = colour_string.pop() if colour_string else ''

    for colour in (left_string + right_string, right_string + left_string):
        if {colour}.issubset(main_colours):
            result.append(colour)
            break
    else:
        left_string_len, right_string_len = len(left_string), len(right_string)
        new_left, new_right = left_string[:left_string_len - 1], right_string[:right_string_len - 1]
        for el in (new_left, new_right):
            if el:
                colour_string.insert(len(colour_string) // 2, el)

for colour in result:
    if colour == "orange" and not {"red", "yellow"}.issubset(result):
        result.remove(colour)
    elif colour == "purple" and not {"red", "blue"}.issubset(result):
        result.remove(colour)
    elif colour == "green" and not {"yellow", "blue"}.issubset(result):
        result.remove(colour)
print(result)