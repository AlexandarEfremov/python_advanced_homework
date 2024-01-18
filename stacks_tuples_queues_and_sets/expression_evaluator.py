# from collections import deque
#
# string_input = deque(input().split())
# working_string = string_input.copy()
# current_sum = []
#
# for element in string_input:
#     current_element = working_string.popleft()
#     if current_element == "+":
#         temp_sum = sum(current_sum)
#         current_sum.clear()
#         current_sum.append(temp_sum)
#     elif current_element == "-" and len(current_element) == 1:
#         temp_value = current_sum[0]
#         while len(current_sum) > 1:
#             current_detractor = current_sum.pop()
#             temp_value -= current_detractor
#         current_sum.clear()
#         current_sum.append(temp_value)
#     elif current_element == "*":
#         temp_multi = current_sum[0]
#         while len(current_sum) > 1:
#             current_multi = current_sum.pop()
#             temp_multi *= current_multi
#         current_sum.clear()
#         current_sum.append(temp_multi)
#     elif current_element == "/":
#         temp_div = current_sum[0]
#         while len(current_sum) > 1:
#             current_div = current_sum.pop()
#             temp_div = temp_div // current_div
#         current_sum.clear()
#         current_sum.append(temp_div)
#     else:
#         current_sum.append(int(current_element))
# print(*current_sum)

# second solution

from functools import reduce
string_input = input().split()
copy_string = string_input.copy()
curr_sum = []

for el in copy_string:
    if el == "+":
        temp_sum = (reduce(lambda a, b: a + b, curr_sum))
        curr_sum.clear()
        curr_sum.append(temp_sum)
    elif el == "-":
        temp_sum = (reduce(lambda a, b: a - b, curr_sum))
        curr_sum.clear()
        curr_sum.append(temp_sum)
    elif el == "*":
        temp_sum = (reduce(lambda a, b: a * b, curr_sum))
        curr_sum.clear()
        curr_sum.append(temp_sum)
    elif el == "/":
        temp_sum = (reduce(lambda a, b: a // b, curr_sum))
        curr_sum.clear()
        curr_sum.append(temp_sum)
    else:
        curr_sum.append(int(el))

print(*curr_sum)