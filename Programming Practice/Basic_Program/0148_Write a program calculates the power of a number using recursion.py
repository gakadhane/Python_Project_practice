def power(x, y):
    if y == 0:  # The base case checks if the exponent y is 0. In mathematics, any number raised to the power of 0 is 1. If y is 0, the function returns 1.
        return 1
    else:
        return x * power(x, y - 1)
                          # If y is not 0, the function recursively calls itself with the exponent decreased by 1 (y - 1). The result is multiplied by x.


result = power(3, 7)
print(result)

# Recursion Explanation:
# Recursion involves a function calling itself with modified arguments until a base condition is met. In this case, power calls itself with y decreased by 1 each time, building up the result through multiplication.
#
# For example, power(3, 7) translates to:
# 3 × 𝑝 𝑜 𝑤 𝑒 𝑟 ( 3 , 6 )
# 3 × ( 3 × 𝑝 𝑜 𝑤 𝑒 𝑟 ( 3 , 5 ) )
# 3 × ( 3 × ( 3 × 𝑝 𝑜 𝑤 𝑒 𝑟 ( 3 , 4 ) ) )
# ... and so on ...
#
# until:
# 3 × ( 3 × . . . × ( 3 × 𝑝 𝑜 𝑤 𝑒 𝑟 ( 3 , 0 ) ) )
# When power(3, 0) is called, the base case is met, returning 1.
#
# Final Calculation:
# So, the function effectively calculates:3 to the power 7 = 3 × 3 × 3 × 3 × 3 × 3 × 3 = 2187
