number = int(input())


def factorial_calc(num):
    if num == 1:
        return num
    return num * factorial_calc(num - 1)


print(factorial_calc(number))