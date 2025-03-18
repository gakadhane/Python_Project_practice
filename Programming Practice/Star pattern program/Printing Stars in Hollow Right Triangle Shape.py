num = int(input("enter the number:\n"))

for row in range(0, num):
    for col in range(0, num):
        if row == 0 or col == (num - 1) or row == col:
            print("*", end="")
        else:
            print(end=" ")
    print()
# enter the number: 5
# *****
#  *  *
#   * *
#    **
#     *