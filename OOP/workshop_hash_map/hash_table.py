class HashTable:
    def __init__(self):
        self.__keys = [None, None, None, None]
        self.__values = [None, None, None, None]
        self.__length = 4

    def __len__(self):
        return len([el for el in self.__keys if el is not None])

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__length
        self.__value = self.__values + [None] * self.__length
        self.__length *= 2

    def __setitem__(self, key, value):
        if self.__len__() == self.__length:
            self.__resize()

        index = self.__find_index(self.hash(key))

        self.__keys[index] = key
        self.__values[index] = value

    def __getitem__(self, item):
        try:
            index = self.__keys.index(item)
            return self.__values[index]
        except ValueError:
            raise KeyError("Key does not exist")

    def get(self, key, return_default_value=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return return_default_value

    def hash(self, key: str):
        return sum([ord(el) for el in key]) % self.__length

    def __find_index(self, index):
        if index == self.__length:
            index = 0
        if self.__keys[index] is None:
            return index
        return self.__find_index(index + 1)

