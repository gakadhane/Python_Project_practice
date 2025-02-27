
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def square(x):
    return x ** 2

def even_number(x):
    return x % 2 != 0

odd_number = filter(even_number, number)

square_odd_number = map(square,odd_number)

new_number = list(square_odd_number)
print(new_number)

