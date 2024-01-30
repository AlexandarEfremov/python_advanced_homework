def even_odd(*args):
    command = args[-1]
    args = args[:-1]

    def even():
        return [num for num in args if num % 2 == 0]

    def odd():
        return [num for num in args if num % 2 != 0]

    if command == "even":
        return even()
    else:
        return odd()


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))