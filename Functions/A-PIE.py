# class Employee:
#     def __init__(self, name, employee_id, department):
#         self.name = name
#         self.employee_id = employee_id
#         self.department = department

#     def display_details(self):
#         print("Employee Name:", self.name)
#         print("Employee ID:", self.employee_id)
#         print("Department:", self.department)


# person = Employee("Rashid Ahmed Nadaf", "507174", "ITH/IT")

# person.display_details()

# class Employee:
#     def __init__(self, emp_id, name, department, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.department = department
#         self.salary = salary

#     def display_details(self):
#         print("Employee ID:", self.emp_id)
#         print("Name:", self.name)
#         print("Department:", self.department)
#         print("Salary:", self.salary)
#         print("-" * 30)


# # Creating objects for four employees
# emp1 = Employee(101, "Rashid", "IT", 60000)
# emp2 = Employee(102, "Kavita", "HR", 55000)
# emp3 = Employee(103, "Amit", "Finance", 58000)
# emp4 = Employee(104, "Neha", "Operations", 52000)

# # Storing employee objects in a list
# employees = [emp1, emp2, emp3, emp4]

# # Displaying employee details
# for emp in employees:
#     emp.display_details()

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("-" * 30)


class EmployeeManager:
    def __init__(self):
        # List to store employee objects
        self.employee_list = []

        # Dictionary to store employees with emp_id as key
        self.employee_dict = {}

    def add_employee(self, employee):
        # Check if employee ID already exists
        if employee.emp_id in self.employee_dict:
            print("Employee ID already exists. Employee not added.")
            return

        # Add to list and dictionary
        self.employee_list.append(employee)
        self.employee_dict[employee.emp_id] = employee

        print("Employee added successfully.")

    def display_all(self):
        if not self.employee_list:
            print("No employees found.")
            return

        for emp in self.employee_list:
            emp.display_details()

    def search_employee(self, emp_id):
        # Search using dictionary (fast lookup)
        if emp_id in self.employee_dict:
            print("Employee found:")
            self.employee_dict[emp_id].display_details()
        else:
            print("Employee not found.")


# Main program
manager = EmployeeManager()

while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        emp = Employee(emp_id, name, department, salary)
        manager.add_employee(emp)

    elif choice == "2":
        manager.display_all()

    elif choice == "3":
        emp_id = int(input("Enter Employee ID to search: "))
        manager.search_employee(emp_id)

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
