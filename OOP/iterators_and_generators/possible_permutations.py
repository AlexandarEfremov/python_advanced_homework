from itertools import permutations


def possible_permutations(perm_list):
    for perm in permutations(perm_list):
        yield list(perm)

[print(n) for n in possible_permutations([1])]
