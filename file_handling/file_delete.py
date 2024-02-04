import os

try:
    path = os.path.join("text.txt")
    os.remove(path)
except FileNotFoundError:
    print("File is already deleted")
