def operate(sign, *args):
    list_of_args = list(args)
    result = 0
    if sign == "+":
        for number in args:
            result += number
    elif sign == "-":
        result = list_of_args.pop(0)
        for number in list_of_args:
            result -= number
    elif sign == "*":
        result = 1
        for number in list_of_args:
            result *= number
    else:
        popped_item = list_of_args.pop(0)
        if popped_item != 0:
            result = popped_item
            while len(list_of_args) > 0:
                result /= list_of_args.pop(0)
    return result


print(operate("/", 3, 4))