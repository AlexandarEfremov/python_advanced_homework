input_data = [x for x in input()]
reversed_string = ''
for _ in range(len(input_data)):
    popped_letter = input_data.pop()
    reversed_string += popped_letter
print(reversed_string)