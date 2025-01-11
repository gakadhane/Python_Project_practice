def compound_intrest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)


compound_intrest(100, 10.25, 5)
