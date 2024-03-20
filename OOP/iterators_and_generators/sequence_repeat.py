from collections import deque


class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = deque(sequence)
        self.number = number
        self.working_sequence = self.sequence.copy()
        self.index = 0
        self.sequence.rotate(1)
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.number:
            raise StopIteration
        self.sequence.rotate(-1)
        self.index += 1
        return self.sequence[0]


result = sequence_repeat('I Love Python', 3)

for item in result:
    print(item, end ='')