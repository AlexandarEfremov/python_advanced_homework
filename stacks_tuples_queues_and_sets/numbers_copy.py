set_one = {int(num) for num in input().split()}
set_two = {int(num) for num in input().split()}
num_of_commands = int(input())

for _ in range(num_of_commands):
    input_command = input().split()
    if "Add" in input_command:
        if "First" in input_command:
            all_digis = [int(x) for x in input_command[2:]]
            for digi in all_digis:
                set_one.add(digi)
        else:
            all_digis = [int(x) for x in input_command[2:]]
            for digi in all_digis:
                set_two.add(digi)
    elif "Remove" in input_command:
        if "First" in input_command:
            all_digis = [int(x) for x in input_command[2:]]
            for digi in all_digis:
                if digi in set_one:
                    set_one.remove(digi)
        else:
            all_digis = [int(x) for x in input_command[2:]]
            for digi in all_digis:
                if digi in set_two:
                    set_two.remove(digi)
    elif "Check" in input_command:
        is_subset_one = set_one.issubset(set_two)
        is_subset_two = set_two.issubset(set_one)
        if is_subset_one or is_subset_two:
            print(True)
        else:
            print(False)

print(*sorted(set_one), sep=", ")
print(*sorted(set_two), sep=", ")
