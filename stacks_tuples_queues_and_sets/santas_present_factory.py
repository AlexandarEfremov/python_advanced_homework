from collections import deque

crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

materials = [int(x) for x in input().split()]
magic_values = deque(int(y) for y in input().split())

while materials and magic_values:
    current_box = materials.pop() if magic_values[0] or not materials[-1] else 0
    current_magic = magic_values.popleft() if current_box or not magic_values[0] else 0

    magic_multi = current_box * current_magic

    if presents.get(magic_multi):
        crafted.append(presents[magic_multi])
    elif magic_multi < 0:
        materials.append(current_magic + current_box)
    elif magic_multi > 0:
        materials.append(current_box + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    reversed_boxes = reversed(materials)
    materials_two = ", ".join(map(str, reversed_boxes))
    print(f"Materials left: {materials_two}")
if magic_values:
    magic = ", ".join(map(str, magic_values))
    print(f"Magic left: {magic}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
