def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
def square(n):
    return n*n

def cube(n):
    return n*n*n

def format_city(city):
    return city


def main():
    n = int(input("Enter n Value: "))
    city = input("Enter a City: ")
    result1 = is_even(n)
    result2 = square(n)
    result3 = cube(n)
    result4 = format_city(city)
    print(result1,result2,result3,result4)

main()