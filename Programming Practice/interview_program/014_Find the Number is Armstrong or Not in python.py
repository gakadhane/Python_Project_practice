num = int(input("Enter the number"))

# Calculate the number of digits in num
str_num = str(num)
order = len(str_num)

# Initialize variables
sum = 0
temp = num

# Calculate the sum of digits raised to the power of num_digits
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# Check if it's an Armstrong number
if sum == num:
    print("This is the armstrong number")
else:
    print("This is not the armstrong number")
