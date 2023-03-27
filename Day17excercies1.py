import json
def most_popluated_countries():
    with open("countries.json", "r") as f:
        countries = json.load(f)

    countries.sort(key=lambda x:x["population"], reverse=True)
    top_10_countries = [country["name"] for country in countries[:10]]

    return top_10_countries
