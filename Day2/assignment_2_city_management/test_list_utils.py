from list_utils import get_unique_cities, get_sorted_cities, convert_cities_to_upper

def main():
    cities = ["Mumbai", "Delhi", "Chennai", "Mumbai", "Bangalore"]

    print("Original Cities:", cities)
    print("Unique Cities:", get_unique_cities(cities))
    print("Sorted Cities:", get_sorted_cities(cities))
    print("Sorted Cities (Descending):", get_sorted_cities(cities, descending=True))
    print("Uppercase Cities:", convert_cities_to_upper(cities))
    print("Original Cities After Function Calls:", cities)

if __name__ == "__main__":
    main()
