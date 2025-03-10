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


def area(r):
    area = math.pi * pow(r, 2)
    return area

radius = int(input("Enter the radius:\n"))
circle_area = area(radius)
print('Area of the circle is:', circle_area)



class Circle:
    def __init__(self, radius):
        # Initialize the circle with a radius
        self.radius = radius
        self.pi = 3.14

    def calculate_area(self):
        # Calculate the area of the circle
        return self.pi * self.radius * self.radius

    def display_area(self):
        # Display the result
        area = self.calculate_area()
        print(f"Area of the circle with radius {self.radius} is: {area}")


# Example usage
radius = float(input("Enter the radius:\n"))
circle = Circle(radius)  # Create an instance of the Circle class
circle.display_area()
