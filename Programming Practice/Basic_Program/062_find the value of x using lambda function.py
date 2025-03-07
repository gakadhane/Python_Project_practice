#Lambda Functions:
# r is a lambda function that takes an argument q and returns q multiplied by 2.
# s is a lambda function that takes an argument q and returns q multiplied by 3.
r = lambda q : q * 2
s = lambda q : q * 3

#Initial Value of x: We initialize the variable x with the value 2.
x = 2

# First Lambda Function Call: We call the lambda function r with the current value of x (which is 2).
# The function r returns 2 * 2, which is 4, and this value is assigned back to x.
x = r(x)

#Second Lambda Function Call: We call the lambda function s with the current value of x (which is 4).
# The function s returns 4 * 3, which is 12, and this value is assigned back to x.
x = s(x)

#Third Lambda Function Call: We call the lambda function r again with the current value of x (which is 12).
# The function r returns 12 * 2, which is 24, and this value is assigned back to x.
x = r(x)

#Print the Final Value of x: We print the final value of x, which is 24.
print(x)


#Summary of Operations:
# Initial value: x = 2
# After r(x): x = 2 * 2 = 4
# After s(x): x = 4 * 3 = 12
# After r(x): x = 12 * 2 = 24