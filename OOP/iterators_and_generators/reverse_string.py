def reverse_text(string: str):
    rev_string = reversed(string)
    for char in rev_string:
        yield char


for char in reverse_text("step"):
    print(char, end='')