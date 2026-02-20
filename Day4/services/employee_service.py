def add_employee(emp_list: list, emp_id: str, name: str, city: str, salary: float) -> None:
    if any(emp["id"] == emp_id for emp in emp_list):
        raise ValueError("Employee ID already exists.")

    if salary <= 0:
        raise ValueError("Salary must be positive.")

    emp_list.append({
        "id": emp_id,
        "name": name,
        "city": city,
        "salary": salary
    })


def edit_employee(emp_list: list, emp_id: str, **updates) -> None:
    for emp in emp_list:
        if emp["id"] == emp_id:
            for key, value in updates.items():
                if key == "salary" and value <= 0:
                    raise ValueError("Salary must be positive.")
                emp[key] = value
            return

    raise ValueError("Employee ID not found.")


def delete_employee(emp_list: list, emp_id: str) -> None:
    for emp in emp_list:
        if emp["id"] == emp_id:
            emp_list.remove(emp)
            return

    raise ValueError("Employee ID not found.")


def list_employees(emp_list: list) -> list:
    return emp_list
