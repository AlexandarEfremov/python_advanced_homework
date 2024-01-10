expression_input = input()
paren_expression = []

for index in range(len(expression_input)):
    if expression_input[index] == "(":
        paren_expression.append(index)
    elif expression_input[index] == ")":
        start_index = paren_expression.pop()
        end_index = index + 1
        text = expression_input[start_index:end_index]
        print(text)

