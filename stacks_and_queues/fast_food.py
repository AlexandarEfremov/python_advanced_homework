from queue import Queue
quantity_of_food = int(input())
orders = [int(x) for x in input().split()]
print(max(orders))
my_queue = Queue()
for order in orders:
    my_queue.put(order)

remaining_quantity = quantity_of_food

while not my_queue.empty() and remaining_quantity >= my_queue.queue[0]:
    current_order = my_queue.get()
    remaining_quantity -= current_order

if my_queue.empty():
    print("Orders complete")
else:
    print("Orders left:", end=" ")
    while not my_queue.empty():
        print(my_queue.get(), end=" ")

