def students_credits(*args):
    courses = {}
    for items in args:
        course, total_credits,max_points, student_points = items.split("-")
        percentage = int(student_points) / int(max_points)
        current_credits = int(total_credits) * percentage
        courses[course] = courses.get(course, 0) + current_credits
    sorted_courses = dict(sorted(courses.items(), key=lambda x: -x[1]))
    sum_credits = sum(courses.values())
    result = []
    if sum_credits >= 240:
        result.append(f"Diyan gets a diploma with {sum_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {(240 - sum_credits):.1f} credits more for a diploma.")
    for course, grade in sorted_courses.items():
        result.append(f"{course} - {grade:.1f}")
    return "\n".join(result)


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)