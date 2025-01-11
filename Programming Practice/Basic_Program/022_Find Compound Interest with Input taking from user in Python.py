def compound_intrest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)


Principal = int(input("Enter principal value: "))
Rate = int(input("Enter rate value: "))
Time = int(input("Enter time value: "))

compound_intrest(Principal, Rate, Time)
