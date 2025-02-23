for i in range(0, 3):
    print("Hello", end=" ");
    print("Hi")

num = int(input("Enter the number of row\n"))

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print("a", end=" ")
    print()
