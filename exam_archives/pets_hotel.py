def accommodate_new_pets(capacity, weight_limit, *args):
    hotel_cap = capacity
    hotel_dict = {}
    result = []
    all_pets = True

    for pet_type, pet_weight in args:
        if hotel_cap <= 0:
            result.append('You did not manage to accommodate all pets!')
            break
        if pet_weight > weight_limit:
            continue
        if pet_type not in hotel_dict:
            hotel_dict[pet_type] = 1
            hotel_cap -= 1
        else:
            hotel_dict[pet_type] += 1
            hotel_cap -= 1
    else:
        result.append(f'All pets are accommodated! Available capacity: {hotel_cap}.')
    sorted_dict = dict(sorted(hotel_dict.items(), key=lambda x: x[0]))
    result.append("Accommodated pets:")
    [result.append(f"{pet_type}: {pet_num}") for pet_type, pet_num in sorted_dict.items()]
    return "\n".join(result)


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))