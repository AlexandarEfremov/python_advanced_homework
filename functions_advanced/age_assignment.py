def age_assignment(*args, **kwargs):
    user_info = [(user, kwargs[user[0]]) for user in args]
    sorted_info = sorted(user_info, key=lambda x: x)
    formated_result =  [f"{item[0]} is {item[1]} years old." for item in sorted_info]
    final = "\n".join(formated_result)
    return final


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))