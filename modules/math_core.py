sign_mapper = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "^": lambda a, b: a ** b
}


def execute_expression(exp):
    num_text, sign, num_two_text = exp.split()
    num_one = float(num_text)
    num_two = float(num_two_text)

    if sign in sign_mapper:
        operation = sign_mapper[sign]
        result = operation(num_one, num_two)
        return result

