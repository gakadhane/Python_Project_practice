
x = 10

def modify_global():
    global x
    x = 20
    print("inside_funcyion:", x)

mod = modify_global()
print("outside_function", x)

z = 10

def modify_global():
    z = 20
    print("inside_funcyion:", z)

mod = modify_global()
print("outside_function", z)