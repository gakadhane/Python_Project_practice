def diamond_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end='')
        for k in range(2*i+1):
            print('*', end='')
        print()
    for i in range(0, n-1):
        for j in range(0, i+1):
            print(' ', end='')
        for k in range(0, 2*(n-i-1)-1):
            print('*', end='')
        print()

num_stars = int(input("Enter the number of rows: "))
diamond_pattern(num_stars)



def pyramid(row):
    # Top half of the pyramid
    for i in range(row):
        print(' ' * (row - i - 1) + '*' * (2 * i + 1))
    # Bottom half of the pyramid
    for j in range(row - 2, -1, -1):
        print(' ' * (row - j - 1) + '*' * (2 * j + 1))

num_star = int(input("Enter the number of rows: "))
pyramid(num_star)



def pyramid(row):
    for i in range(0, row + 1):
        print(" " * (row - i) + "* " * (i))
    for j in range(1, row + 1):
        print(" " * (j) + "* " * (row - j))

num_star = int(input("Enter the number of rows: "))
pyramid(num_star)
