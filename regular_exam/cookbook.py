def cookbook(*args):
    recipie_dict = {}
    for name, cuisine, ingredient_list in args:
        if cuisine not in recipie_dict:
            recipie_dict[cuisine] = []
            recipie_dict[cuisine].append((name, ingredient_list))
        else:
            recipie_dict[cuisine].append((name, ingredient_list))
    sorted_recipie = dict(sorted(recipie_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ""
    for key, value in sorted_recipie.items():
        result += f"{key} cuisine contains {len(value)} recipes:\n"
        for recipe, ingredients in sorted(value):
            result += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"
    return result


print(cookbook(
                    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
                      ("Chicken Curry", "Indian", ["chicken", "curry paste", "coconut milk", "rice"]),
                      ("Caesar Salad", "American", ["romaine lettuce", "croutons", "parmesan", "caesar dressing"]),
                      ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
                      ("Mushroom Risotto", "Italian", ["arborio rice", "mushrooms", "onion", "parmesan", "broth"]),
                      ("Tacos", "Mexican", ["tortillas", "ground beef", "lettuce", "tomato", "cheese"]),
                      ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"]),
                      ("Chicken Alfredo", "Italian", ["fettuccine", "chicken", "alfredo sauce", "broccoli"])))