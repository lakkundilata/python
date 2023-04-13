def compound_interst(principal, rate, time):
    principal = float(input("enter the principal amount:"))
    rate = float(input("enter rate of interest:"))
    time = float(input("enter time in year:  "))
    amount = principal * (pow((1+rate/100),time))
    ci = amount - principal
    result=compound_interst(principal,rate,time)
    print(result)
