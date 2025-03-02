class MathUtils:
    @staticmethod
    def square_root(x):
        return x ** 0.5

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        return n * MathUtils.factorial(n - 1)


# Using static methods: We call the static methods square_root and factorial using the class name MathUtils without creating an instance of the class.
result1 = MathUtils.square_root(25)
result2 = MathUtils.factorial(5)

print("Square Root:", result1)  # Output: Square Root: 5.0
print("Factorial:", result2)  # Output: Factorial: 120

# Key Points:
# No self Parameter: Static methods don't take a self parameter because they don't operate on an instance of the class.
# Utility Functions: They're ideal for utility functions that perform a task independently of the class or its instances.
# Access via Class: They can be accessed directly via the class name without creating an instance.
# Static methods provide a way to logically group related functions within a class, even though they don't access or modify class-specific data
