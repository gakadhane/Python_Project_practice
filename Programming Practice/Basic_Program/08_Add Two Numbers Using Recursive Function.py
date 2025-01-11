# Define a recursive function to add two numbers

def add_number_recursive(x, y):
    if y == 0:
        return x
    else:
        return add_number_recursive(x + 1, y - 1)


# Take input from the user

num1 = 65
num2 = 49

# Call the recursive function to add the two numbers

result = add_number_recursive(num1, num2)

# Print the result

print("the sum of", num1, "and", num2, "is", result)
