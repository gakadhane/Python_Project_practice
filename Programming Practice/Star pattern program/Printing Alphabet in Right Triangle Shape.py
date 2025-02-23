num = int(input("enter the number"))
k = ord("A")

for i in range(num):
    for j in range(i + 1):
        print(chr(k), end="")
        k = k + 1
    print()

num = int(input("enter the number"))

for i in range(num):
    k = ord("A") + i
    for j in range(i + 1):
        print(chr(k), end="")
        k = k + 1
    print()
