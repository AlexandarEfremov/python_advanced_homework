def squares(number: int):
    result = (number ** 2 for number in range(1, number + 1))
    return result


print(list(squares(5)))

#second solution with yield

def squares(number: int):
    start = 1
    while start <= number:
        yield start ** 2
        start += 1


print(list(squares(5)))