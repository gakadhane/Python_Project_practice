# solution 1 with For
num = int(input("Enter the number:"))

for i in range(1, 11):
    print(num, '*', i, "=", num * i)

# -------------------------------------------------------
# solution 2 with while loop
n = 3
i = 1

while i <= 10:
    print(n, '*', i, "=", n * i)
    i += 1
