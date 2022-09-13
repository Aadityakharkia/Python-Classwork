import math
a = eval(input("Enter the first number "))
b = eval(input("Enter the second number "))
c = input("Enter the operation ")
d = 0 
if (c == '+'):
    d = a+b
    print(d)
elif (c == '-'):
    d = a - b
    print(d)
elif (c == '*'):
    d = a * b
    print(d)
elif (c == '/'):
    d = a / b
    print(d)
elif (c == '//'):
    d = a // b
    print(d)
elif (c == '**'):
    d = a ** b
    print(d)
else:
    print("The operation sign is invalid")