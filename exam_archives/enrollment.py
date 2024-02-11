def gather_credits(num_of_credits, *args):
    needed_cred = num_of_credits
    collected_cred = 0
    courses = []
    result = []

    for course_name, cred in args:
        if course_name in courses:
            continue
        if needed_cred > 0:
            courses.append(course_name)
            needed_cred -= cred
            collected_cred += cred
        if needed_cred <= 0:
            break

    if needed_cred <= 0:
        result.append(f"Enrollment finished! Maximum credits: {collected_cred}.\nCourses: ")
        result.append(", ".join(sorted(courses)))
        return "".join(result)
    else:
        result.append(f"You need to enroll in more courses! You have to gather {needed_cred} credits more.")
        return "".join(result)


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))