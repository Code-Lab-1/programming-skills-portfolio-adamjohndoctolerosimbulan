places = {
    'baguio': {
        'country': 'philippines',
        'population': 345_366,
        'nearby mountains': 'jumbo',
        },
    'tokyo': {
        'country': 'japan',
        'population': 14_000_000,
        'nearby mountains': 'fuji',
        },
    'california': {
        'country': 'united states',
        'population': 39_340_000,
        'nearby mountains': 'shasta',
        }
    }

for place, places_info in places.items():
    country = places_info['country'].title()
    population = places_info['population']
    mountains = places_info['nearby mountains'].title()

    print(f"\n{place.title()} is located in {country}.")
    print(f"  It has a total population of {population}.")
    print(f"  The {mountains} mountain is nearby.")