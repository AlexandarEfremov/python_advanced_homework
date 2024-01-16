usernames_num = int(input())
username_set = set()

for i in range(usernames_num):
    name = input()
    username_set.add(name)
for nam in username_set:
    print(nam)

