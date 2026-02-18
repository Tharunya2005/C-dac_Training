def categorize_person(age):
    if type(age) != int:
        raise TypeError("Integer Only Considerable")
    
    if age < 0 or age > 120:
        raise ValueError("Invalid Input")
    
    if age>=0 and age<=12:
        return "Child"
    elif age>=13 and age<=19:
        return "Teenager"
    elif age>=20 and age <= 59:
        return "Adult"
    else:
        return "Citizen"



def main():
    age = int(input("Enter the Age: "))
    result = categorize_person(age)
    print(result)
    print(id(age))
    print(type(result))
main()