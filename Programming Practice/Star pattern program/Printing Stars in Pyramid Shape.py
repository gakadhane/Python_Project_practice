# print '*' pyramid with space and odd even number
num = int(input("enter the number in row\n"))

for i in range(0, num):
    for j in range(0, num - i - 1):
        print(end=" ")
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

# print '*' pyramid with odd number
for i in range(0, num):
    for j in range(0, num - i - 1):
        print(end=" ")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# print'*' pyramid in single line program without space in odd number
for i in range(0, num):
    print(' ' * (num - i - 1) + '*' * (2 * i + 1))
