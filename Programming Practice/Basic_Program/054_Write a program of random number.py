# This imports Python's built-in random module, which contains functions for generating random numbers.
import random


# Function Definition:
# The function generate_random_number takes two arguments: min_value and max_value.
# Inside the function, random.randint(min_value, max_value) generates a random integer between min_value and max_value (inclusive) and returns it.
def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)


# Example usage:We define min_value as 1 and max_value as 100.
# We call the generate_random_number function with these values and store the result in the variable random_number.
# We print the generated random number using an f-string for formatted output.
min_value = 1
max_value = 100
random_number = generate_random_number(min_value, max_value)
print(f"Generated random number: {random_number}")

# Perform some operations with the random number
print(f"Square of the random number: {random_number ** 2}")
# This calculates the square of random_number using the ** operator and prints it.
print(f"Square root of the random number: {random_number ** 0.5:.2f}")
# This calculates the square root of random_number using the ** operator (raising it to the power of 0.5) and formats the result to two decimal places using :.2f.
print(f"Double the random number: {random_number * 2}")
# This multiplies random_number by 2 and prints the result.
print(f"Random number modulo 10: {random_number % 10}")
# This calculates the remainder when random_number is divided by 10 using the % operator and prints it.
