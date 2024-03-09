class Calculator:
    @staticmethod
    def add(*args):
        return sum([arg for arg in args])

    @staticmethod
    def multiply(*args):
        result = 1
        for arg in args:
            result *= arg
        return result

    @staticmethod
    def divide(*args):
        num_list = [e for e in args]
        first_el = num_list.pop(0)
        for _ in num_list:
            while num_list:
                first_el /= num_list.pop(0)
        return first_el

    @staticmethod
    def subtract(*args):
        num_list = [e for e in args]
        first_el = num_list.pop(0)
        for _ in num_list:
            while num_list:
                first_el -= num_list.pop(0)
        return first_el

print(Calculator.add(5, 10, 4))

print(Calculator.multiply(1, 2, 3, 5))

print(Calculator.divide(100, 2))

print(Calculator.subtract(90, 20, -50, 43, 7))