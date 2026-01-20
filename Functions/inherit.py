from abc import ABC, abstractmethod


class Person(ABC):
    """
    Abstraction:
    - Person is an abstract base class (cannot be instantiated directly).
    - It enforces that every subclass must implement get_role().
    """
    def __init__(self, emp_id, name):
        # Encapsulation (private attributes)
        self.__emp_id = emp_id
        self.__name = name

    # Encapsulation via getters/setters (controlled access)
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        self.__name = name

    @abstractmethod
    def get_role(self):
        """Abstraction: subclasses must define their role."""
        pass

    def display_details(self):
        """
        Polymorphism:
        - This method can be used for any subclass object.
        - It calls get_role(), which is implemented differently in subclasses.
        """
        print("Employee ID:", self.get_emp_id())
        print("Name:", self.get_name())
        print("Role:", self.get_role())


class Employee(Person):
    """
    Inheritance:
    - Employee inherits from Person.
    """
    def __init__(self, emp_id, name, department, salary):
        super().__init__(emp_id, name)
        self.__department = department
        self.__salary = salary

    # Encapsulation: getters/setters for private fields
    def get_department(self):
        return self.__department

    def set_department(self, department):
        if not department.strip():
            raise ValueError("Department cannot be empty.")
        self.__department = department

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary <= 0:
            raise ValueError("Salary must be greater than 0.")
        self.__salary = salary

    def get_role(self):
        return "Employee"

    # Polymorphism: overriding display_details
    def display_details(self):
        super().display_details()
        print("Department:", self.get_department())
        print("Salary:", self.get_salary())
        print("-" * 30)


class Manager(Employee):
    """
    Inheritance:
    - Manager inherits from Employee.
    """
    def __init__(self, emp_id, name, department, salary, team_size):
        super().__init__(emp_id, name, department, salary)
        self.__team_size = team_size

    def get_team_size(self):
        return self.__team_size

    def set_team_size(self, team_size):
        if team_size < 0:
            raise ValueError("Team size cannot be negative.")
        self.__team_size = team_size

    def get_role(self):
        return "Manager"

    # Polymorphism: overriding display_details
    def display_details(self):
        super().display_details()
        print("Team Size:", self.get_team_size())
        print("-" * 30)


# -------------------------
# Main Program (Demo)
# -------------------------
people = [
    Employee(101, "Rashid", "IT", 60000),
    Manager(201, "Kavita", "IT", 90000, 10),
    Employee(102, "Amit", "Finance", 58000)
]

# Polymorphism in action:
# Same method call works differently based on object type (Employee vs Manager)
for person in people:
    person.display_details()
