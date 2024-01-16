n, m = map(int, input().split())
set_one = {int(input()) for _ in range(n)}
set_two = {int(input()) for _ in range(m)}

print(*(set_one.intersection(set_two)), sep="\n")