from abc import ABC, abstractmethod
# Abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    def display_info(self):
        print(f"This is a {self.__class__.__name__}")

# Derived class
class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine has started.")

    def stop_engine(self):
        print(f"The {self.make} {self.model}'s engine has stopped.")

    def display_info(self):
        super().display_info()
        print(f"Make: {self.make}, Model: {self.model}")

# Another derived class
class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine has started.")

    def stop_engine(self):
        print(f"The {self.make} {self.model}'s engine has stopped.")

    def display_info(self):
        super().display_info()
        print(f"Make: {self.make}, Model: {self.model}")


# Sample usage
car = Car("Toyota", "Corolla")
motorcycle = Motorcycle("Yamaha", "MT-07")

car.display_info()
car.start_engine()
car.stop_engine()

print("\n")

motorcycle.display_info()
motorcycle.start_engine()
motorcycle.stop_engine()

# Explanation:
# Abstract Base Class Vehicle:
# The Vehicle class serves as an abstract base class with abstract methods start_engine and stop_engine that must be implemented by derived classes.
# The display_info method is a regular method that provides some common functionality.
#
# Derived Class Car:
# The Car class inherits from the Vehicle class and provides implementations for the abstract methods start_engine and stop_engine.
# The display_info method is overridden to provide additional information specific to cars.
#
# Derived Class Motorcycle:
# The Motorcycle class inherits from the Vehicle class and provides implementations for the abstract methods start_engine and stop_engine.
# The display_info method is overridden to provide additional information specific to motorcycles.
#
# Sample Usage:
# Instances of Car and Motorcycle are created, and their methods are called to demonstrate data abstraction and polymorphism in action.
