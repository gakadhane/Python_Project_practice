class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"

# Function to demonstrate polymorphism
def animal_sound(Animal):
    print(Animal.speak())

# Sample usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

animal_sound(dog)   # Output: Buddy says Woof!
animal_sound(cat)   # Output: Whiskers says Meow!
animal_sound(bird)  # Output: Tweety says Tweet!



# Explanation:
# Base Class Animal:
# The Animal class serves as the base class with an __init__ method to initialize the name attribute.
# The speak method is defined as an abstract method that should be implemented by the subclasses.
#
# Derived Classes (Dog, Cat, Bird):
# Each derived class (Dog, Cat, Bird) inherits from the Animal class.
# The speak method is overridden in each derived class to provide specific implementations for each animal.
#
# Polymorphic Function animal_sound:
# The animal_sound function takes an Animal object as an argument and calls the speak method on it.
# This demonstrates polymorphism, as the speak method behaves differently depending on the type of the Animal object passed to the function.
#
# Sample Usage:
# Instances of Dog, Cat, and Bird are created, and their speak methods are called through the animal_sound function to demonstrate polymorphism.