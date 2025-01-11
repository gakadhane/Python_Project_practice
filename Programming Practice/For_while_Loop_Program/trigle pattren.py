def star_Trangle(num):
    for i in range(num):
        for j in range(num - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()


num = int(input("enter the valur num:"))
star_Trangle(num)