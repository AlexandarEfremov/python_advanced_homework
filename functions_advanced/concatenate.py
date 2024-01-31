def concatenate(*args, **kwargs):
    concat = "".join([f"{item}" for item in args])
    key_list = [key for key in kwargs.keys()]
    for key in key_list:
        if key in concat:
            concat = concat.replace(key, kwargs[key])

    return concat


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))