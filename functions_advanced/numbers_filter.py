def even_odd_filter(**kwargs):
    def odd():
        odd_numbers = [num for num in kwargs["odd"] if num % 2 != 0]
        return odd_numbers

    def even():
        even_numbers = [num for num in kwargs["even"] if num % 2 == 0]
        return even_numbers

    final_result = {}

    for k, v in kwargs.items():
        if k == "even":
            final_result["even"] = even()
        else:
            final_result["odd"] = odd()
    sorted_dict = dict(sorted(final_result.items(), key=lambda x: -len(x[1])))

    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))