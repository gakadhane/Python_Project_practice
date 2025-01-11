def compound_interest(principal, rate, time):
    amount = principal
    for i in range(time):
        amount = amount * (1 + rate / 100)
    CI = amount - principal
    print("Compound interest is", CI)
    # Driver Code


compound_interest(1200, 5.4, 2)
