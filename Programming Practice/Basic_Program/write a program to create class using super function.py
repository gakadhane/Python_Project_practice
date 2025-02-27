class parent_class():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"the name is : {self.name} and age is: {self.age}")


class employed(parent_class):
    def __init__(self, name, age, ID):
        super().__init__(name, age)
        self.ID = ID

    def display_info(self):
        super().display_info()
        print(f"the employed ID is: {self.ID}")


class Manager(employed):
    def __init__(self, name, age, ID, department):
        super().__init__(name, age, ID)
        self.departmant = department

    def display_info(self):
        super().display_info()
        print(f"the employe department is: {self.departmant}")


manager = Manager("Gaurav", 33, 111, "Mechanical")
manager.display_info()
