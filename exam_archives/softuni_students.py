def softuni_students(*args, **kwargs):
    student_data = [(x[0], x[1]) for x in args]
    student_dict = {}
    for key, value in kwargs.items():
        student_dict[key] = value
    results = []
    error_result = []
    for info in student_data:
        student_id = info[0]
        student_name = info[1]
        if student_id in student_dict:
            results.append(f"*** A student with the username {student_name} has successfully finished the course {student_dict[student_id]}!")
        else:
            error_result.append(student_name)
    sorted_list = sorted(results)
    sorted_error_result = sorted(error_result)
    error_string = "!!! Invalid course students: " + ", ".join(sorted_error_result) if sorted_error_result else ""
    return "\n".join(sorted_list + [error_string])


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))