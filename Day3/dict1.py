def add_employee(directory: dict, emp_id: str, data: dict) -> None:
    """
    Adds a new employee to directory.
    """
    if emp_id in directory:
        print("Employee ID already exists.")
    else:
        directory[emp_id] = data
        print("Employee added successfully.")


def get_employee(directory: dict, emp_id: str) -> dict:
    """
    Returns employee details safely.
    """
    return directory.get(emp_id, {})


def delete_employee(directory: dict, emp_id: str) -> None:
    """
    Deletes employee if exists.
    """
    if emp_id in directory:
        directory.pop(emp_id)
        print("Employee deleted successfully.")
    else:
        print("Employee ID not found.")

def main():
    employees = {
        "EMP101": {"name": "Vinod", "city": "Bangalore", "salary": 75000},
        "EMP102": {"name": "Amit", "city": "Delhi", "salary": 60000}
    }

    print("Initial Directory:", employees)


    new_data = {"name": "Rahul", "city": "Mumbai", "salary": 50000}
    add_employee(employees, "EMP103", new_data)
    print("After Adding:", employees)


    emp = get_employee(employees, "EMP101")
    print("Get EMP101:", emp)


    emp = get_employee(employees, "EMP999")
    print("Get EMP999:", emp)


    delete_employee(employees, "EMP102")
    print("After Deletion:", employees)


    delete_employee(employees, "EMP999")


main()
