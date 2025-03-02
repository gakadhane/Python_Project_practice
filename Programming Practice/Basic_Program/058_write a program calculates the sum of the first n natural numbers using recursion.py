# This defines a function named sum_of_natural that takes a single argument n, which is expected to be a positive integer.
def sum_of_natural(n):
    # Base Case: If n is less than or equal to 0, the function returns 1. This acts as the stopping condition for the recursion.
    # Recursive Case: If n is greater than 0, the function returns n plus the result of calling sum_of_natural with n - 1. This means the function keeps calling itself with decreasing values of n until it reaches the base case.
    if n <= 0:
        return 1
    else:
        return n + sum_of_natural(n - 1)


# We call the sum_of_natural function with n = 10 and store the result in the variable result.
# We print the result using an f-string for formatted output.
result = sum_of_natural(10)
print(f"natural number:\n{result}")

# Example Walkthrough
# Let's trace the execution of sum_of_natural(10):
# sum_of_natural(10) returns 10 + sum_of_natural(9)
# sum_of_natural(9) returns 9 + sum_of_natural(8)
# sum_of_natural(8) returns 8 + sum_of_natural(7)
# sum_of_natural(7) returns 7 + sum_of_natural(6)
# sum_of_natural(6) returns 6 + sum_of_natural(5)
# sum_of_natural(5) returns 5 + sum_of_natural(4)
# sum_of_natural(4) returns 4 + sum_of_natural(3)
# sum_of_natural(3) returns 3 + sum_of_natural(2)
# sum_of_natural(2) returns 2 + sum_of_natural(1)
# sum_of_natural(1) returns 1 + sum_of_natural(0)
# sum_of_natural(0) returns 1 (base case)

# sum_of_natural(10) = 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 1 = 56
# natural number: 56
