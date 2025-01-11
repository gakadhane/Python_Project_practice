# Function for nth Fibonacci number

def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# Driver Program

print(Fibonacci(10))

#-----------------------------------

a = 0
b = 1
num = int(input("Enter the number"))

if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1, num+1):
        c = a+b
        a=b
        b=c
        print(c)