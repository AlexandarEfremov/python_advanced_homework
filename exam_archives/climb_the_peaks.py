from collections import deque
conquered_peaks = []
peak_dict = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}

daily_portions = [int(x) for x in input().split(", ")]
daily_stamina = deque([int(x) for x in input().split(", ")])

for _ in range(7):
    if len(conquered_peaks) == 5:
        break
    current_portion = daily_portions.pop()
    current_stamina = daily_stamina.popleft()
    result = current_portion + current_stamina
    for peak, value in peak_dict.items():
        if result >= value:
            conquered_peaks.append(peak)
            del peak_dict[peak]
            break
        else:
            break

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks:")
    print('\n'.join(conquered_peaks))
