# from collections import deque
#
# total_honey = 0
#
# worker_bees = deque(int(x) for x in input().split())
# nectar = deque(int(x) for x in input().split())
# honey_symbols = deque(x for x in input().split())
#
# while worker_bees and nectar:
#     current_bee = worker_bees.popleft()
#     current_nectar = nectar.pop()
#
#     if current_bee > current_nectar:
#         worker_bees.appendleft(current_bee)
#         continue
#     else:
#         current_symbol = honey_symbols.popleft()
#         if current_symbol == "+":
#             current_honey = current_bee + current_nectar
#             total_honey += current_honey
#         elif current_symbol == "-":
#             current_honey = abs(current_bee - current_nectar)
#             total_honey += current_honey
#         elif current_symbol == "*":
#             current_honey = current_bee * current_nectar
#             total_honey += current_honey
#         elif current_symbol == "/":
#             if current_nectar == 0:
#                 continue
#             else:
#                 current_honey = current_bee / current_nectar
#                 total_honey += current_honey
#
# print(f"Total honey made: {total_honey}")
# if worker_bees:
#     bee = ", ".join(map(str, worker_bees))
#     print(f"Bees left: {bee}")
# if nectar:
#     nec = ", ".join(map(str, nectar))
#     print(f"Nectar left: {nec}")

# second solution

from collections import deque
working_bees = deque(int(x) for x in input().split())
nectar_input = [int(y) for y in input().split()]
symbols = deque(input().split())

total_honey = 0

while working_bees and nectar_input:
    current_bee = working_bees.popleft()
    current_nectar = nectar_input.pop()
    if current_bee > current_nectar:
        working_bees.appendleft(current_bee)
        continue
    else:
        current_symbol = symbols.popleft()
        functions = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b if b != 0 else 0
        }

        total_honey += abs(functions[current_symbol](current_bee, current_nectar))

print(f"Total honey made: {total_honey}")
if working_bees:
    bee = ", ".join(map(str, working_bees))
    print(f"Bees left: {bee}")
if nectar_input:
    nec = ", ".join(map(str, nectar_input))
    print(f"Nectar left: {nec}")