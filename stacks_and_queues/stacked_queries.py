number_of_inputs = int(input())
stack = []

for i in range(number_of_inputs):
    command_info = input().split()
    if command_info[0] == "1":
        number_to_push = int(command_info[1])
        stack.append(number_to_push)
    elif command_info[0] == "2":
        if stack:
            stack.pop()
        else:
            continue
    elif command_info[0] == "3":
        if stack:
            max_number_in_stack = max(stack)
            print(max_number_in_stack)
        else:
            continue
    elif command_info[0] == "4":
        if stack:
            min_number_in_stack = min(stack)
            print(min_number_in_stack)
        else:
            continue

reversed_stack = stack[::-1]
print(", ".join(map(str, reversed_stack)))

