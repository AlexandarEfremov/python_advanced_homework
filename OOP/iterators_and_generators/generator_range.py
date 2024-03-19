def genrange(start: int, end: int):
    result = (int(x) for x in range(start, end + 1))
    return result

print(list(genrange(1, 10)))

#second solution with yield


def genrange(start: int, end: int):
    while start <= end:
        yield start
        start += 1

print(list(genrange(1, 10)))