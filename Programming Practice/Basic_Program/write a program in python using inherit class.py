# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

# Another Derived class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"

# Sample usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Gray")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!





# Explanation:
# Base Class Animal:
# The Animal class serves as the base class with an __init__ method to initialize the name attribute.
# The speak method is defined as an abstract method that should be implemented by the subclasses.
#
# Derived Class Dog:
# The Dog class inherits from the Animal class and has an additional breed attribute.
# The speak method is overridden to provide a specific implementation for dogs.
#
# Derived Class Cat:
# The Cat class inherits from the Animal class and has an additional color attribute.
# The speak method is overridden to provide a specific implementation for cats.
#
# Sample Usage:
# Instances of Dog and Cat classes are created, and their speak methods are called to demonstrate the functionality.

