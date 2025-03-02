import random


def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)


# Example usage:
min_value = 1
max_value = 100
random_number = generate_random_number(min_value, max_value)
print(f"Generated random number: {random_number}")

# Perform some operations with the random number
print(f"Square of the random number: {random_number ** 2}")
print(f"Square root of the random number: {random_number ** 0.5:.2f}")
print(f"Double the random number: {random_number * 2}")
print(f"Random number modulo 10: {random_number % 10}")
