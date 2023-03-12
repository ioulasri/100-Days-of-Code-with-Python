travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇

def add_new_country(country, time_visited, places_visited):
    new_countries = {"Country": country, "visits": time_visited, "cities": places_visited}
    a = new_countries.copy()
    travel_log.append(a)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Morocco", 34, ["Agadir", "Taroudant"])
add_new_country("France", 6, ["Paris", "Petersburg"])

print(travel_log)
