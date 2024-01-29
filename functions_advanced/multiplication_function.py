def multiply(*args):
    total_multi = 1
    for el in args:
        total_multi *= el
    return total_multi

print(multiply(2, 0, 1000, 5000))