

def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)


def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=30)
