def reverse_number(n):
    rev = 0
    if n < 0:
        raise ValueError("Input Not in Negative")
    
    while n > 0:
        digit = n % 10
        rev = rev*10+digit
        n = n//10
    return rev

def main():
    n = int(input())
    res = reverse_number(n)
    print(res)
main()