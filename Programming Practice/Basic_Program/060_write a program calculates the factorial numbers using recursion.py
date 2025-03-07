# This defines a function named factorial that takes a single argument n, which is expected to be a non-negative integer.
from functools import reduce


def factorial(n):
    # The base case of the recursion checks if n is equal to 0.
    # If n is 0, the function returns 1. This is based on the mathematical definition that the factorial of 0 is 1.
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
        # If n is not 0, the function returns n multiplied by the result of factorial(n-1).
        # This means the function calls itself with the argument n-1.


print(factorial(5))  # We call the factorial function with the argument 5 and print the result.

"""
Example Walkthrough
Let's trace the execution of factorial(5):
factorial(5) returns 5 * factorial(4)
factorial(4) returns 4 * factorial(3)
factorial(3) returns 3 * factorial(2)
factorial(2) returns 2 * factorial(1)
factorial(1) returns 1 * factorial(0)
factorial(0) returns 1 (base case)

So, we have:
factorial(5) = 5 * factorial(4)
             = 5 * (4 * factorial(3))
             = 5 * (4 * (3 * factorial(2)))
             = 5 * (4 * (3 * (2 * factorial(1))))
             = 5 * (4 * (3 * (2 * (1 * factorial(0)))))
             = 5 * (4 * (3 * (2 * (1 * 1))))
             = 5 * (4 * (3 * (2 * 1)))
             = 5 * (4 * (3 * 2))
             = 5 * (4 * 6)
             = 5 * 24
             = 120
"""




my_list = [1,2,3,4,5]
result = reduce(lambda x,y : x * y, my_list)
print(result)
