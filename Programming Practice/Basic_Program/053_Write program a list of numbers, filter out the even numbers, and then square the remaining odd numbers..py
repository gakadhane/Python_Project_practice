number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# Function to Calculate Square: This defines a function named square that takes an argument x and
# returns the square of x (i.e., x raised to the power of 2).
def square(x):
    return x ** 2


# Function to Check for Odd Numbers: This defines a function named even_number that takes an argument x and
# returns True if x is odd (i.e., the remainder when x is divided by 2 is not 0).
# The function is misnamed here as it actually checks for odd numbers, not even numbers.
def even_number(x):
    return x % 2 != 0


# Map Square Function to Odd Numbers: We use the map function to apply the square function to each element in the odd_number iterator.
# This creates an iterator that contains the squares of the odd numbers.
odd_number = filter(even_number, number)
square_odd_number = map(square, odd_number)

# Convert to List and Print: We convert the square_odd_number iterator to a list and store it in the variable new_number.
# Finally, we print the new_number list.
new_number = list(square_odd_number)
print(new_number)

# Explanation:
# The odd numbers from the number list are: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# The squares of these odd numbers are: [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
# So the new_number list contains the squares of the filtered odd numbers.
