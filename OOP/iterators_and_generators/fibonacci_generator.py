def fibonacci():
    a_num = 0
    b_num = 1

    while True:
        yield a_num
        a_num, b_num = b_num, a_num + b_num


generator = fibonacci()

for i in range(5):
    print(next(generator))