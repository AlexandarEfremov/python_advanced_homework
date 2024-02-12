from collections import deque
time_to_complete_a_task = deque([int(x) for x in input().split()])
number_of_tasks = [int(x) for x in input().split()]

duck_dict = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while time_to_complete_a_task and number_of_tasks:
    current_time = time_to_complete_a_task.popleft()
    current_task = number_of_tasks.pop()
    result = current_time * current_task
    if 0 <= result <= 60:
        duck_dict["Darth Vader Ducky"] += 1
    elif 61 <= result <= 120:
        duck_dict["Thor Ducky"] += 1
    elif 121 <= result <= 180:
        duck_dict["Big Blue Rubber Ducky"] += 1
    elif 181 <= result <= 240:
        duck_dict["Small Yellow Rubber Ducky"] += 1
    else:
        current_task -= 2
        number_of_tasks.append(current_task)
        time_to_complete_a_task.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

[print(f"{key}: {value}") for key, value in duck_dict.items()]



