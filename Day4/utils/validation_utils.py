def validate_employee_id(emp_id: str) -> None:
    if not emp_id.startswith("EMP"):
        raise ValueError("Employee ID must start with 'EMP'.")


def validate_salary(salary: float) -> None:
    if salary <= 0:
        raise ValueError("Salary must be positive.")


def validate_non_empty(value: str, field_name: str) -> None:
    if not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")
