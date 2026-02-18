def filter_sales_above(sales: list, threshold: int) -> list:
    """Returns sales values above threshold using list comprehension."""
    return [s for s in sales if s > threshold]

def get_sales_summary(sales: list, first_n: int, last_n: int) -> tuple:
    """Returns (first_n_sales_list, last_n_sales_list) using slicing."""
    return (sales[:first_n], sales[-last_n:])

def get_reversed_sales(sales: list) -> list:
    """Returns a reversed copy of the sales list."""
    return sales[::-1]

def get_sorted_sales(sales: list, descending: bool = False) -> list:
    """Returns a sorted copy of sales without modifying original."""
    return sorted(sales, reverse=descending)
