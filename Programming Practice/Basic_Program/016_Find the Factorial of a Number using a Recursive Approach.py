def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# Driver Code
num = 6

# Output: The factorial of the number
print("The factorial of", num, "is", factorial(num))
