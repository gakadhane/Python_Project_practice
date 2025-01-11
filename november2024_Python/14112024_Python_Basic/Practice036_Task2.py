# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine
# if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.


side1 = float(input("Enter the side1\n"))
side2 = float(input("Enter the side2\n"))
side3 = float(input("Enter the side3\n"))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if side1 == side2 and side1 == side3 and side2 == side3:
            print("triange is", "equilateral")
        elif side1 == side2 and side2 != side3 and side3 != side1:
            print("trianle is", "isosceles")
        else:
            print("triangle is", "scalane")
    else:
        print("Not a Triangle")
else:
    print("Length is not valid")


#or

def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return "Equilateral"
            elif a == b or b == c or a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            print("Not a Triangle")
    else:
        print("Not a Valid Length")


side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

result = classify_triangle(side1, side2, side3)
print(f"The triangle is classified as: {result}")