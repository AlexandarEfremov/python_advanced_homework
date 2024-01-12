from collections import deque

petrol_pump_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
petrol_pump_data_copy = petrol_pump_data.copy()

gas_in_tank = 0
index = 0

while petrol_pump_data_copy:
    petrol, distance = petrol_pump_data_copy.popleft()

    gas_in_tank += petrol
    if gas_in_tank >= distance:
        gas_in_tank -= distance

    else:
        petrol_pump_data.rotate(-1)
        petrol_pump_data_copy = petrol_pump_data.copy()
        index += 1
        gas_in_tank = 0
print(index)