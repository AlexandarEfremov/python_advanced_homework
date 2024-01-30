# def rectangle(*args):
#     for i in args:
#         if not isinstance(i, int):
#             return "Enter valid values!"
#     length, width = args
#     area = length * width
#     perimeter = 2 * (length + width)
#     answer = f"""Rectangle area: {area}
# Rectangle perimeter: {perimeter}"""
#     return answer


# second solution

def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return length * width

    def per():
        return 2 * (length + width)

    return f"Rectangle area: {area()}\nRectangle perimeter: {per()}"

print(rectangle(2, 10))