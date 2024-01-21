rows, columns = [int(x) for x in input().split(', ')]
array = [[int(x) for x in input().split(", ")] for _ in range(rows)]
array_sum = sum(sum(x) for x in array)
print(array_sum)
print(array)