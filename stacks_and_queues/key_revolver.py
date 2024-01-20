from collections import deque

price_of_each_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(y) for y in input().split())
value_of_intelligence = int(input())

shot_bullets = 0
barrel = size_of_gun_barrel
while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft() if locks[0] >= current_bullet else print("Ping!")
    if current_lock is not None:
        barrel -= 1
        shot_bullets += 1
        print("Bang!")
    else:
        shot_bullets += 1
        barrel -= 1
    if barrel == 0 and len(bullets) > 0:
        barrel = size_of_gun_barrel
        print("Reloading!")

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence - (shot_bullets * price_of_each_bullet)}" )
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")