def password_validator(n):
    if len(n) >= 8:
        if any(char.isdigit() for char in n):
            if any(char.isupper() for char in n):
                return "Valid Password"
    else:
        raise ValueError("Rules not satisfied")   

def main():
    n = input()
    result = password_validator(n)
    print(result)

main()