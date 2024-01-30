def sorting_cheeses(**kwargs):
    result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    final = ""
    for key, value in result:
        final += key + "\n"
        for val in sorted(value, reverse=True):
            final += f"{val}\n"
    return final


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)