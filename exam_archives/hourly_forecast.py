def forecast(*args):
    weather_dict = {}
    for location, weather in args:
        weather_dict[weather] = weather_dict.get(weather, [])
        weather_dict[weather].append(location)
    sorting_order = ["Sunny", "Cloudy", "Rainy"]
    sorted_weather = dict(sorted(weather_dict.items(), key=lambda x: sorting_order.index(x[0])))
    result = ""
    for key, value in sorted_weather.items():
        for city in sorted(value):
            result += f"{city} - {key}\n"
    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))