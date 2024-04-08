"""
Report Generation Module

This module provides a function for generating reports based on employee data.
"""
import statistics

def generate_reports():
    """
    Generate Reports Function

    This function generates various reports based on employee data, such as:
    - List of departments
    - List of all employees with ID, full name, and department
    - List of all departments with the average age and salary of employees
    - List of employees in each department with ID, full name, date of birth, salary,
      and total salary for department's employees
    """
    # Read employee data from file
    employees_data = read_employees()

    # Generate list of departments
    departments = {employee.split(',')[2] for employee in employees_data}
    print("List of departments:")
    print(", ".join(departments))

    # Generate list of all employees with ID, full name, and department
    print("\nList of all employees with ID, full name, and department:")
    for employee in employees_data:
        employee_id, full_name, department = employee.split(',')
        print(f"{employee_id}, {full_name}, {department}")

    # Generate list of all departments with the average age and salary of employees
    print("\nList of all departments with the average age and salary of employees:")
    for department in departments:
        department_employees = [employee for employee in employees_data if employee.split(',')[2] == department]
        ages = [int(employee.split(',')[3]) for employee in department_employees]
        salaries = [float(employee.split(',')[4]) for employee in department_employees]
        avg_age = statistics.mean(ages)
        avg_salary = statistics.mean(salaries)
        print(f"{department}: Average age = {avg_age}, Average salary = {avg_salary}")

    # Generate list of employees in each department with ID, full name, date of birth, salary,
    # and total salary for department's employees
    print("\nList of employees in each department with ID, full name, date of birth, salary,")
    print("and total salary for department's employees:")
    for department in departments:
        department_employees = [employee for employee in employees_data if employee.split(',')[2] == department]
        print(f"\n{department}:")
        total_salary = 0
        for employee in department_employees:
            employee_id, full_name, department, age, salary = employee.split(',')
            total_salary += float(salary)
            print(f"{employee_id}, {full_name}, {age}, {salary}, {total_salary}")