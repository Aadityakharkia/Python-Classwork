print("Please enter 3 numbers to determine the middle number")
print("Please ennter the first number")
a = eval(input(""))
print("Please ennter the second number")
b = eval(input(""))
print("Please ennter the third number")
c = eval(input(""))

if (a>b>c):
    print("The middle number is ",b)

elif (a>c>b):
    print("The middle number is ",c)

elif (b>a>c):
    print("The middle number is ",a)

elif (b>c>a):
    print("The middle number is ",c)

elif (c>b>a):
    print("The middle number is ",b)

elif (c>a>b):
    print("The middle number is ",a)
