class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Method Overriding
    def area(self):
        return 3.14159 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method Overriding
    def area(self):
        return self.length * self.width


class Calculator():
    # Simulating Method Overloading using variable-length arguments
    def add(self, *args):
        return sum(args)


# Function to demonstrate polymorphism
def display_area(shape):
    print(f"The area of the {type(shape).__name__.lower()} is {shape.area()}")


# Sample usage
circle = Circle(5)
rectangle = Rectangle(4, 6)

display_area(circle)  # Output: The area of the circle is 78.53975
display_area(rectangle)  # Output: The area of the rectangle is 24

# Demonstrating method overloading-like behavior
calculator = Calculator()
print("Sum of 2 and 3:", Calculator.add(2, 3))
print("Sum of 2 and 3:", calculator.add(2, 3))  # Output: Sum of 2 and 3: 5
print("Sum of 1, 2, 3, and 4:", calculator.add(1, 2, 3, 4))  # Output: Sum of 1, 2, 3, and 4: 10

# Explanation:
# Base Class Shape:
# The Shape class serves as the base class with an abstract area method that must be implemented by subclasses.
#
# Derived Classes (Circle, Rectangle):
# Each derived class (Circle, Rectangle) inherits from the Shape class.
# The area method is overridden in each derived class to provide specific implementations for calculating the area of the circle and rectangle.
#
# Class Calculator:
# The Calculator class demonstrates method overloading-like behavior using the add method with variable-length arguments (*args). This allows the method to handle a varying number of arguments.
#
# Polymorphic Function display_area:
# The display_area function takes a Shape object as an argument and calls the area method on it.
# This demonstrates polymorphism, as the area method behaves differently depending on the type of the Shape object passed to the function.
#
# Sample Usage:
# Instances of Circle and Rectangle are created, and their area methods are called through the display_area function to demonstrate polymorphism.
# The Calculator class demonstrates the method overloading-like behavior by handling different numbers of arguments.
