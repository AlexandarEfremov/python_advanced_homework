numbers = [float(num) for num in input().split()]
numbers_dict = {}

for n in numbers:
    numbers_dict[n] = numbers_dict.get(n, 0) + 1
for key, value in numbers_dict.items():
    print(f"{key:.1f} - {value} times")