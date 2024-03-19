def genrange(start: int, end: int):
    result = (int(x) for x in range(start, end + 1))
    return result

print(list(genrange(1, 10)))