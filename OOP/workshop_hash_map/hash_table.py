class HashTable:
    def __init__(self):
        self.__keys = [None, None, None, None]
        self.__values = [None, None, None, None]
        self.__length = 4

    def __setitem__(self, key, value):
        index = self.hash(key)
        self.__keys[index] = key
        self.__values[index] = value

    def hash(self, key: str):
        return sum([ord(el) for el in key]) % self.__length

