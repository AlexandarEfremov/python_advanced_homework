from collections import deque

people_queue = deque()
total_litres = int(input())
while True:
    input_info = input()
    if input_info == "Start":
        break
    else:
        people_queue.append(input_info)

while True:
    input_command = input()
    if input_command == "End":
        break
    elif "refill" in input_command:
        top_up = int(input_command.split()[1])
        total_litres += top_up
    else:
        desired_litres = int(input_command)
        if desired_litres <= total_litres:
            person_in_line = people_queue.popleft()
            total_litres -= desired_litres
            print(f"{person_in_line} got water")
        else:
            person_in_line = people_queue.popleft()
            print(f"{person_in_line} must wait")
print(f"{total_litres} liters left")