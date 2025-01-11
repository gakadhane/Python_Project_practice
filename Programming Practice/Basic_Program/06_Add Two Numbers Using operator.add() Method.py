import operator

# Program to add two numbers

num1 = 12
num2 = 57

# Adding, subtraction, multiplication, power two no.

sum = operator.add(num1, num2)
minus = operator.sub(num1, num2)
mul = operator.mul(num1, num2)
pow = operator.pow(num1, num2)

# result of the value

print("sum of {0} and {1} is {2}".format(num1, num2, sum))
print("sum of {0} and {1} is {2}".format(num1, num2, minus))
print("sum of {0} and {1} is {2}".format(num1, num2, mul))
print("sum of {0} and {1} is {2}".format(num1, num2, pow))
