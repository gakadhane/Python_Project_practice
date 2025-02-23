num = int(input("enter the number:\n"))
for row in range(num):
    for col in range(row + 1):
        print(row, end="")
    print()

num = int(input("enter the number:\n"))
for row in range(num):
    for col in range(row + 1):
        print(col, end="")
    print()

num = int(input("enter the number:\n"))
k = 0
for i in range(num):
    k = k + 1

m = num + k

for row in range(num):
    for col in range(row + 1):
        print(format(m, "<3"), end=" ")
        m = m - 1
    print()
