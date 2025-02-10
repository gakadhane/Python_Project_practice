numbers = [1, 2, 3, 4, 5]


def map_lambda(args):
    squared_numbers = map(lambda x: x ** 2, numbers)
    print(list(squared_numbers))


def filter_lambda(args):
    even_number = filter(lambda x: x % 2 ==0, numbers)
    print(list(even_number))

map = map_lambda(numbers)
filter = filter_lambda(numbers)