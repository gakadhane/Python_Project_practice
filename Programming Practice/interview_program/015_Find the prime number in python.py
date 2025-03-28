num = 10

if num == 1:
    print("it is not a prime number")

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("not prime")
            break
    else:
        print("Prime number")


#--------------------------------------------------------

num = int (input("Enter the number:"))

flag = False # define a flag variable

if num == 1:
    print("number is not prime number")

elif num > 1:
    for i in range (2, num): # check for factors
        if num % i == 0:
            flag = True   # if factor is found, set flag to True
            break   # break out of loop

if flag:        # check if flag is True
    print("number is not prime number")
else:
    print("number is prime number")

#-------------------------------------------------------------

