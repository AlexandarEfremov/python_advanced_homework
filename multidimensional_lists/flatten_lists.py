matrix = [x for x in input().split("|")]
flatten = (y.split() for y in matrix[::-1])
[[print(inside_el, end=" ") for inside_el in el] for el in flatten]