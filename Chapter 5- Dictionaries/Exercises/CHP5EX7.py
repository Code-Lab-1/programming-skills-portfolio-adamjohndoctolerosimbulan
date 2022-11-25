fav_sports = {
    'adam': ['volleyball', 'basketball', 'kendo'],
    'esmei': ['swimming', 'badminton', 'volleyball'],
    'matthew': ['basketball', 'jumping rope', 'track and field']
    }

for name, sports in fav_sports.items():
    print(f"\n{name.title()} likes the following sports:")
    for place in sports:
        print(f"- {place.title()}")