number_of_commands = int(input())
car_list = []
for i in range(number_of_commands):
    direction, reg = input().split()
    if direction == "IN,":
        car_list.append(reg)
    elif direction == "OUT,":
        if reg in car_list:
            car_list.remove(reg)
if not car_list:
    print("Parking Lot is Empty")
else:
    for car in set(car_list):
        print(car)