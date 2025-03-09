class calculator:
    def add(self, num1, num2):
        return num1 + num2


calu = calculator()
result = calu.add(10, 20)
print(result)

result3 = calculator().add(30,  40)
print(result3)

# both program difference is calu = calculator() and calu = calculator


class calculator:
    def add(self, num1, num2):
        return num1 + num2


calc = calculator
result1 = calc.add(0, 40, 30)
print(result1)

result2 = calculator.add(0, 20, 20)
print(result2)
