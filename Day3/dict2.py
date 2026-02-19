def get_top_city(sales: dict) -> str:
    """
    Returns city with highest sales.
    """
    return max(sales, key=sales.get)


def get_low_sales_cities(sales: dict, threshold: int) -> dict:
    """
    Returns dictionary of cities with sales below threshold.
    """
    return {city: amount for city, amount in sales.items() if amount < threshold}


def increase_sales(sales: dict, percentage: float) -> dict:
    """
    Returns a new dictionary with increased sales values.
    Original dictionary must not be modified.
    """
    return {
        city: int(amount + (amount * percentage / 100))
        for city, amount in sales.items()
    }

def main():
    sales = {
        "Mumbai": 120000,
        "Delhi": 95000,
        "Chennai": 150000,
        "Pune": 80000
    }

    print("Original Sales:", sales)

    print("Top City:", get_top_city(sales))

    print("Low Sales Cities (<100000):", get_low_sales_cities(sales, 100000))

    new_sales = increase_sales(sales, 10)
    print("Sales After 10% Increase:", new_sales)

    print("Original Sales After Increase:", sales)


main()
