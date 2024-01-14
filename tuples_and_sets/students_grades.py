student_info = [(name, float(grade)) for _ in range(int(input())) for name, grade in [input().split()]]
student_dict = {}

for item in student_info:
    name, grade = item[0], item[1]
    student_dict[name] = student_dict.get(name, [])
    student_dict[name].append(grade)

for i, v in student_dict.items():
    print(f"{i} -> {' '. join(map(lambda x: f'{x:.2f}', v))} (avg: {(sum(v) / len(v)):.2f})")

