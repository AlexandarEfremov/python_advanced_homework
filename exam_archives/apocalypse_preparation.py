from collections import deque
textile_integers = deque([int(x) for x in input().split()])
meds = [int(x) for x in input().split()]

med_dict = {}

while textile_integers and meds:
    current_textile = textile_integers.popleft()
    current_med = meds.pop()
    result = current_textile + current_med
    if result == 30:
        med_dict["Patch"] = med_dict.get("Patch", 0) + 1
    elif result == 40:
        med_dict["Bandage"] = med_dict.get("Bandage", 0) + 1
    elif result == 100:
        med_dict["MedKit"] = med_dict.get("MedKit", 0) + 1
    elif result > 100:
        med_dict["MedKit"] = med_dict.get("MedKit", 0) + 1
        diff = abs(result - 100)
        meds[-1] += diff
    else:
        current_med += 10
        meds.append(current_med)

if not textile_integers and not meds:
    print("Textiles and medicaments are both empty.")
elif not textile_integers and meds:
    print("Textiles are empty.")
elif not meds and textile_integers:
    print("Medicaments are empty.")

textile_integers_two = list(textile_integers)
meds.reverse()
sorted_dict = dict(sorted(med_dict.items(), key=lambda x: (-x[1], x[0])))
[print(f"{key} - {value}") for key, value in sorted_dict.items()]
if meds:
    print(f"Medicaments left: {', '.join(map(str, meds))}")
elif textile_integers:
    print(f"Textiles left: {', '.join(map(str, textile_integers_two))}")


