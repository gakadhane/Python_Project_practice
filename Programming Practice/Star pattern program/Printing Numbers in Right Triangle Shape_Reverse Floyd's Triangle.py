num = int(input("enter the number:\n"))
for row in range(num):
    for col in range(row + 1):
        print(row, end="")
    print()
# O/P:enter the number:5
# 0
# 11
# 222
# 3333
# 44444

num = int(input("enter the number:\n"))
for row in range(num):
    for col in range(row + 1):
        print(col, end="")
    print()
# O/P: enter the number:5
# 0
# 01
# 012
# 0123
# 01234

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
# O/P:5
# 10
# 9   8
# 7   6   5
# 4   3   2   1
# 0   -1  -2  -3  -4