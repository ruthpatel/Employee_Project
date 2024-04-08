class Employee:
    def _init_(self, id, first_name, last_name, dob, department, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.department = department
        self.salary = salary

def add_employee(employees):
    print("\nEnter employee details:")
    id = input("Employee ID: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    # Create an instance of the Employee class
    new_employee = Employee(id, first_name, last_name, dob, department, salary)

    # Append the new employee to the list
    employees.append(new_employee)

    # Write employee data to the text file
    with open("employee_data.txt", "a") as file:
        file.write(f"{id},{first_name},{last_name},{dob},{department},{salary}\n")

    print("Employee added successfully.")

# Example usage
if _name_ == "_main_":
    employees = []  # List to store employees
    while True:
        print("\n1. Add Employee")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please enter a valid option.")