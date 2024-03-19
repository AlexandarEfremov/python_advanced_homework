class vowels:
    def __init__(self, string: str):
        self.string = string
        self.vowels = ["a", "e", "o", "u", "y", "i"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.string):
            letter = self.string[self.index]
            if letter.lower() in self.vowels:
                return letter
            else:
                return self.__next__()
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')

for char in my_string:
    print(char)