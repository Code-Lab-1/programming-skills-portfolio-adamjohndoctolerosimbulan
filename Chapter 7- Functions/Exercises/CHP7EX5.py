def describe_city(city, country='philippines'):
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('baguio')
describe_city('tokyo', 'japan')
describe_city('pampanga')