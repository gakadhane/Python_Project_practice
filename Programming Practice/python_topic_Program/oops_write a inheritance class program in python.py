# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


# Derived class
class Dog(Animal):
    def __init__(self, name, breed, color):
        super().__init__(name)
        super().__init__(color)
        self.name = name
        self.color = color
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof! and Dog breed is: {self.breed} and dog colour is: {self.color} "


# Another Derived class
class Cat(Animal):
    def __init__(self, name, breed, color):
        super().__init__(name)
        super().__init__(breed)
        self.name = name
        self.breed = breed
        self.color = color

    def speak(self):
        return f"{self.name} says Meow! and cat breed is: {self.breed} and cat colour is: {self.color}"


# Sample usage
dog = Dog("Buddy", "Golden Retriever", "black")
cat = Cat("Whiskers", "parsin", "Gray")

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
