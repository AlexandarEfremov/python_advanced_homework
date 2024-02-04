import re
import os.path

words_path = os.path.join("words.txt")
text_path = os.path.join("input.txt")
output_file_path = os.path.join("text.txt")

with open(words_path) as file:
    searched_words = file.read()
    searched_words = [word.lower() for word in searched_words.split()]

with open(text_path) as file:
    content = file.read().lower()

words_count = {}

for searched_word in searched_words:
    pattern = re.compile(rf"\b{searched_word}\b")
    result = re.findall(pattern, content)
    words_count[searched_word] = len(result)

sorted_word_count = sorted(words_count.items(), key=lambda kvp: -kvp[1])

with open(output_file_path, "a") as file:
    for word, count in sorted_word_count:
        file.write(f"{word} - {count}\n")