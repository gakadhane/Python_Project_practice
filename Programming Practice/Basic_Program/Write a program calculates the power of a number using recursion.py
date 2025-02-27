def power(x,y):
    if y==0:
        return 1
    else:
        return x * power(x,y-1)

result = power(3,7)
print(result)