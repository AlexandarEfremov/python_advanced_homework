import roman


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        decimal_num = roman.fromRoman(value)
        return cls(decimal_num)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))


first_num = Integer(10)

print(first_num.value)

second_num = Integer.from_roman("IV")

print(second_num.value)

print(Integer.from_float("2.6"))

print(Integer.from_string(2.6))