"""
Employee Operations Module

This module provides functions for adding, deleting, and updating employee information.
"""

def add_employee():
  employee=[]
  how=int(input("Enter how many employee to add:"))
  for i in range (how):
      id=int(input("Enter id of employee:"))
      first=input("Enter first name of employee:")
      last=input("Enter last name of employeee:")
      birth=input("Enter birth date:")
      start=int(input("Enter starting year:"))
      positon=input("Enter position")
      salary=int(input("Enter salary:"))
      list=[id,first,last,birth,start,position,salary]
      employee.append(list)
    """
    Add Employe Function

    This function prompts the user to input details for a new employee and adds the employee
    to the system.

    """
    
    def delete_employee():
      who=int(input("Enter Employee id to delete:"))
      for i in employee:
        if who== i[0]:
          employee.remove(i)
      """
    Delete Employee Function

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.

    """

      def update_employee():
        who=int(input("Enter Employee id to update:"))
        for i in employee:
          if who== i[0]:
            id=int(input("Enter id of employee:"))
            first=input("Enter first name of employee:")
            last=input("Enter last name of employeee:")
            birth=input("Enter birth date:")
            start=int(input("Enter starting year:"))
            position=input("Enter position")
            salary=int(input("Enter salary:"))
            i=[id,first,last,birth,start,salary]
            
    """
    Update Employee Function

    This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.

    """      
