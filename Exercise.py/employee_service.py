_emps = [
    {'empid': 1122, 'name': 'Sanjay', 'salary': 45000, 'dept': 'ADMIN'},
    {'empid': 2131, 'name': 'Suresh', 'salary': 35000, 'dept': 'ACCOUNTING'},
    {'empid': 3231, 'name': 'Rajeev', 'salary': 55000, 'dept': 'ADMIN'},
]

def accept_and_add_emp():
    global _emps
    try:
        print('Enter employee details')
        empid =  int(input('ID.        : '))
        name   = input('Name       : ')
        salary = float(input('Salary     : '))
        dept   = input('Department : ')

        emp = dict(empid=empid, name=name, salary=salary, dept=dept)
        _emps.append(emp)
    except:
        print('Invalid value entered. Please retry')


def print_employees():
    if len(_emps) == 0:
        print("No employees found. Please add.")
        return

    print(".","-"*53,".", sep="")
    print(f'|{"ID":5}|{"Name":20}|{"Salary":10}|{"Department":15}|')
    print("|","-"*53,"|", sep="")

    for emp in _emps:
        print(f'|{emp["empid"]:5}|{emp["name"]:20}|{emp["salary"]:10.1f}|{emp["dept"]:15}|')
    
    print(".","-"*53,".", sep="")

    
def save_emp_data_as_csv_file():
    if len(_emps) == 0:
        print("No employees found. Please add.")
        return
    
    filename = "employees.csv"
    f = open(filename, 'w')
    header = ','.join(_emps[0].keys())
    f.write(header)
    f.write('\n')
    for e in _emps:
        rec = ','.join([str(v) for v in e.values()])
        f.write(rec)
        f.write('\n')
    
    f.close()
    print(f"All employees data written to the file {filename} successfully")
        

Exercise.py/employee_service.py