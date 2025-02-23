n = int(input("Enter the number of rows\n"))
for i in range(0, n + 1):
    for j in range(0, 2 * i + 1):
        print("*", end=" ")
    print()

k = 1
for i in range(1, n + 1):
    for j in range(1, k + 1):
        print("*", end=" ")
    k = k + 2
    print()
