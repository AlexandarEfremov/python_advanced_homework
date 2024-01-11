stack = [int(num) for num in input().split()]
for _ in range(len(stack)):
    last = stack.pop()
    print(last, end=" ")