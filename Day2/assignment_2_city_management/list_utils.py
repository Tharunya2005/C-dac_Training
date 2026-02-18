def get_unique_cities(cities: list) -> list:
    """Return a new list containing unique city names, preserving order."""
    unique = []
    for city in cities:
        if city not in unique:
            unique.append(city)
    return unique


def get_sorted_cities(cities: list, descending: bool = False) -> list:
    """Return a sorted copy of the cities list."""
    return sorted(cities, reverse=descending)


def convert_cities_to_upper(cities: list) -> list:
    """Return a new list with all city names converted to uppercase."""
    return [city.upper() for city in cities]
