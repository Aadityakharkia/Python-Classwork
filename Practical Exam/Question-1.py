a = eval(input("Please input your salary "))
b = eval(input("Please input the year of your service "))
if (b>10):
    c = 10/100*a
    d = c+a
    print("You will get", d , "as a bonus with salary")
elif (b>=6 and b<=10):
    c = 8/100*a
    d = c+a
    print("You will get", d , "as a bonus with salary")
elif (b<6):
    c = 5/100*a
    d = c+a
    print("You will get", d , "as a bonus with salary")
