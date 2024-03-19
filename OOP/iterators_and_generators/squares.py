def squares(number: int):
    result = (number ** 2 for number in range(1, number + 1))
    return result


print(list(squares(5)))