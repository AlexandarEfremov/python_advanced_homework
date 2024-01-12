stack_of_clothes = [int(x) for x in input().split()]
hanger_cap = int(input())
current_hanger_cap = hanger_cap
hanger_count = 1

stack_of_clothes.reverse()
for clothes in stack_of_clothes.copy():
    if current_hanger_cap >= clothes:
        current_hanger_cap -= clothes
    else:
        hanger_count += 1
        current_hanger_cap = hanger_cap
        current_hanger_cap -= clothes

print(hanger_count)