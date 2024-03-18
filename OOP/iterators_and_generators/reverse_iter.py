class reverse_iter:
    def __init__(self, iter_value):
        self.iter_value = iter_value
        self.reverse_value = reversed(iter_value)

    def __iter__(self):
        return self

    def __next__(self):
        for num in self.reverse_value:
            return num
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])

for item in reversed_list:
    print(item)