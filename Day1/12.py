from ageclassification import categorize_person
from stipendbonus import calculate_stipend_bonus
from ATM import withdraw
from reverse import reverse_number
from sumofdigit import sum_of_digits
from AdmissionEvaluation import check_admission
from vinod_utils import is_even,cube,square,format_city


def reg_student(name,age,marks,city):
    if type(name) and type(city) != str:
        raise TypeError("Name and city must be in string format")
    if type(age) and type(marks) != int:
        raise TypeError("Age and marks must be in integer format")

    return id(name,age,marks)

def main():
    name = input("Enter Your name: ")
    age = int(input("Enter your age: "))
    marks = int(input("Ener Your marks: "))
    city = input("Enter Your city: ")

main()
categorize_person()
calculate_stipend_bonus()
withdraw()
reverse_number()
sum_of_digits()
check_admission()
is_even()
square()
cube()
format_city()
