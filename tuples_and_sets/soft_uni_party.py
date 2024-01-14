number_of_guests = int(input())

vip_list = set()
reg_list = set()


for _ in range(number_of_guests):
    invitation_code = input()
    if invitation_code[0].isdigit():
        vip_list.add(invitation_code)
    else:
        reg_list.add(invitation_code)

total_set = vip_list | reg_list

while True:
    coming_guest = input()
    if coming_guest == "END":
        break
    if coming_guest in total_set:
        total_set.remove(coming_guest)

print(len(total_set))
ordered_set = sorted(total_set, key=lambda x: (not x[0].isdigit(), x))
for item in ordered_set:
    print(item)