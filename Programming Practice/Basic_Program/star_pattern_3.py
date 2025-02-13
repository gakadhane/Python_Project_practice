def pyramid_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end='')
        for k in range(2*i+1):
            print('*', end='')
        print()

num_stars = int(input("Enter the number of rows: "))
pyramid_pattern(num_stars)
