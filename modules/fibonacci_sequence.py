from modules.fibonacci_core import create_sequence, locate_number

command = input()

while command != "Stop":
    com, *details = command.split()

    if com == "Create":
        count = int(details[1])
        sequence = create_sequence(count)
        print(*sequence)
    elif com == "Locate":
        number = int(details[0])
        result = locate_number(number, sequence)
        print(result)
    command = input()
