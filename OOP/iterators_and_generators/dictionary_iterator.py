class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.dict_obj = list(dict_obj.items())
        self.current_pair = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_pair == len(self.dict_obj) - 1:
            raise StopIteration

        self.current_pair += 1
        return self.dict_obj[self.current_pair]


result = dictionary_iter({1: "1", 2: "2"})

for x in result:
    print(x)
