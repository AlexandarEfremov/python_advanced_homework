input_text = input()
count_dict = {}
for letter in input_text:
    counter = input_text.count(letter)
    count_dict[letter] = counter
for i, v in sorted(count_dict.items(), key=lambda x: x):
    print(f"{i}: {v} time/s")

