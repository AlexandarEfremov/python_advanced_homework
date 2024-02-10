def team_lineup(*args):
    country_dict = {}
    for arg in args:
        name = arg[0]
        country = arg[1]
        if country not in country_dict:
            country_dict[country] = []
            country_dict[country].append(name)
        else:
            country_dict[country].append(name)
    sorted_dict = dict(sorted(country_dict.items(), key=lambda x: (-len(x[1]), (x[0]))))
    result = ""
    for country, player_name in sorted_dict.items():
        result += f"{country}:\n"
        for player in player_name:
            result += f"  -{player}\n"
    return result.strip()


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
