def create_employee(emp_id: str, name: str, city: str, salary: float)-> tuple:
    """Returns an employee record as a tuple.Validate inputs properly."""
    if not isinstance(emp_id,str) or not emp_id.strip():
        raise ValueError("Employee id must be a non-empty string")
    if not isinstance(name,str) or not name.strip():
        raise ValueError("Name must be a non-empty string")
    if not isinstance(city,str) or not city.strip():
        raise ValueError("City must be a non-emoy string")
    if not isinstance(salary,(int,float)):
        raise ValueError("salary must be a non-empty integer or float")
    
    return(emp_id,name,city,salary)



def update_salary(employee: tuple, new_salary: float) -> tuple:
    """Since tuples are immutable, return a new tuple with updatedsalary.Original tuple must not be modified."""
    if  not isinstance(employee,tuple) or len(employee)!=4:
        raise ValueError("employee details must be in tuple")
    if not isinstance(new_salary,(int,float)) or new_salary <= 0:
        raise ValueError("Salary must be a non negative number")
    
    emp_id,name,city,_ = employee

    return (emp_id,name,city,float(new_salary))


def get_employee_details(employee: tuple) -> str:
    """Returns formatted string containing employee details."""
    if not isinstance(employee,tuple) or len(employee)!=4:
        raise ValueError("invalid employee record")
    
    emp_id, name, city, salary = employee

    return(
        f"Employee Id : {emp_id}\n"
        f"Name : {name}\n"
        f"city : {city}\n"
        f"salary : {salary}"
    )


def main():
    employee_id = input("Enter Employee id: ")
    name = input("Enter Name: ")
    city = input("Enter City: ")
    salary = int(input("Enter Your Salary: "))

    employee = create_employee(employee_id, name, city, salary)
    print("\nEmployee Created Successfully!")
    print(get_employee_details(employee))

    new_salary = float(input("\nEnter New Salary: "))
    updated_employee = update_salary(employee, new_salary)

    print("\nUpdated Employee Details:")
    print(get_employee_details(updated_employee))

    print("\nOriginal Employee Details (Still Same):")
    print(get_employee_details(employee))

main()
