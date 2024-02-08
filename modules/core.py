def print_triangle(n):
    print_top(n)
    print_bottom(n)


def print_top(n):
    for row in range(1, n + 1):
        for num in range(1, row + 1):
            print(num, end=" ")
        print()


def print_bottom(n):
    for row in range(n, 0, -1):
        for num in range(1, row):
            print(num, end=" ")
        print()
