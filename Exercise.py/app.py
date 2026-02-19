#! /Library/Frameworks/Python.framework/Versions/3.12/bin/python3
"""
Menu driven program
"""

from employee_service import print_employees, accept_and_add_emp, save_emp_data_as_csv_file
import subprocess


def menu():
    print(f"""
{"Employee data management system".center(50, "=")}
{"Main Menu".center(50, "=")}
0. Exit
1. Add new employee
2. Search
3. Edit
4. Delete
5. View all
6. Save as CSV file
          """)
    
    choice = input("Enter your choice (0-6): ")
    try:
        choice = int(choice)
    except:
        choice = -1

    return choice


def main():
    while True:
        subprocess.run("clear")
        choice = menu()
        if choice == 0:
            print("Thanks for using our app.")
            break

        if choice <0 or choice > 6:
            print("Enter a valid value between 0 and 6.")

        if choice == 1:
            accept_and_add_emp()

        if choice == 2:
            print("Search user feature not ready yet")

        if choice == 3:
            print("Edit user feature not ready yet")

        if choice == 4:
            ...

            
        if choice == 5:
            print_employees()

        if choice == 6:
            save_emp_data_as_csv_file()

        input("Hit ENTER/RETURN key to proceed")


if __name__ == '__main__':
    main()