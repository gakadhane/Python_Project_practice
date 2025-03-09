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