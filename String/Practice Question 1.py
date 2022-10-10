a= input("Please enter a sentence ")
l = len(a)
c = 0 
for i in range(0,l):
    print(a[i])
    if (a[i]=='a'):
            c=c+1
    elif(a[i]=='A'):
        c=c+1
print(" Number of 'a' in the sentence ",a, "is",c)