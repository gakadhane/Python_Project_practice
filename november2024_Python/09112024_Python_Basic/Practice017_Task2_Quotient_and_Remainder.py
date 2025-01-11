# Task for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

num1 = int(input("Enter Dividend:"))
num2 = int(input("Enter Divisor:"))

print("Division of the numbers is:", num1 / num2)

quotient = num1 // num2
remainder = num1 % num2

print("Quotient is:", quotient, "\nRemainder is:", remainder)
