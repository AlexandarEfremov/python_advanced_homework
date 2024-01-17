set_one = {int(num) for num in input().split()}
set_two = {int(num) for num in input().split()}

for _ in range(int(input())):
    first_command, second_command, *data = input().split()
    command = first_command + " " + second_command
    if command == "Add First":
        [set_one.add(int(x)) for x in data]
    elif command == "Add Second":
        [set_two.add(int(x)) for x in data]
    elif command == "Remove First":
        [set_one.discard(int(x)) for x in data]
    elif command == "Remove Second":
        [set_two.discard(int(x)) for x in data]
    else:
        print(set_one.issubset(set_two) or set_two.issubset(set_one))

print(*sorted(set_one), sep=", ")
print(*sorted(set_two), sep=", ")

# solution 2

# set_one = {int(num) for num in input().split()}
# set_two = {int(num) for num in input().split()}
# num_of_commands = int(input())
#
# for _ in range(num_of_commands):
#     input_command = input().split()
#     if "Add" in input_command:
#         if "First" in input_command:
#             all_digis = [int(x) for x in input_command[2:]]
#             for digi in all_digis:
#                 set_one.add(digi)
#         else:
#             all_digis = [int(x) for x in input_command[2:]]
#             for digi in all_digis:
#                 set_two.add(digi)
#     elif "Remove" in input_command:
#         if "First" in input_command:
#             all_digis = [int(x) for x in input_command[2:]]
#             for digi in all_digis:
#                 if digi in set_one:
#                     set_one.remove(digi)
#         else:
#             all_digis = [int(x) for x in input_command[2:]]
#             for digi in all_digis:
#                 if digi in set_two:
#                     set_two.remove(digi)
#     elif "Check" in input_command:
#         is_subset_one = set_one.issubset(set_two)
#         is_subset_two = set_two.issubset(set_one)
#         if is_subset_one or is_subset_two:
#             print(True)
#         else:
#             print(False)
#
# print(*sorted(set_one), sep=", ")
# print(*sorted(set_two), sep=", ")
