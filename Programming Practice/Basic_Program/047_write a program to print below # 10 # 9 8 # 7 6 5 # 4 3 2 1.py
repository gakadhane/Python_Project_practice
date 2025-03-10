
def print_pattern():
    num = 10
    count = 4
    while num > 0:
        print("#", end=" ")
        for _ in range(count):
            if num > 0:
                print(num, end=" ")
                num -= 1
        print()
        count -= 1

print_pattern()




def print_pattern():
    num = 10
    count = 1
    while num > 0:
        print("#", end=" ")
        for _ in range(count):
            if num > 0:
                print(num, end=" ")
                num -= 1
        print()
        count += 1

print_pattern()

#Output
# 10
# 9 8
# 7 6 5
# 4 3 2 1

