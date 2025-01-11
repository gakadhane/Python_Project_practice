num1 = 16
num2 = 20
num3 = 55

if num1 > num2 and num1 > num3:
    print("the number is large", num1)
elif num2 > num1 and num2 > num3:
    print("{0} the number is large".format(num2))
else:
    print("the number", (int(num3)), "is large")
