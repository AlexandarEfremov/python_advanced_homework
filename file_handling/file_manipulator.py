import os

input_command = input()

while input_command != "End":
    instruction, *info = input_command.split("-")

    if instruction == "Create":
        with open(f"files/{info[0]}", "w"): pass
    elif instruction == "Add":
        with open(f"files/{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")
    elif instruction == "Replace":
        try:
            with open(f"files/{info[0]}", "r+") as file:
                text = file.read()
                text = text.replace(info[1], info[2])

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print("An error occurred")

    elif instruction == "Delete":
        try:
            os.remove(f"files/{info[0]}")
        except FileNotFoundError:
            print("An error occurred")
    input_command = input()