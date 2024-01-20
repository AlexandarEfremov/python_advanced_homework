from collections import deque

total_honey = 0

worker_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
honey_symbols = deque(x for x in input().split())

while worker_bees and nectar:
    current_bee = worker_bees.popleft()
    current_nectar = nectar.pop()

    if current_bee > current_nectar:
        worker_bees.appendleft(current_bee)
        continue
    else:
        current_symbol = honey_symbols.popleft()
        if current_symbol == "+":
            current_honey = current_bee + current_nectar
            total_honey += current_honey
        elif current_symbol == "-":
            current_honey = abs(current_bee - current_nectar)
            total_honey += current_honey
        elif current_symbol == "*":
            current_honey = current_bee * current_nectar
            total_honey += current_honey
        elif current_symbol == "/":
            if current_nectar == 0:
                continue
            else:
                current_honey = current_bee / current_nectar
                total_honey += current_honey

print(f"Total honey made: {total_honey}")
if worker_bees:
    bee = ", ".join(map(str, worker_bees))
    print(f"Bees left: {bee}")
if nectar:
    nec = ", ".join(map(str, nectar))
    print(f"Nectar left: {nec}")