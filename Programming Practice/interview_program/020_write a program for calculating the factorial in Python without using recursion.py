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

#---------------------------------------------------------------------------------
# Input: An integer number
num = 6
# Initialize the factorial variable to 1
factorial = 1
if num < 0:
    print("factorial of 0 is not exist")
if num == 0:
    print("The factorial of 0 is:", 1)
# Calculate the factorial using a for loop
for i in range(1, num + 1):
    factorial *= i      #factorial = factorial * i
# Output: The factorial of the number
print(f"The factorial of {num} is {factorial}")