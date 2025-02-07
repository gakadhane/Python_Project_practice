n = 10
for i in range(1, n):
    for j in range (i):
        print(i, end='  ')
    print( )

s= ["a", "b", "c"]
for i in s:
    print(i)
    for i in s:
        print(i)