from collections import deque
current_queue = deque([])
while True:
    input_info = input()
    if input_info == "End":
        print(f"{len(current_queue)} people remaining.")
        break
    elif input_info == "Paid":
        while current_queue:
            print(current_queue.popleft())
    else:
        current_queue.append(input_info)
