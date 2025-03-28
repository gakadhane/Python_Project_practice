class Greeting:
    def say_hello(self, name=None, time_of_day=None):
        if name is not None and time_of_day is not None:
            return f"Good {time_of_day}, {name}!"
        elif name is not None:
            return f"Hello, {name}!"
        else:
            return "Hello!"


# Create an instance of Greeting
greet = Greeting()

# Demonstrate polymorphism
print(greet.say_hello("Alice", "morning"))  # Output: Good morning, Alice!
print(greet.say_hello("Bob"))  # Output: Hello, Bob!
print(greet.say_hello())  # Output: Hello!

# In this example, the say_hello method in the Greeting class can handle different numbers of arguments.
# Depending on the arguments passed, it will generate a different greeting message.
# This shows how you can achieve polymorphism through method overloading by using default arguments in Python.
