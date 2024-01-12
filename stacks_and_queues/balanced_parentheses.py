input_string = [x for x in input()]
opening = ["[", "(", "{"]
closing = ["]", ")", "}"]
copy_string = input_string.copy()
cond = True
stack = []
for char in input_string:
    if char in opening:
        stack.append(char)
    elif char in closing:
        char_index = closing.index(char)
        if not stack or stack.pop() != opening[char_index]:
            cond = False
    else:
        cond = False

if cond:
    print("YES")
else:
    print("NO")