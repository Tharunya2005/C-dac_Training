def load_employees(file_path: str) -> list:
    employees = []

    with open(file_path, "r") as file:
        for line in file:
            emp_id, name, city, salary = line.strip().split(",")
            employees.append({
                "id": emp_id,
                "name": name,
                "city": city,
                "salary": float(salary)
            })

    return employees


def save_employees(file_path: str, emp_list: list) -> None:
    with open(file_path, "w") as file:
        for emp in emp_list:
            line = f'{emp["id"]},{emp["name"]},{emp["city"]},{emp["salary"]}\n'
            file.write(line)
