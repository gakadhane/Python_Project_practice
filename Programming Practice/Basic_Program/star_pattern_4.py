def diamond_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end='')
        for k in range(2*i+1):
            print('*', end='')
        print()
    for i in range(n-1):
        for j in range(i+1):
            print(' ', end='')
        for k in range(2*(n-i-1)-1):
            print('*', end='')
        print()

num_stars = int(input("Enter the number of rows: "))
diamond_pattern(num_stars)
