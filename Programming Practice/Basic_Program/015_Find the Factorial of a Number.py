from math import factorial


def rec_fun(n):

    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

result = rec_fun(19)
print(result)