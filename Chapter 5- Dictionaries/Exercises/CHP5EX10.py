fav_color = {
    'Adam': ['red', 'green', 'purple'],
    'Matt': ['brown', 'red', 'yellow'],
    'May': ['black', 'neon green', 'red']
    }

for name, colors in fav_color.items():
    print(f"\n{name.title()} likes the colors:")
    for place in colors:
        print(f"> {place.title()}")