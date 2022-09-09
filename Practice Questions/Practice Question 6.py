print("Please enter the 3 sides of the triangle ")

a = int(input("Please enter the first side "))
b = int(input("Please enter the second side "))
c = int(input("Please enter the third side "))

if (a==b==c):
    print("Its a Equilateral Triangle ")


elif ( a==b or b==c or c==a):
    print("Its a Isoceles Triangle ")

else:
    print("Its a scalen trianngle ")
