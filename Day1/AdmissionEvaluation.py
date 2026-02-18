def check_admission(marks, age, city):
    cities = ["Mumbai","Delhi","Pune"]

    if city not in cities:
        raise ValueError("city must be chennai,Delhi,Pune")
    
    if marks >= 70 and age >= 18 and city in cities:
        return "Admission Aproved"
    else:
        return "Admission Denied"

def main():
    marks = int(input("Enter Marks: "))
    age = int(input("Enter Your Age: "))
    city = input("Enter Your City (Mumbai/Pune/Delhi): ")
    result = check_admission(marks, age, city)
    print(result)

main()

