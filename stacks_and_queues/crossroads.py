from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())

car_deque = deque()
passed_cars = 0

info = input()

while info != "END":
    if info != "green":
        car_deque.append(info)
    else:
        current_green_light = green_light_duration

        while current_green_light > 0 and car_deque:
            car = car_deque.popleft()
            time = current_green_light + free_window_duration
            if len(car) > time:
                print(f"A crash happened!")
                print(f"{car} was hit at {car[time]}.")
                exit()
            current_green_light -= len(car)
            passed_cars += 1
    info = input()

print(f"Everyone is safe.")
print(f"{passed_cars} total cars passed the crossroads.")