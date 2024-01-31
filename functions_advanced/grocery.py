def grocery_store(**kwargs):
    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

    final_result = [f"{key}: {value}" for key, value in sorted_dict.items()]
    return "\n".join(final_result)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))