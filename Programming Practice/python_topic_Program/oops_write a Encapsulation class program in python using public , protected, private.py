class Person:
    def __init__(self, name, age, salary):
        self.name = name  # Public attribute - accessed directly from outside the class.
        self._age = age  # Protected attribute - not be accessed directly from outside the class.
        self.__salary = salary  # Private attribute

    # Public method
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Salary: {self.__salary}")

    # Getter for the private attribute __salary
    def get_salary(self):
        return self.__salary

    # Setter for the private attribute __salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary amount")


# Derived class
class Employee(Person):
    def __init__(self, name, age, salary, employee_id):
        super().__init__(name, age, salary)
        self.employee_id = employee_id  # Public attribute

    # Method to display employee info
    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        self.display_info()


# Sample usage
employee = Employee("John Doe", 30, 50000, "E12345")
employee.display_employee_info()

# Accessing public attribute
print("\nAccessing public attribute:", employee.name)

# Accessing protected attribute (not recommended but possible)
print("Accessing protected attribute:", employee._age)

# Accessing private attribute directly (will raise an AttributeError)
try:
    print("Accessing private attribute:", employee.__salary)
except AttributeError as e:
    print(e)

# Accessing private attribute using getter
print("Accessing private attribute using getter:", employee.get_salary())

# Modifying private attribute using setter
employee.set_salary(55000)
print("Updated salary:", employee.get_salary())

# Explanation:
# Public Attributes and Methods:
# The name attribute and the display_info method in the Person class are public and can be accessed directly from outside the class.
#
# Protected Attributes:
# The _age attribute is protected, indicated by a single underscore (_). By convention, it should not be accessed directly from outside the class, although it is possible to do so.
#
# Private Attributes:
# The __salary attribute is private, indicated by double underscores (__). It cannot be accessed directly from outside the class and should be accessed via getter and setter methods.
#
# Inheritance:
# The Employee class inherits from the Person class and adds an employee_id attribute along with a method to display employee info.
#
# Sample Usage:
# The program creates an instance of the Employee class and demonstrates how to access and modify public, protected, and private attributes.
