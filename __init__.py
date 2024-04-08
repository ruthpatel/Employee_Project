def update_employee_data(employee_id, employees=None):
    if employee_id not in employees:
        print(f"No employee was found with ID {employee_id}.")
        return

    employee = employees[employee_id]

    # Update employee attributes
    employee.first_name = input("Enter the new first name: ")
    employee.last_name = input("Enter the new last name: ")
    employee.date_of_birth = input("Enter the new date of birth (MM/DD/YYYY): ")
    employee.department = input("Enter the new department: ")
    employee.salary = float(input("Enter the new salary: "))

    # Save updated employee dictionary to text file
    with open("employees.txt", "w") as f:
        for employee_id, employee in employees.items():
            f.write(f"{employee_id},{employee.first_name},{employee.last_name},{employee.date_of_birth},{employee.department},{employee.salary}\n")

    print(f"Employee with ID {employee_id} has been updated.")