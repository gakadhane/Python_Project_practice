num = int(input("Enter the number of row\n"))

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
# Enter the number of row
# 5
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print("a", end=" ")
    print()
# a
# a a
# a a a
# a a a a
# a a a a a
