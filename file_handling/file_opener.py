file_name = "text.txt"

try:
    file = open(file_name)
    print("File found")
except FileNotFoundError:
    print("File is not found")