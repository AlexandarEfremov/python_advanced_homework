def even_parameters(func):

    def wrapper(*args, **kwargs):
        for el in args:
            if not isinstance(el, int) or el % 2 != 0:
                return f"Please use only even numbers!"
        else:
            return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))

print(add("Peter", 1))