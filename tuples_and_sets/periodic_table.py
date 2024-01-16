# count_of_input_lines = int(input())
# chem_set = set()
# for _ in range(count_of_input_lines):
#     chem = input().split()
#     for el in chem:
#         chem_set.add(el)
# print(*chem_set, sep="\n")

chem_set = {el for _ in range(int(input())) for el in input().split()}
print(*chem_set, sep="\n")


