string = (input("enter the string:\n"))
length = len(string)

for row in range(0, length):
    for col in range(0, row + 1):
        print(string[col], end="")
    print()



string = (input("enter the string:\n"))
length = len(string)

for row in range(0, length):
    for col in range(0, row + 1):
        print(string[row], end="")
    print()




string = (input("enter the string:\n"))
length = len(string)

for row in range(0, length):
    for j in range(length-row-1):
        print(" ", end=" ")
    for col in range(0, row + 1):
        print(string[col], end=" ")
    print()


string = (input("enter the string:\n"))
length = len(string)

for row in range(0, length):
    for j in range(length-row-1):
        print(" ", end=" ")
    for col in range(0, row + 1):
        print(string[row], end=" ")
    print()