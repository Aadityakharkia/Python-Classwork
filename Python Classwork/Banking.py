import math

print("Welcome to jingalala Bank")
print("Please choose a service from the list below:- ")
print("Press 1 for Loan")
print("Press 2 for Withdrawl")
print("Press 3 for Internet Banking")

banking_service = int(input(""))

if (banking_service == 1):
    print("Would you like to take a Simple Interest Loan or Compound Interest Loan")
    print("Press 1 for Simple Interest Loan and press 2 for compound interest loan")
    a = int(input(""))
    if (a == 1):
        print("Please enter the amount you need")
        p = eval(input(""))
        print("Please enter the time required to payback the loan in years")
        t = eval(input(""))
        print("Please enter the rate of interest you desire")
        r = eval(input(""))
        si = p*r*t/100
        print(" You need to pay", si , 'ruppee over', t, "years")
        
    elif (a == 2):
        print("Please enter the amount you need")
        p = eval(input(""))
        print("Please enter the time required to payback the loan in years")
        t = eval(input(""))
        print("Please enter the rate of interest you desire")
        r = eval(input(""))
        ci = p * (pow((1 + r / 100), t))
        print(" You need to pay", ci , 'ruppee over', t, "years")

    else:
        print("Please choose a valid Service from the list given above")

elif (banking_service == 2):
    print("Sorry you are not eligible for this service")
    print("Thankyou for visiting us, have a nice day ahead")
    
 
elif (banking_service == 3):
    print("Sorry you are not eligible for this service")
    print("Thankyou for visiting us, have a nice day ahead")

else:
    print("Please choose a valid Service from the list given above")
