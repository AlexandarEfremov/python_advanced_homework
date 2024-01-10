from collections import deque
kids_names = deque(input().split())
leave_count = int(input()) - 1

while len(kids_names) > 1:
    kids_names.rotate(- leave_count)
    removed_kid = kids_names.popleft()
    print(f"Removed {removed_kid}")
print(f"Last is {kids_names[0]}")