from collections import deque

price_of_each_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
bullets.reverse()
locks = [int(y) for y in input().split()]
value_of_intelligence = int(input())

deq_bullets = deque(bullets)
deq_locks = deque(locks)

add = 0
while True:
    add += 1
