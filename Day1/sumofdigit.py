def sum_of_digits(n):
    add = 0
    n = abs(n)
    
    while n > 0:
        ld = n%10
        add += ld
        n = n//10
    return add


def main():
    n = int(input())
    res = sum_of_digits(n)
    print(res)

main()