from list_utils import filter_sales_above, get_sales_summary, get_reversed_sales, get_sorted_sales

sales = [1200, 800, 1500, 600, 2000, 1000]

print("Original Sales:", sales)
print("Sales above 1000:", filter_sales_above(sales, 1000))
first, last = get_sales_summary(sales, 2, 2)
print("First 2 Sales:", first)
print("Last 2 Sales:", last)
print("Reversed Sales:", get_reversed_sales(sales))
print("Sorted Sales Asc:", get_sorted_sales(sales))
print("Sorted Sales Desc:", get_sorted_sales(sales, descending=True))
print("Original Sales after operations:", sales)
