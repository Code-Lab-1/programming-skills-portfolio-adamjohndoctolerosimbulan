fav_nums = {
    'esmei': [77, 17, 27, 777],
    'adam': [7, 22, 14, 3],
    'mattew': [1, 16, 12, 5],
    }

for person, numbers in fav_nums.items():
    print(f"\n> {person.title()} likes the following numbers:")
    for number in numbers:
        print(f"- {number}")