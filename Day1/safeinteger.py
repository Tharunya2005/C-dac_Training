def safe_integer_input(prompt):
    n = input(prompt)
    try:
        return int(n)
    except ValueError:
        raise TypeError("Conversion Fails")


num = safe_integer_input("enter input: ")
print(num)
