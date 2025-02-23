def right_aligned_triangle(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end=' ')
        for k in range(i+1):
            print('*', end=' ')
        print()

num_stars = int(input("Enter the number of rows:\n1 "))
right_aligned_triangle(num_stars)
