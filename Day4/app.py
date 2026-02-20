from services import (
    add_employee,
    edit_employee,
    delete_employee,
    list_employees
)
from utils.file_utils import load_employees, save_employees
from utils.validation_utils import (
    validate_employee_id,
    validate_salary,
    validate_non_empty
)

import os

DATA_FILE = os.path.join("data", "employees.txt")


def main():
    try:
        employees = load_employees(DATA_FILE)
    except FileNotFoundError:
        employees = []

    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. Edit Employee")
        print("3. Delete Employee")
        print("4. List Employees")
        print("5. Save to File")
        print("6. Exit")

        try:
            choice = input("Enter choice: ")

            if choice == "1":
                emp_id = input("Enter ID: ")
                name = input("Enter Name: ")
                city = input("Enter City: ")
                salary = float(input("Enter Salary: "))

                validate_employee_id(emp_id)
                validate_non_empty(name, "Name")
                validate_non_empty(city, "City")
                validate_salary(salary)

                add_employee(employees, emp_id, name, city, salary)
                print("Employee added successfully.")

            elif choice == "2":
                emp_id = input("Enter ID to edit: ")
                updates = {}

                name = input("New Name (leave blank to skip): ")
                city = input("New City (leave blank to skip): ")
                salary_input = input("New Salary (leave blank to skip): ")

                if name:
                    validate_non_empty(name, "Name")
                    updates["name"] = name
                if city:
                    validate_non_empty(city, "City")
                    updates["city"] = city
                if salary_input:
                    salary = float(salary_input)
                    validate_salary(salary)
                    updates["salary"] = salary

                edit_employee(employees, emp_id, **updates)
                print("Employee updated successfully.")

            elif choice == "3":
                emp_id = input("Enter ID to delete: ")
                delete_employee(employees, emp_id)
                print("Employee deleted successfully.")

            elif choice == "4":
                for emp in list_employees(employees):
                    print(emp)

            elif choice == "5":
                save_employees(DATA_FILE, employees)
                print("Data saved successfully.")

            elif choice == "6":
                save = input("Save before exit? (y/n): ")
                if save.lower() == "y":
                    save_employees(DATA_FILE, employees)
                print("Exiting...")
                break

            else:
                print("Invalid choice.")

        except ValueError as ve:
            print("Validation Error:", ve)
        except FileNotFoundError as fe:
            print("File Error:", fe)
        except Exception as e:
            print("Unexpected Error:", e)


if __name__ == "__main__":
    main()
