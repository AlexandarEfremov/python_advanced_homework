from datetime import datetime, timedelta
from collections import deque

robot_data = [(robot_name, int(time)) for robot in input().split(";") for robot_name, time in [robot.split("-")]]
user_time = input()
current_time = datetime.strptime(user_time, "%H:%M:%S")


def increment(inc):
    increment_result = timedelta(seconds=inc)
    return increment_result


robot_dict = {}
for (name, time) in robot_data:
    robot_dict[name] = [time, 0]

products = deque()

while True:
    product_info = input()
    if product_info == "End":
        break
    products.append(product_info)

len_products = len(products)

while len_products > 0:
    product = products.popleft()
    current_time += increment(1)
    for robot, time in robot_dict.items():
        if robot_dict[robot][1] == 0:
            robot_dict[robot][1] = robot_dict[robot][0]
            tt = current_time.strftime('%H:%M:%S')
            print(robot + " - " + product + " [" + tt + "]")
            len_products -= 1
            robot_dict[robot][1] -= 1
            break
    else:
        products.append(product)
        for r, t in robot_dict.items():
            if robot_dict[r][1] != 0:
                robot_dict[r][1] -= 1
            else:
                continue




