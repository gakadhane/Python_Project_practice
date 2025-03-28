start = int(input("enter the start number"))
end = int(input("enter the end number"))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

#-------------------------------------------------
lower = 2
upper = 10

for num in range (lower, upper + 1):
    if num > 1:
        for i in range (2, num):
            if num % 2 == 0:
                break
        else:
            print(f"Prime number: {num}")

#-------------------------------------------------------

def is_prime(number):
    for i in range (2, number):
        if (number%i == 0):
            return False
    return True

def add(number):
    total = 0
    for i in range (2, number+1):
        if is_prime(i):
            total = total + i
    return total

add(10)