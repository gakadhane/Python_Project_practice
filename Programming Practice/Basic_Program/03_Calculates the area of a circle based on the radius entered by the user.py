import math

radius = float(input("Enter the radius:\n"))

pi = 3.14

Area = pi * radius * 2

print("Area of circle with\t" + str(radius) + " is:\t" + str(Area))


# --------------------------------------------------------------------------------------

def area(r):
    area = math.pi * pow(r, 2)
    return print('Area of circle is:', area)


area(4)

#--------------------------

import math

def area(r):
    area = math.pi * pow(r, 2)
    return area

radius = int(input("Enter the radius:\n"))
circle_area = area(radius)
print('Area of the circle is:', circle_area)
