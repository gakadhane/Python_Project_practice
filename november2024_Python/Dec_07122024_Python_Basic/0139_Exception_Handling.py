print(2+3)
print(x)  # NameError: name 'x' is not defined

x = 10  # IndentationError: unexpected indent

result = 10 / 0 # ZeroDivisionError: division by zero

print(1+"1") # TypeError: unsupported operand type(s) for +: 'int' and 'str

print(int("a")) # ValueError: invalid literal for int() with base 10: 'a'

my_list = [1, 2, 3, 3]
print(my_list[0])
print(my_list[5]) # IndexError: list index out of range

# while True print("Hello World") # SyntaxError: invalid syntax

a = int(input("Ent the num1"))  # ValueError: invalid literal for int() with base 10: 'gaurav'
b = int(input("Ent the num2"))

c = a / b  # ZeroDivisionError: division by zero
print("Result Div is ", c)