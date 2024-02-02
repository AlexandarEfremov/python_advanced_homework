numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
        print(numbers_dictionary)
        exit()
    line = input()

while line != "Remove":
    line = input()
    print(numbers_dictionary[line])
    line = input()

while line != "End":
    line = input()
    try:
        del numbers_dictionary[line]
    except KeyError:
        print("Number does not exist in dictionary")
        print(numbers_dictionary)
        exit()
    line = input()
print(numbers_dictionary)