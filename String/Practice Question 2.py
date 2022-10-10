a = input("Please enter a sentence ")
l = len(a)
b=0
for i in range(0,l):
    if(a[i]==a.isupper()):
        b=b+1
print("The number of upercase characters is: ", b)
