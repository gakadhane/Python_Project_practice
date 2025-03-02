# This defines a function named power that takes two arguments: base (the base number) and exponent (the power to raise the base to).
def power(base, exponent):
    result = 1  # We initialize a variable result to 1. This will hold the cumulative product of multiplying the base.

    for _ in range(exponent):
        result *= base  # We use a for loop to iterate exponent times. In each iteration, we multiply result by the base.

    return result
    # fter the loop completes, we return the value of result, which now holds the result of base raised to the power of exponent.


# Example usage: We call the power function with base set to 2 and exponent set to 5 and print the result.
base = 2
exponent = 5
print(f"{base} to the power of {exponent} is {power(base, exponent)}")
