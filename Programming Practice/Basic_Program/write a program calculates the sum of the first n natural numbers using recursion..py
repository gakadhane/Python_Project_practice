def sum_of_natural(n):
    if n<= 0:
        return 1
    else:
        return n + sum_of_natural(n-1)

result = sum_of_natural(10)
print(f"natural number:\n{result}")