def number_check(numbers):
    negative = 0
    positive = 0
    for num in numbers:
        if num > 0:
            positive += num
        else:
            negative += num
    if abs(negative) > positive:
        return f"{negative}\n{positive}\nThe negatives are stronger than the positives"
    else:
        return f"{negative}\n{positive}\nThe positives are stronger than the negatives"


array = [int(x) for x in input().split()]

print(number_check(array))
