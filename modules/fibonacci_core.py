def create_sequence(c):
    seq = [0, 1]
    for _ in range(c - 2):
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
    return seq


def locate_number(number, seq):
    try:
        temp_res = seq.index(number)
        return f"The number - {number} is at index {temp_res}"
    except ValueError:
        return f"The number {number} is not in the sequence"
