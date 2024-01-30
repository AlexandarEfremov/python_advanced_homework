def kwargs_length(**kwargs):
    length = len(kwargs.keys())
    return length


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
