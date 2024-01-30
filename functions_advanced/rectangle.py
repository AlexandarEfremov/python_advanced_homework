def rectangle(*args):
    for i in args:
        if not isinstance(i, int):
            return "Enter valid values!"
    length, width = args
    area = length * width
    perimeter = 2 * (length + width)
    answer = f"""Rectangle area: {area}
Rectangle perimeter: {perimeter}"""
    return answer

print(rectangle('2', 10))