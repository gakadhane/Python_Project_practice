import gc
import sys
from tkinter.font import names


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
print(person1 == person2)  # Output: True
print(sys.getsizeof(person1))
print(sys.getsizeof(person2))
gc.collect()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
print(person1 != person2)  # Output: True
