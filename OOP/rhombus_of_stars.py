n = int(input())


def print_row(size, star):
    print(f"{' ' * (size - star)}{'* ' * star}{' ' * (size - star)}")


def print_top(size):
    for star in range(1, size + 1):
        print_row(size, star)


def print_bottom(size):
    for star in range(size - 1, 0, -1):
        print_row(size, star)


def rhombus_printout(size):
    print_top(size)
    print_bottom(size)


rhombus_printout(n)