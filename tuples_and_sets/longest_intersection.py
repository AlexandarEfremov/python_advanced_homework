number_of_intersections = int(input())
intersection_list = []

for _ in range(number_of_intersections):
    set_one = set()
    set_two = set()
    first_info, second_info = input().split("-")
    first_start, first_end = first_info.split(",")
    second_start, second_end = second_info.split(",")
    for number in range(int(first_start), int(first_end) + 1):
        set_one.add(number)
    for numb in range(int(second_start), int(second_end) + 1):
        set_two.add(numb)
    intersection = set_one.intersection(set_two)
    intersection_list.append(list(intersection))

sorted_list = sorted(intersection_list, key=lambda x: -(len(x)))

print(f"Longest intersection is {sorted_list[0]} with length {len(sorted_list[0])}")