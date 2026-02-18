def factorial(num):
    """
    This is a function to calculate and return the fact of the input.

    
    """
    if type(num) != int:
        raise TypeError("only int is allowed")
    
    if num<0:
        raise ValueError("not negative values are alllowed")
    
    f = 1
    while num>0:
        f *= num
        num -= 1

    return f