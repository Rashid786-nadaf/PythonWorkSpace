# # Parent class
# class Employee:
#     def __init__(self, name, basic_salary):
#         self.name = name
#         self.basic_salary = basic_salary

#     def calculate_salary(self):
#         print("Calculating base employee salary")


# # Child class 1
# class Developer(Employee):
#     def calculate_salary(self):
#         bonus = self.basic_salary * 0.10
#         total_salary = self.basic_salary + bonus
#         print(f"Developer {self.name} Salary: {total_salary}")


# # Child class 2
# class Manager(Employee):
#     def calculate_salary(self):
#         bonus = self.basic_salary * 0.20
#         total_salary = self.basic_salary + bonus
#         print(f"Manager {self.name} Salary: {total_salary}")


# # Child class 3
# class Intern(Employee):
#     def calculate_salary(self):
#         stipend = self.basic_salary
#         print(f"Intern {self.name} Stipend: {stipend}")


# # -------- Polymorphism in action --------
# employees = [
#     Developer("Rashid", 50000),
#     Manager("Alice", 70000),
#     Intern("Vedant", 15000)
# ]

# for emp in employees:
#     emp.calculate_salary()   # Same method, different output

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_details(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}" 
class Coder(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    def get_details(self):
        self.salary += 10000  # Coders get a bonus
        return f"Employee Name: {self.name}, Salary: {self.salary}, Programming Language: {self.programming_language}" 
class Designer(Employee): 
    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool
    def get_details(self):
        self.salary += 5000  # Designers get a bonus
        return f"Employee Name: {self.name}, Salary: {self.salary}, Design Tool: {self.design_tool}"

Employees=[Employee("Alice", 70000), Coder("Bob", 90000, "Python"), Designer("Charlie", 80000, "Photoshop")]

for emp in Employees:
    print(emp.get_details())