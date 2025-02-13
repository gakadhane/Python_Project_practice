num = int(input("enter the value:"))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        if j <= i:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()


for i in range(1, num + 1):
    for j in range(1, i+1):
        if j >= i:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()


for i in range(1, 5):
    for j in range(1, 5):
        if j <= 5-i:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()


for i in range(1, 5):
    for j in range(1, 5):
        if j >= 5-i:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()


for i in range(1, 5):
    for j in range(1, 8):
        if j >= 5-i and j<=3+i:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()


for i in range(1, 5):
    for j in range(1, 8):
        if j >= i and j<=8-i:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()