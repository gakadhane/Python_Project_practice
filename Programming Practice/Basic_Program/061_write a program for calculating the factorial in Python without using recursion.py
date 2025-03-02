# This defines a function named factorial that takes a single argument n, which is expected to be a non-negative integer.
def factorial(n):
    result = 1  # We initialize a variable result to 1. This will hold the cumulative product of the numbers from 1 to n.

    # We use a for loop to iterate through each number i from 1 to n (inclusive).
    # In each iteration, we multiply result by i and update result.
    for i in range(1, n + 1):
        result *= i  # Multiply result by i for each i from 1 to n

    return result  # After the loop completes, we return the value of result, which now holds the factorial of n.


# Example usage: We call the factorial function with the argument 5 and print the result.
n = 5
print(f"The factorial of {n} is {factorial(n)}")
