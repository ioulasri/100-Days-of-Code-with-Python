travel_log = {
    "France": ["Paris", "Lille", "Marseille"]
}
for k, v in travel_log.items():
    print(k + " best cities are:")
    for item in v:
        print("-" + item)

cities_visited = {
    "France": ["Paris", "Lille"]
}
for k, v in cities_visited.items():
    print(k + "'s visited cities are:")
    for item in v:
        print("-" + item)

names = [{"imad": "Oulasri"}, {"Bouchra": "Oulasri"}]
for i in range(len(names)):
    for k, v in names[i].items():
        print("-" + k + " " + v.upper())

