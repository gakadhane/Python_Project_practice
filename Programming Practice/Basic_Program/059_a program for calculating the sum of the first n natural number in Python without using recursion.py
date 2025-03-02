# This defines a function named sum_of_natural_numbers that takes a single argument n,
# which is expected to be a positive integer.
def sum_of_natural_numbers(n):
    # We initialize a variable total to 0. This will hold the cumulative sum of the numbers from 1 to n.
    total = 0

    # We use a for loop to iterate through each number i from 1 to n (inclusive).
    # In each iteration, we add i to total.
    for i in range(1, n + 1):
        total += i  # Add each number from 1 to n to the total
        # After the loop completes, we return the value of total, which now holds the sum of the first n natural numbers.

    return total


# Example usage
n = 10
print(f"The sum of the first {n} natural numbers is {sum_of_natural_numbers(n)}")
# We call the sum_of_natural_numbers function with the argument 10 and print the result.
