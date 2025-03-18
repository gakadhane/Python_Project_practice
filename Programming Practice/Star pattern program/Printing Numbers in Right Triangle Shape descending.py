num = int(input("enter the number"))

for row in range(num, 0, -1):
    for col in range(1, row + 1):
        print(col, end="")
    print()
# O/p:enter the number5
# 12345
# 1234
# 123
# 12
# 1

for row in range(num, 0, -1):
    for col in range(1, row + 1):
        print(row, end="")
    print()
# O/p:
# 55555
# 4444
# 333
# 22
# 1