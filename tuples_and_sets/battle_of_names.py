num_of_lines = int(input())
odd_set = set()
even_set = set()

for i in range(1, num_of_lines + 1):
    name_value = sum([ord(name) for name in input()]) // i
    if name_value % 2 != 0:
        odd_set.add(name_value)
    else:
        even_set.add(name_value)
odd_set_sum = sum(odd_set)
even_set_sum = sum(even_set)
if odd_set_sum == even_set_sum:
    print(*odd_set.union(even_set), sep=", ")
elif odd_set_sum > even_set_sum:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")